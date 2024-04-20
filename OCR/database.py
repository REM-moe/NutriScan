#-*- coding: utf-8 -*-
import sqlite3 as sql

conn = sql.connect('product_substances.db')

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

# insert all substances into the table
cursor.execute(""" INSERT INTO substances (name_of_substance, e_code, group_of_substance, function, harmfulness) VALUES
('High Fructose Corn Syrup', '', 'Sweetener', 'Used to sweeten foods and beverages', 'Linked to obesity, diabetes, and other health issues'),
('Sugar', '', 'Sweetener', 'Used to sweeten foods and beverages', 'Linked to obesity, diabetes, and tooth decay'),
('Artificial Colors', '', 'Colorant', 'Used to give candies vibrant appearance', 'May cause allergic reactions and hyperactivity in susceptible individuals'),
('Trans Fat', '', 'Fat', 'Used to enhance flavor and increase shelf life of foods', 'Associated with increased risk of heart disease and bad cholesterol levels'),
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
('Artificial Flavor', '', 'Flavoring Agent', 'Enhances the taste of food beyond its original flavor', 'Chemical composition can vary widely; some may be harmful or cause allergic reactions'),
('Salt', '', 'Seasoning', 'Adds flavor to dishes', 'Excessive consumption linked to high blood pressure and cardiovascular issues'),
('MSG', '', 'Flavor Enhancer', 'Enhances the umami taste in savory dishes', 'Can cause headaches and other symptoms in sensitive individuals'),
('BHA', '', 'Preservative', 'Used to prevent fats from becoming rancid', 'May have carcinogenic effects in high doses'),
('BHT', '', 'Preservative', 'Similar to BHA, used to prevent fats from becoming rancid', 'May have carcinogenic effects in high doses'),
('Potassium Sorbate', 'E202', 'Preservative', 'Used to inhibit mold and yeast growth in foods', 'Can cause allergic reactions and stomach upset in some individuals'),
('Sulfites', '', 'Preservative', 'Used to prevent discoloration and bacterial growth in foods and beverages', 'Can cause allergic reactions, particularly in asthmatic individuals'),
('Calcium Propionate', 'E282', 'Preservative', 'Used to extend shelf life of baked goods', 'May cause allergic reactions and stomach irritation in some individuals'),
('Ascorbic Acid', 'E300', 'Antioxidant', 'Used to prevent browning in fruits and vegetables and as a preservative', 'Generally recognized as safe, but may cause stomach upset in high doses'),
('Sodium Chloride', 'E508', 'Seasoning', 'Commonly known as table salt, used to enhance flavor', 'Excessive consumption linked to high blood pressure and cardiovascular issues'),
('Sucralose', 'E955', 'Artificial Sweetener', 'Calorie-free sweetener used in beverages and food products', 'Generally recognized as safe, but may cause digestive issues in some individuals'),
('Saccharin', 'E954', 'Artificial Sweetener', 'One of the oldest artificial sweeteners, used in various products', 'Linked to cancer in animal studies, but not conclusively proven in humans'),
('Xylitol', '', 'Sugar Alcohol', 'Sweetener used in sugar-free gum and candies', 'Can be toxic to dogs and may cause digestive issues in humans if consumed in large amounts'),
('Stevia', '', 'Natural Sweetener', 'Derived from the leaves of the Stevia plant, used as a sugar substitute', 'Generally considered safe')
""")

cursor.execute(""" SELECT * FROM substances WHERE e_code = \"E320\"""")
print(cursor.fetchall())

conn.commit()

conn.close()
