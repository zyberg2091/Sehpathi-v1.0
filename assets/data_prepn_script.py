import csv 
import json



def data_prep(list_data,fname):

  coursefile=open(f'{fname}.csv','w', newline='',encoding='utf-8')
  coursera=csv.writer(coursefile,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  for course in list_data:
    with open(course,'r',encoding='utf-8') as output_file:
      files=json.load(output_file)
    items=files['items']
    for item in items:
      title=item['snippet']['title']
      channel=item['snippet']['channelTitle']
      coursera.writerow([title,channel])

if __name__=="__main__":
  c1,c2,c3,c4,c5,fname=str(input()),str(input()),str(input()),str(input()),str(input()),str(input())
  list_data=[c1,c2,c3,c4,c5]
  data_prep(list_data,fname)

