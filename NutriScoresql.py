import json
import sqlite3
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

class User:
    def __init__(self, userid, group, country, age, gender, education, incomes):
        self.userid = userid
        self.group = group
        self.country = country
        self.age = age
        self.gender = gender
        self.education = education
        self.incomes = incomes

    def __str__(self):
        return "{} ({}) - Cumulus ID: {}".format(self.userid, self.group, self.country, self.age, self.gender, self.education, self.incomes)

@app.route('/', methods=['POST'])
    
def post_userdata():
    u = json.loads(request.data)
    user = User(u['userid'], u['group'], u['country'], u['age'], u['gender'], u['education'], u['incomes'])
    save_user_to_sql(user)

    return "User data received!", 201



def save_user_to_sql(user):
    conn = sqlite3.connect('nutriscore.db')
    print("Successfully Connected to SQLite")
    userid = user.userid
    group = user.group
    country = user.country
    age = user.age
    gender = user.gender
    education = user.education
    incomes = user.incomes
    conn.execute("INSERT INTO user_infor VALUES ('%s','%s','%s','%s','%s','%s','%s')" %(userid, group, country, age, gender, education, incomes))
    conn.commit()
    print("Successfully saved data to SQLite")

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run() 
