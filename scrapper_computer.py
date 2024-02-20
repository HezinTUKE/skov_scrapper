from bs4 import BeautifulSoup
import requests as req
from db_connector import conn, cursor

url = 'https://justwebworld.com/computer-brands-manufacturers/'

response = req.get(url)

print(response)

soup = BeautifulSoup(response.text, 'html.parser')

brands_block = soup.find_all('span', {'style' : """color: #008000;"""})

for i in brands_block:
	brand = i.text

	if 'HP' in brand:
		brand = 'HP'
	elif len(brand) > 25 :
		continue

	cursor.execute(f"""INSERT INTO public.items_list_subcategory
                           ("name_en", "name_sk", "name_cz", category_id)
                           VALUES ('{brand}', '{brand}', '{brand}', 6)""")

conn.commit()

cursor.close()
conn.close()


