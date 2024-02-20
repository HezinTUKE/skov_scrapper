import pandas as pd
import requests as req

from db_connector import conn, cursor

url = 'https://sk.wikipedia.org/wiki/Zoznam_okresov_na_Slovensku'

response = req.get(url)

table = pd.read_html(response.text)
data = table[0].values.tolist()

for row in data:
	reg = row[3]
	dist = row[0]

	cursor.execute(f"""SELECT id
			FROM public.locations_regions
			WHERE region = '{reg}';""")

	region_id = cursor.fetchone()

	conn.commit()

	region_id = region_id[0]

	try :
		cursor.execute(f"""INSERT INTO public.locations_districts
				(district, region_id)
				VALUES('{dist}', {region_id});""")
	except Exception as ex :
		print(reg)
	conn.commit()

conn.close()
cursor.close()
