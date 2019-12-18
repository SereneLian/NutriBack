import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("nutriscore.db")
conn.execute('''CREATE TABLE user_infor
         (user_id, user_group, user_country, user_age, user_gender, user_education, user_incomes)''')
conn.commit()
