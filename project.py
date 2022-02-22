import mysql.connector as driver
import sys
           
con=driver.connect(host='localhost',user='root',passwd='123456',charset=
,database='mydata')
if con.is_connected():
    cur=con.cursor()
    cur.execute(create database if not exists mydata)
    print()
    con.close()

con=driver.connect(host='localhost',user='root',passwd='123456',charset=
,database='mydata')
if con.is_connected():   
     cur=con.cursor()
     cur.execute(create table if not exists login (first name varchar(300),second name varchar(400), phone int(10),course feddback varchar(200), staff feddback varchar(300),transport varchar(200),canteen feddback varchar(30),allocationvarchar(30) )


def login(): 
         while 1:
            print("LOGIN PAGE")
            print("")

            print("1. Login as student")
            print('2. Login as teacher ')
            print('3. QUIT')
            user_option=input("option:")
            if user_option =="1"
                student_login()
            if user_option =="2"
                teacher()
            if user_option=="3"
                break


def student_login():
   
    print("")
    print( "student LOGIN")
    print("")
    username = input("username :")
    password = input("PASSWORD :")
    if username== "21cs116"
        if password  =="password"
            menu()
    else:
        print("wrong credentials")




def teacher():
   
    print("")
    print( "TEACHER  LOGIN")
    print("")
    username = input("username :")
    password = input("PASSWORD :")
    if username== "9840234544"
        if password  =="password"
            display()
    else:
        print("wrong credentials")


def menu():

    print("ENTER THE CHOICE ACCORDING TO YOU WANT TO proceed:")
    print("1.STUDENT FEEDBACK")
    print("2.MAIN MENU")
    choice=int(input("ENTER THE CHOICE (1-2) :")) 
    if choice=='1':
      d=input("Enter STUDENT NAME FIRST NAME  : ")
      n=input("Enter STUDENT NAME SECOND NAME  : ")
      a=int(input("ENTER THE PHONE NUMBER:"))
      v=input("ENTER THE FEEBACK OF COURSE:")
      g=input("ENTER THE FEEDBACK OF THE STAFF:")
      h=input("ENTER THE FEEDBACK OF THE COLLEGE TRANSPORT:")
      i=input("ENTER THE FEEDBACK OF THE COLLEGE CANTEEN:")
      query1="INSERT INTO login(first name,second name,phone,course feddback,staff feedback,transport,canteen feedback)VALUES('{}','{}',{},'{}','{}','{}','{}')".format(d,n,a,v,g,h,i)
      cur.execute(query1)
      con.commit()
      print("feedback completed")
      con.close()
     else:
        print("not connected")

     elif choice=='2':
         login()



def display():
    print("ENTER THE CHOICE ACCORDING TO YOU WANT TO proceed:")
    print("1 FEEDBACK review")
    print("2.MAIN MENU")
    choice=int(input("ENTER THE CHOICE (1-2) :"))
    if choice=='1':
        query1="select * from login"
        cur.execute(query1)
        rec=cur.fetchall()
        count=cur.rowcount

        for i in rec:
            print(i)
        
     else:
        print("Error : Database Connection is not success" )
    
    

    elif choice=='2':
        login()

login()




