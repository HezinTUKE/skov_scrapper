from bs4 import BeautifulSoup
import requests as req
from db_connector import conn, cursor

url = 'https://car-dimensions-tool.com/en/make/'

response = req.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

block = soup.find('div', {'class' : 'custom-page'})

cars_block = block.find_all('li')

for i in cars_block :
	cursor.execute(f"""INSERT INTO public.items_list_subcategory
				("name_en", "name_sk", "name_cz", category_id)
				VALUES ('{i.text}', '{i.text}', '{i.text}', 1)""")
conn.commit()

cursor.close()
conn.close()
