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
cursor.execute(""" 
    insert into substances (name_of_substance, e_code, group_of_substance, function, harmfulness) values
    ('high fructose corn syrup', '', 'sweetener', 'used to sweeten foods and beverages', 'linked to obesity, diabetes, and other health issues'),
    ('sugar', '', 'sweetener', 'used to sweeten foods and beverages', 'linked to obesity, diabetes, and tooth decay'),
    ('artificial colors', '', 'colorant', 'used to give candies vibrant appearance', 'may cause allergic reactions and hyperactivity in susceptible individuals'),
    ('trans fat', '', 'fat', 'used to enhance flavor and increase shelf life of foods', 'associated with increased risk of heart disease and bad cholesterol levels'),
    ('monosodium glutamate', 'e621', 'flavor enhancer', 'enhances the taste of food', 'can cause headache, flushing, and feelings of discomfort in some individuals'),
    ('tartrazine', 'e102', 'artificial color', 'used to color foods and beverages', 'may cause allergic reactions and hyperactivity in susceptible individuals'),
    ('sodium benzoate', 'e211', 'preservative', 'used to preserve freshness', 'when mixed with vitamin c, can form benzene, a carcinogen'),
    ('aspartame', 'e951', 'artificial sweetener', 'used as a sugar substitute in foods and beverages', 'linked to headaches, anxiety, and other neurological effects in sensitive individuals'),
    ('butylated hydroxyanisole (bha)', 'e320', 'antioxidant', 'prevents food spoilage', 'possible carcinogen and may induce allergic reactions in sensitive individuals'),
    ('sodium nitrite', 'e250', 'preservative', 'used in curing meats to preserve color and prevent bacterial growth', 'can form nitrosamines, potent carcinogens, when heated or combined with stomach acid'),
    ('potassium bromate', '', 'flour improver', 'used to strengthen dough and enhance bread rise', 'possible carcinogen and banned in several countries'),
    ('propyl paraben', 'e216', 'preservative', 'used to extend the shelf life of foods', 'linked to hormone disruption and possibly fertility issues'),
    ('acesulfame k', 'e950', 'artificial sweetener', 'used as a calorie-free sweetener', 'linked to changes in gut bacteria and potential carcinogen in animal studies'),
    ('polysorbate 80', 'e433', 'emulsifier', 'used to mix ingredients together that would not otherwise mix well', 'may negatively affect gut health and cause inflammation'),
    ('carrageenan', 'e407', 'thickener and stabilizer', 'used in dairy and meat products to improve texture', 'linked to gastrointestinal inflammation and discomfort in sensitive individuals'),
    ('highly processed wheat flour', '', 'flour', 'primary ingredient in cookies', 'lacks nutrients and may cause blood sugar spikes'),
    ('palm oil', '', 'fat', 'used as a cheap fat source', 'associated with deforestation and habitat destruction, high in saturated fats which can increase bad cholesterol levels'),
    ('artificial flavor', '', 'flavoring agent', 'enhances the taste of food beyond its original flavor', 'chemical composition can vary widely; some may be harmful or cause allergic reactions'),
    ('salt', '', 'seasoning', 'adds flavor to dishes', 'excessive consumption linked to high blood pressure and cardiovascular issues'),
    ('msg', '', 'flavor enhancer', 'enhances the umami taste in savory dishes', 'can cause headaches and other symptoms in sensitive individuals'),
    ('bha', '', 'preservative', 'used to prevent fats from becoming rancid', 'may have carcinogenic effects in high doses'),
    ('bht', '', 'preservative', 'similar to bha, used to prevent fats from becoming rancid', 'may have carcinogenic effects in high doses'),
    ('potassium sorbate', 'e202', 'preservative', 'used to inhibit mold and yeast growth in foods', 'can cause allergic reactions and stomach upset in some individuals'),
    ('sulfites', '', 'preservative', 'used to prevent discoloration and bacterial growth in foods and beverages', 'can cause allergic reactions, particularly in asthmatic individuals'),
    ('calcium propionate', 'e282', 'preservative', 'used to extend shelf life of baked goods', 'may cause allergic reactions and stomach irritation in some individuals'),
    ('ascorbic acid', 'e300', 'antioxidant', 'used to prevent browning in fruits and vegetables and as a preservative', 'generally recognized as safe, but may cause stomach upset in high doses'),
    ('sodium chloride', 'e508', 'seasoning', 'commonly known as table salt, used to enhance flavor', 'excessive consumption linked to high blood pressure and cardiovascular issues'),
    ('sucralose', 'e955', 'artificial sweetener', 'calorie-free sweetener used in beverages and food products', 'generally recognized as safe, but may cause digestive issues in some individuals'),
    ('saccharin', 'e954', 'artificial sweetener', 'one of the oldest artificial sweeteners, used in various products', 'linked to cancer in animal studies, but not conclusively proven in humans'),
    ('xylitol', '', 'sugar alcohol', 'sweetener used in sugar-free gum and candies', 'can be toxic to dogs and may cause digestive issues in humans if consumed in large amounts'),
    ('stevia', '', 'natural sweetener', 'derived from the leaves of the stevia plant, used as a sugar substitute', 'generally considered safe')
""")


cursor.execute(""" SELECT * FROM substances WHERE e_code = \"e320\"""")
print(cursor.fetchall())

conn.commit()

conn.close()
