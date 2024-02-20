from bs4 import BeautifulSoup
import requests as req
from db_connector import conn, cursor

url = 'https://www.gsmarena.com/makers.php3'

response = req.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

brand_div = soup.find('div', {'class' : 'st-text'})
brand_table = brand_div.find('table')

brand_list_rows = brand_table.find_all('tr')

for row in brand_list_rows:
	brand_a = row.find('a')
	brand = brand_a.get_text(strip = True, separator = '\n').splitlines()[0]
	cursor.execute(f"""INSERT INTO public.items_list_subcategory
                                ("name_en", "name_sk", "name_cz", category_id)
                                VALUES ('{brand}', '{brand}', '{brand}', 5)""")

conn.commit()

conn.close()
cursor.close()
