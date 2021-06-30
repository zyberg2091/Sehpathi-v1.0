import pandas as pd
import numpy as np 
import re

# Python courses

def Roadmap_py(user_input):

    def python(py_data):

        py_courses=py_data['course'].values
            
        count=0
        ds_course_list,cn_course_list,backend_course_list,dsal_course_list=[],[],[],[]
        for course in py_courses:
            try:
                course=' '.join([word.lower() if word.isalpha() else word for word in course.split()])
                if re.search('data science',course.lower()) or re.search('ml',course.lower()) or re.search('machine',course.lower()):
                    ds_course_list.append(course)
                elif re.search('socket programming',course.lower()) or re.search('networking',course.lower()):
                    cn_course_list.append(course)
                elif re.search('django',course.lower()) or re.search('flask',course.lower()):
                    backend_course_list.append(course)
                elif re.search('data structures',course.lower()):
                    dsal_course_list.append(course)
            except:
                count+=1
                # print(course)
                continue
        
        # print("null courses : %d" % count)
        return ds_course_list,cn_course_list,backend_course_list,dsal_course_list





    #Mapping python roadmap

    py_dict={}     
    py_data=pd.read_csv('pystat.csv',encoding='latin-1')
    ds_course_list,cn_course_list,backend_course_list,dsal_course_list = python(py_data)
    py_dict['data_science']=ds_course_list
    py_dict['comp_networking']=cn_course_list
    py_dict['backend_dev']=backend_course_list
    py_dict['data_structures']=dsal_course_list

    categories=['data_structures','backend_dev','data_science','comp_networking']

    path=str(input('select domain of study : A) data_structures  B) backend_dev  C) data_science  D) comp_networking \n\n'))

    if path==categories[2] and user_input.lower()=='python':
        print(py_dict['data_science'])

    elif path==categories[0] and user_input.lower()=='python':
        print(py_dict['data_structures'])

    elif path==categories[3] and user_input.lower()=='python':
        print(py_dict['comp_networking'])

    elif path==categories[1] and user_input.lower()=='python':
        print(py_dict['backend_dev'])

    else:
        pass



