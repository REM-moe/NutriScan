from OCR import *
from fuzzywuzzy import fuzz
import sqlite3 as sql
import re
class StringMatching:
    # Function to read text from file
    def read_text_from_file(file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text

    def fuzzy_string_matching_ratio(string_from_OCR: str, string_from_db: str) -> int:
        # Force lowercase characters to make levenshtein more accurate
        string_from_OCR, string_from_db = string_from_OCR.lower(), string_from_db.lower()

        # Filter all characters that are not present in substances' names
        regex_to_filter_noise_from_string = re.compile('[^a-zA-Z0-9\'-/ ]')
        # string_from_OCR = string_from_OCR.sub("", string_from_OCR)
        # string_from_db = string_from_OCR.sub("", string_from_db)

        # Filter additional spaces
        string_from_OCR = ' '.join(filter(None, string_from_OCR.split(' ')))
        print(string_from_OCR)
        # Return Levenshtein ratio of input strings
        return fuzz.ratio(string_from_OCR, string_from_db)

    def check_in_database(substance):
        conn = sql.connect('product_substances.db')
        cursor = conn.cursor()

        print(substance)
        cursor.execute(f'SELECT name_of_substance, harmfulness FROM substances WHERE name_of_substance="{substance}"')
        print(cursor.fetchone())



    def match_string_with_database_from_file(self, file_path:str) -> list:
        # Read text from file
        string_from_OCR = self.read_text_from_file(file_path)

        # Initialize a list to store all matched substances
        matched_substances = []

        # Connect to the database
        conn = sql.connect('product_substances.db')
        cursor = conn.cursor()

        # Determine which column to search based on the format of the OCR string
        string_from_OCR_no_space = ''.join(filter(None, string_from_OCR.split(' ')))
        e_check_regex = re.compile("^.{0,2}[0-9]{2,3}.{0,2}$")
        if re.match(e_check_regex, string_from_OCR_no_space):
            cursor.execute("SELECT e_code FROM substances")
        else:
            cursor.execute("SELECT name_of_substance FROM substances")

        # Iterate over database results
        for substance in cursor.fetchall():
            substance_name = substance[0]
            # Calculate fuzzy ratio
            # check_in_database(substance_name)
            ratio = self.fuzzy_string_matching_ratio(string_from_OCR_no_space, substance_name)
            # # If ratio is above a certain threshold, consider it a match
            if ratio > 7:  # Adjust threshold as needed
                print(substance_name)
                matched_substances.append(substance_name)

        # Close database connection
        conn.close()

        return matched_substances