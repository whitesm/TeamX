import pymysql
from sqlalchemy import create_engine
import pandas as pd

data = pd.read_csv("../data10.csv")
data = data[['BLTN_GD_ESSN_ID', 'BLTN_CFLV_CGR_NM', 'BRND_NM', 'BLTN_GD_MDL_NM', 'SLER_NM', 'RVW_WRT_DATE', 'RVW_CN', 'RVW_SCOR', 'DELIVER', 'PRODUCT', 'SERVICE']]
columns = ['cn_id', 'item_cate', 'brand', 'model', 'shop_mall', 'wrt_date', 'review', 'score', 'deliver', 'product', 'service']
data.columns = columns

empty_df = pd.DataFrame(columns = columns)

# MySQL Connector using pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

engine = create_engine("mysql+mysqldb://root:"+"1234"+"@localhost/teamax", encoding='utf-8')
conn = engine.connect()

data.to_sql(name='data_table', con=engine, if_exists='append', index=False)
empty_df.to_sql(name='searching_list', con=engine, if_exists='append', index=False)
