import mysql.connector as connector

class DB_helper():

    def __init__(self,host,port,user,passwd,database):
        self.con = connector.connect(host=host,port=port,user=user,password=passwd,database=database)
        cur=self.con.cursor()
        # cur.execute('CREATE DATABASE My_DB')
        query="create table if not exists user1(user_Id int primary key, user_name varchar(255), user_input varchar(255), user_hist varchar(255), user_courses TEXT(40000))"
        print('Database Created')
        cur.execute(query)

    def insert_val(self,user_id,user_name,user_input,user_hist,user_courses):
        query="insert into user1(user_id,user_name,user_input,user_hist,user_courses) values({} ,'{}','{}','{}','{}')".format(user_id,user_name,user_input,user_hist,user_courses)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('data added')

    def fetch_input(self,user_id):
        query="select user_input from user1 where user_id={}".format(user_id)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            return row[0]

    def fetch(self,col_name):
        query="select * from user1"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            if col_name=='user_id':
                return row[0]
            elif col_name=='user_name':
                return row[1]
            elif col_name=='user_input':
                return row[2]
            elif col_name=='user_hist':
                return row[3]
            elif col_name=='user_courses':
                return row[4]
            else:
                return row

    def update(self,user_id):
        query="update user_courses from user1 where user_id = {}".format(user_id)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('data updated')

    def delete(self,user_id):
        query="delete from user1 where user_id = {}".format(user_id)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("data deleted")

if __name__=='__main__':
    db=DB_helper(host='localhost',port=3306,user='root',passwd='password123',database='My_DB')
    # db.insert_val(111,'sachin','js', 'javascript for beginners', "python for beginners,Machine learning in python")
    # print(db.fetch_input(111))