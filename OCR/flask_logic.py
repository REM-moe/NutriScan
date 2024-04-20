from flask import Flask, request, jsonify
import os
from datetime import datetime
from nutri_logic import NutriScan

path = ""
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    global path
    if 'image' not in request.files:
        return 'No image provided', 400

    file = request.files['image']
    if file.filename == '':
        return 'No image selected', 400

    # Generate a unique filename based on the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'image_{timestamp}.jpg'
    
    # Save the file to the desired location
    file_path = os.path.join('/home/rem/WORK/NutriScan/OCR', filename)
    
    file.save(file_path)
    path = file_path
    print(f"{path}\n\n\n\n")
    # Return the filename along with the success message
    return jsonify({'filename': filename, 'message': 'Image uploaded successfully' }), 200


@app.route('/get_data', methods=['GET'])
def get_data():
    nutri = NutriScan(path)
    result = nutri.scan()
    return jsonify({'result':result})
     

if __name__ == '__main__':
    app.run(debug=True,  host="0.0.0.0", port =50001)
