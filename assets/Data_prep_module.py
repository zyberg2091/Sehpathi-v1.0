# content based personalized simple rec engine- data_engine

import pandas as pandas
import numpy as np
import csv
import json

class Data_Engine():
    def __init__(self,course,c1,c2,c3,c4,c5):
            self.data_json_1=c1
            self.data_json_2=c2
            self.data_json_3=c3
            self.data_json_4=c4
            self.data_json_5=c5
            self.course=course
    def data_prep(self):

        list_data=[self.data_json_1,self.data_json_2,self.data_json_3,self.data_json_4,self.data_json_5]
        if self.course=='python' or self.course=='sql' or self.course=='js':
            coursefile=open(f'{self.course}.csv','w', newline='',encoding='utf-8')
            coursera=csv.writer(coursefile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for data in list_data:
                output_file=open(data,'r',encoding='utf-8')
                files=json.load(output_file)
                items=files['items']
                for item in items:
                    title=item['snippet']['title']
                    channel=item['snippet']['channelTitle']
                    coursera.writerow([title,channel])

    

pydata=Data_Engine('python','Python files/pycourse1.json','Python files/pycourse2.json','Python files/pycourse3.json','Python files/pycourse4.json','Python files/pycourse5.json')

pydata.data_prep()
