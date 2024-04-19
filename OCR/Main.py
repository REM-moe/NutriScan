from prettytable import PrettyTable
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

if __name__ == '__main__':
    oc = OCR()
    recognized_text, text_file_path = oc.get_string_from_image(r"Biscut.jpg", "bilateralFilter")
    print(recognized_text)
    print(text_file_path)
    file_path = f"{text_file_path}"
    matched_substance = read_file_content(file_path=file_path)
    
    IL = Ingredient_Find(matched_substance)
    results = IL.ing_search()
    
    # Create a PrettyTable
    table = PrettyTable()
    table.field_names = ["Name of Substance", "E Code", "Group of Substance", "Harmfulness"]
    
    # Add data to the table
    for res in results:
        table.add_row([res['name_of_substance'], res['e_code'], res['group_of_substance'], res['harmfulness']])
    
    # Print the table
    print(table)
