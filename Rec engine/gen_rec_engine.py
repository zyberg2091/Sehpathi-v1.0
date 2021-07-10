import numpy as np
import pandas as pd
from Levenshtein import ratio
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class Rec_Engine():

  def __init__(self, cosine_similarity, ratio):
    self.cosine_similarity=cosine_similarity
    self.ratio=ratio
  

  def _data(self,x1,x2,x3,y1,y2,y3):
    x_data,y_data=[],[]
    for (i,j,k),(i1,j1,k1) in zip(zip(x1,x2,x3),zip(y1,y2,y3)):
      x_data.append(i),y_data.append(i1)
      x_data.append(j),y_data.append(j1)
      x_data.append(k),y_data.append(k1)
    
    return np.array(x_data),np.array(y_data)


  def __call__(self,user_input,x1,x2,x3,y1,y2,y3):

      scores={}
      model=SentenceTransformer('stsb-distilbert-base')
      x_data,y_data=self._data(x1,x2,x3,y1,y2,y3)

      course_database=x_data

      encodings_database=model.encode(course_database)

      user_encoding=model.encode([user_input])

      for i,encoding in enumerate(encodings_database):
        sim_score=self.cosine_similarity(user_encoding,[encoding])
        scores[i]=sim_score

      best_score=max(scores.values())
      # print('bestscore : ',best_score)
      # print('\n')

      #suggesting top 10 courses/top 5 courses

      top_10_scores=list(sorted(scores.values(),reverse=True))[:10]    #sorted scores
      top_10_courses=[(course_database[i[0]],y_data[i[0]],list(i[1][0])) for i in [(key,val) for key,val in scores.items() if val in top_10_scores] if x_data[i[0]]==course_database[i[0]]]

      unique_top_scores=sorted(np.unique(top_10_scores),reverse=True)

      #suggest courses in descending order,threshold score is 0.58 which is taken after experiments.

      top_10_preferences=[]
      for i in unique_top_scores:
        for courses in top_10_courses:
          if courses[2][0]==i and i>0.58:
            top_10_preferences.append(courses)

      # predict top 5 courses if top_10_preferences is null

      if len(top_10_preferences)==0:
        top_5_preferences=[]
        top_5_scores=np.array(top_10_scores[:5]).ravel()

        for courses in top_10_courses:
          if courses[2][0] in top_5_scores:
            top_5_preferences.append(courses)

      #   print(top_5_preferences)   #sorted order
      #   print('\n')

      # else:
      #   print(top_10_preferences)  #sorted order
      #   print('\n')


      # top_5_scores=np.array(top_10_scores[:5]).ravel()
      # top_5_scores

      # syntactic simalrity measurement using fuzzy matching with levenshetien distance and ratio

      final_course_dis,sync_score=[],[]
      
      if len(top_10_preferences)!=0:
        sub=[course[0].lower() for course in top_10_preferences]          
        author=[course[1] for course in top_10_preferences]
        sem_score=[course[2] for course in top_10_preferences]
      else:
        sub=[course[0].lower() for course in top_5_preferences]
        author=[course[1] for course in top_5_preferences]
        sem_score=[course[2] for course in top_5_preferences]  

      for course,ch_name,s in zip(sub,author,sem_score):
        overlap=np.intersect1d(np.array([i for i in course]),np.array([i for i in user_input.lower()]))
        if len(overlap)>0:   
            r=self.ratio(user_input.lower(),course)
            sync_score.append(r)
            if len(top_10_preferences)!=0 and r>0.45:                                                                    # threshold val is selected after few experiments
              final_course_dis.append((course,ch_name,f'syntactic_s : {r}',f'semtantic_s : {s}'))
            elif len(top_10_preferences)==0:                                                          # print top_3_preferences ignoring syntactic scores
              final_course_dis.append((course,ch_name,f'syntactic_s : {r}',f'semtantic_s : {s}'))

      if final_course_dis is not None: 
        return f'user is trying to search for courses like: {final_course_dis}'

      else:
        return 'error has occured'
      




"""if __name__=='__main__':


  py_data=pd.read_csv('pystat_new.csv')
  js_data=pd.read_csv('jsstat_new.csv')
  sql_data=pd.read_csv('sqlstat_new.csv')
  #prepn for python,js,sql

  x1,y1=py_data['course'].values,py_data['channel_name'].values
  x2,y2=js_data['course'].values,js_data['channel_name'].values
  x3,y3=sql_data['course'].values,sql_data['channel_name'].values
  user_input=str(input('course searched : \n'))
  engine=Rec_Engine(cosine_similarity, ratio)
  print(engine(user_input,x1,x2,x3,y1,y2,y3))"""






