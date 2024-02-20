import pandas as pd
from db_connector import conn, cursor
import requests as req

url = 'https://sk.wikipedia.org/wiki/Zoznam_krajov_na_Slovensku'

response = req.get(url)

pd_html = pd.read_html(url)

reg_list = pd_html[0].values.tolist()

del reg_list[-1]

for reg in reg_list:
	_reg = reg[1]
	cursor.execute(f"""INSERT INTO public.locations_regions
			(region, coutry_id)
			VALUES('{_reg}', 1);
			""")

conn.commit()

cursor.close()
conn.close()
