from flask import Flask, request, jsonify
import os
from datetime import datetime
from nutri_logic import NutriScan

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
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
    print(f"Image saved at: {file_path}\n\n")

    nutri = NutriScan(file_path)
    result = nutri.scan()
    print(result)

    # Return 'Safe' if result is empty
    if not result:
        return jsonify({'result': 'Safe'}), 200

    # Otherwise, format the result as a list of dictionaries
    
    print(result)
    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=50001)

