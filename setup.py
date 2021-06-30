# code refactored for flask backend

"""from Roadmap_js import Roadmap_jsfn
from Roadmap_python import Roadmap_py

user_input=str(input('select the course type you studied :  A) Python  B) Web development  C) Sql \n\n'))

if user_input.lower()=='python':
    print(Roadmap_py(user_input.lower()))

elif user_input.lower()=='web development':
    print(Roadmap_jsfn(user_input.lower()))

else: 
    print('Please enter the course name correctly')"""

# Start code

import flask
from flask import request
from flask import Flask,jsonify
from gen_rec_engine import Rec_Engine
from Roadmap_js import Roadmap_jsfn
from Roadmap_python import Roadmap_py
import pandas as pd 
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from Levenshtein import ratio
from dbhelper import DB_helper




app=Flask(__name__)

def recommendation_engine(user_data):
    py_data=pd.read_csv('pystat.csv', encoding='latin-1')                             
    js_data=pd.read_csv('jsstat.csv')
    sql_data=pd.read_csv('sqlstat.csv')
    #prepn for python,js,sql

    x1,y1=py_data['course'].values,py_data['channel_name'].values
    x2,y2=js_data['course'].values,js_data['channel_name'].values
    x3,y3=sql_data['course'].values,sql_data['channel_name'].values

    engine=Rec_Engine(cosine_similarity, ratio)
    recommendations=engine(user_data,x1,x2,x3,y1,y2,y3)

    return recommendations


def roadmap(user_input):  #roadmap for python and web dev courses only

    if user_input.lower()=='python':
        user_roadmap_py=Roadmap_py(user_input.lower())
        return user_roadmap_py

    elif user_input.lower()=='web development':
        user_roadmap_js=Roadmap_jsfn(user_input.lower())
        return user_roadmap_js

    else: 
        print('Please enter the course name correctly')

db=DB_helper(host='localhost',port=3306,user='root',passwd='password123',database='My_DB')

# POST method has not been used yet

@app.route("/predict",methods=["GET"])
def predict():
    data={'user_id':'shu123', 'user_name':'Shubham Kumar','user_input' : 'js' , 'user_hist' : 'python for beginners'}
    user_input=data['user_input']
    user_hist=data['user_hist']
    user_id=data['user_id']
    user_name=data['user_name']
    response={}

    if user_hist is not None:
        response['history']=recommendation_engine(user_hist)
        user_courses=response['history']
        if user_id not in db.fetch_all(col_name='user_id'):
            db.insert_val(user_id,user_name,user_input,user_courses)
        else:
            db.update(user_id)

    if user_input is not None:
        response['recommendations']=recommendation_engine(user_input)
        user_courses=response['recommendations']
        if user_id not in db.fetch_all(col_name='user_id'):
            db.insert_val(user_id,user_name,user_input,user_courses)
        else:
            db.update(user_id)

    

    return jsonify(response)

    

@app.route("/My Roadmap",methods=["GET"])  
def roadmap():
    data=request.get_json(force=True)
    cours_type=data['user_input']
    new_response={}
    if course_type is not None:
        new_response['user_roadmap']=roadmap(course_type)

    return jsonify(new_response)



if __name__ == "__main__":
    app.run(debug=True)






 



