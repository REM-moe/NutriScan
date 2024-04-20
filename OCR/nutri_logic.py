from Ingredient_Finder import Ingredient_Find
from OCR import OCR

def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

class NutriScan:

    def __init__(self, image) -> None:
        self.image = image

    def scan(self):
        oc = OCR()
        recognized_text, text_file_path = oc.get_string_from_image(f"{self.image}", "bilateralFilter")
        file_path = f"{text_file_path}"
        matched_substance = read_file_content(file_path=file_path)
        
        IL = Ingredient_Find(matched_substance)
        results = IL.ing_search()
        return results
