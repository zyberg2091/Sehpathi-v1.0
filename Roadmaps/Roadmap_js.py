import pandas as pd
import numpy as np 
import re

#web dev courses 

def Roadmap_jsfn(user_input):

    def web_dev(js_courses):

        count=0
        w_web_course_list,w_ht_course_list,w_js_course_list,w_dsal_course_list=[],[],[],[]
        for course in js_courses:
            try:
                course=' '.join([word.lower() if word.isalpha() else word for word in course.split()])
                if re.search('web development',course.lower()) or re.search('web dev',course.lower()) or re.search('web',course.lower()):
                    w_web_course_list.append(course)
                elif re.search('html',course.lower()) or re.search('css',course.lower()):
                    w_ht_course_list.append(course) 
                elif re.search('javascript',course.lower()) or re.search('js',course.lower()):
                    w_js_course_list.append(course)
                elif re.search('data structures',course.lower()):
                    w_dsal_course_list.append(course)

            except:
                # print(course)
                count+=1
                continue

        # print("null courses %d" % count)
        return w_web_course_list,w_ht_course_list,w_js_course_list,w_dsal_course_list



    path=str(input('select domain of course study : A) general web development  B) html&css  C) javascript  D) data structures with js \n\n'))
    categories=['general web development','html&css','javascript','data structures']

    js_data = pd.read_csv('jsstat.csv')
    js_courses=js_data['course'].values

    js_dict={}
    w_web_course_list,w_ht_course_list,w_js_course_list,w_dsal_course_list = web_dev(js_courses)
    js_dict['general web development']=w_web_course_list
    js_dict['html&css']=w_ht_course_list
    js_dict['javascript']=w_js_course_list
    js_dict['data structures']=w_dsal_course_list

    #mapping web dev roadmap



    try:
        if path==categories[0] and user_input.lower()=='web development':
            print(js_dict[categories[0]])
        elif path==categories[1] and user_input.lower()=='web development':
            print(js_dict[categories[1]])
        elif path==categories[2] and user_input.lower()=='web development':
            print(js_dict[categories[2]])
        elif path==categories[3] and user_input.lower()=='web development':
            print(js_dict[categories[3]])

    except:
        print("Something went wrong with path/domain")








