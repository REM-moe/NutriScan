import sqlite3

class Ingredient_Find:

    def __init__(self, paragraph):
        self.paragraph = paragraph 

    def ing_search(self):
        
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        # cleaning table - only for debug
        cursor.execute("DROP TABLE IF EXISTS substances")

        # create table of substances
        cursor.execute(""" CREATE TABLE IF NOT EXISTS substances(
                name_of_substance text,
                e_code text,
                group_of_substance text,
                function text,
                description text,
                harmfulness integer
                );""")
        
        cursor.execute(""" INSERT INTO substances (name_of_substance, e_code, group_of_substance, function, harmfulness) VALUES
               
                ('High Fructose Corn Syrup', '', 'Sweetener', 'Used to sweeten foods and beverages', 'Linked to obesity, diabetes, and other health issues'),
                ('Sugar', '', 'Sweetener', 'Used to sweeten foods and beverages', 'Linked to obesity, diabetes, and tooth decay'),
                ('Artificial Colors', '', 'Colorant', 'Used to give candies vibrant appearance', 'May cause allergic reactions and hyperactivity in susceptible individuals'),
                ('Fat', '', 'Fat', 'Used to enhance flavor and increase shelf life of foods', 'Associated with increased risk of heart disease and bad cholesterol levels'),
                ('Monosodium Glutamate', 'E621', 'Flavor Enhancer', 'Enhances the taste of food', 'Can cause headache, flushing, and feelings of discomfort in some individuals'),
                ('Tartrazine', 'E102', 'Artificial Color', 'Used to color foods and beverages', 'May cause allergic reactions and hyperactivity in susceptible individuals'),
                ('Sodium Benzoate', 'E211', 'Preservative', 'Used to preserve freshness', 'When mixed with vitamin C, can form benzene, a carcinogen'),
                ('Aspartame', 'E951', 'Artificial Sweetener', 'Used as a sugar substitute in foods and beverages', 'Linked to headaches, anxiety, and other neurological effects in sensitive individuals'),
                ('Butylated Hydroxyanisole (BHA)', 'E320', 'Antioxidant', 'Prevents food spoilage', 'Possible carcinogen and may induce allergic reactions in sensitive individuals'),
                ('Sodium Nitrite', 'E250', 'Preservative', 'Used in curing meats to preserve color and prevent bacterial growth', 'Can form nitrosamines, potent carcinogens, when heated or combined with stomach acid'),
                ('Potassium Bromate', '', 'Flour Improver', 'Used to strengthen dough and enhance bread rise', 'Possible carcinogen and banned in several countries'),
                ('Propyl Paraben', 'E216', 'Preservative', 'Used to extend the shelf life of foods', 'Linked to hormone disruption and possibly fertility issues'),
                ('Acesulfame K', 'E950', 'Artificial Sweetener', 'Used as a calorie-free sweetener', 'Linked to changes in gut bacteria and potential carcinogen in animal studies'),
                ('Polysorbate 80', 'E433', 'Emulsifier', 'Used to mix ingredients together that would not otherwise mix well', 'May negatively affect gut health and cause inflammation'),
                ('Carrageenan', 'E407', 'Thickener and Stabilizer', 'Used in dairy and meat products to improve texture', 'Linked to gastrointestinal inflammation and discomfort in sensitive individuals'),
                ('Highly Processed Wheat Flour', '', 'Flour', 'Primary ingredient in cookies', 'Lacks nutrients and may cause blood sugar spikes'),
                ('Palm Oil', '', 'Fat', 'Used as a cheap fat source', 'Associated with deforestation and habitat destruction, high in saturated fats which can increase bad cholesterol levels'),
                ('Artificial Flavor', '', 'Flavoring Agent', 'Enhances the taste of food beyond its original flavor', 'Chemical composition can vary widely; some may be harmful or cause allergic reactions');

            """)

        cursor.execute("SELECT name_of_substance, e_code, group_of_substance, harmfulness FROM substances WHERE INSTR(?, name_of_substance) > 0", (self.paragraph,))
        substances = cursor.fetchall()  

        results = []

        for substance in substances:
            name_of_substance = substance[0]
            e_code = substance[1]
            group_of_substance = substance[2]
            harmfulness = substance[3]

            results.append({'name_of_substance': name_of_substance, 'e_code': e_code, 'group_of_substance': group_of_substance, 'harmfulness': harmfulness})

        conn.close()
        return results