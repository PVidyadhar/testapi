import pymysql
from decimal import Decimal
from flask import jsonify
def query(querystr,return_json=True):
    connection = pymysql.connect(host='localhost',user='root',password='Vidya@no7',db='testapi',cursorclass=pymysql.cursors.DictCursor)
    connection.begin()
    mycursor = connection.cursor()
    mycursor.execute(querystr)
    result = encode(mycursor.fetchall())
    connection.commit()
    mycursor.close()
    connection.close()
    if return_json:
        return jsonify(result)
    else:
        return result

def encode(data):
    for row in data:
        for key,value in row.items():
            if isinstance(value,Decimal):
                row[key]=str(value)
    return data
