import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API"))
model = genai.GenerativeModel('gemini-pro')

class GenaerateResults:  
    
    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def get_answer(self):
      senetence = ""
      with open(self.filepath, 'r') as file:
          senetence = file.read()


          prompt = f"""
              this sentences {senetence} contains names of ingredients or things that are consumed, list the effects of them on human body like smallest negative efffects 
                    """
          response = model.generate_content(prompt)
          return response.text