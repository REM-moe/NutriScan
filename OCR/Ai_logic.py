import pathlib
from google.generativeai import GenerativeModel

# Replace with your Gemini API key
API_KEY = "YOUR_API_KEY"

# Path to your text file
text_file_path = pathlib.Path("ingredients.txt")


# Function to extract and replace sentences with ingredients
def rewrite_with_ingredients(file_path, model):
  with open(file_path, "r") as file:
    text = file.read()
  sentences = text.split(".")

  # Generate ingredients for each sentence and build new content
  new_content = ""
  for sentence in sentences:
    sentence = sentence.strip()
    prompt = f"List the potential ingredient names from the sentence: (the sentence is from an OCR system){sentence}"
    content = [GenerativeModel.Content.text(prompt)]
    response = model.generate_content(content)
    generated_text = response.text.strip()

    # Combine generated ingredients with separator (e.g., comma)
    new_content += generated_text + ", "

  # Remove trailing comma and newline
  new_content = new_content[:-2]

  # Overwrite the file with new content
  with open(file_path, "w") as file:
    file.write(new_content)


# Create a GenerativeModel object
model = GenerativeModel(model="gemini-pro", api_key=API_KEY)

# Rewrite the text file
rewrite_with_ingredients(text_file_path, model)

print(f"Successfully rewrote {text_file_path} with ingredient names.")
