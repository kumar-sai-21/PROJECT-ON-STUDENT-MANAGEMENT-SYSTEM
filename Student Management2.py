#PROJECT ON STUDENT MANAGEMENT SYSTEM
#ADMIN ACCESS
#TEACHER'S ACCESS
#STUDENT'S ACCESS

#SAI KUMAR SATAPATHY(190310248)

import os , getpass , re

class Student:
    def __init__(self,id ,name, grade, m1, m2, m3, m4, m5):
        self.id=id
        self.name=name
        self.grade=grade
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def newstudent(self,id, name, grade, m1, m2, m3, m4, m5):
        try:

            #print("Enter Student Detail marks (Maths, Science,English,C,Python)")
            new=Student(id,name,grade,m1,m2,m3,m4,m5)
            ls.append(new)
            f = open("Student.txt", "a")
            f.write(id+'\t'+name+'\t'+grade+'\t'+m1+'\t'+m2+'\t'+m3+'\t'+m4+'\t'+m5 )
            f.write("\n")


        finally:
            f.close()
        #Student.backup(id,name)

    def display(self):
        print("")
        try:
            file=open("Student.txt",'r')
            for line in file:
                print(line)
        except FileExistsError:
            print("No FIle")
        finally:
            file.close()
    def search(self):
        n = input("enter the id to be searched")
        flag=1
        try:
            f=open("Student.txt","r")
            for sdata in f.readlines():
                sdata=sdata.strip()
                l=list(sdata.split('\t'))
                if(l[0]==n):
                    flag=1
                    print("Student Found ")
                    print("Id",l[0])
                    print("Name",l[1])
                    print("Class",l[2])
                    print("Maths",l[3])
                    print("English",l[4])
                    print("Science",l[5])
                    print("C",l[6])
                    print("Python",l[7])
                    return True
                else:
                    flag=0
        except FileExistsError:
            print("File not exit")
        finally:
            f.close()
        if(flag!=1):
            print("Not Found")
            return False

    def backup(id, name, password="password"):
        f=open("Login.txt","a")
        f.write(id+" "+name+" "+password+"\n")
        f.close()

    def update(self,id,m1,m2,m3,m4,m5):
        newfile = []
        try:
            obj = open("Student.txt", 'r')
            for l in obj.readlines():
                s = list(l.strip().split('\t'))
                if(s[0] == id):
                    s[3] = m1
                    s[4] = m2
                    s[5] = m3
                    s[6] = m4
                    s[7] = m5
                    newfile.append(s)
                else:
                    newfile.append(s)
        except FileExistsError:
            print("above file doesn't exists")
        finally:
            obj.close()
        try:
            obj = open("Student.txt", 'w')
            for l in newfile:
                obj.write("\t".join(l))
                obj.write("\n")
        except FileExistsError:
            print("Not Exit ")
        finally:
            obj.close()
            print("Updated Sucessfully")


    def remove(self,id):
        try:
            obj = open("Student.txt", 'r')
            newfile = []
            for l in obj.readlines():
                s = list(l.strip().split('\t'))
                if s[0] == id:
                    pass
                else:
                    newfile.append(s)
        except FileExistsError:
            print("above file doesn't exists")

        finally:
            obj.close()
        try:
            obj = open("Student.txt", 'w')
            for l in newfile:
                obj.write("\t".join(l))
                obj.write("\n")
        except FileExistsError:
            print("above file doesn't exists")

        finally:
            obj.close()
            print("\ndelete success")
class Teacher:
    def __init__(self,id,name,grade,subject):
        self.id=id
        self.name=name
        self.grade=grade
        self.subject=subject

    def newteacher(self,id,name,grade,subject):
        newt=Teacher(id,name,grade,subject)
        ls.append(newt)
        f = open("Teacher.txt", "a")
        f.write(id+ "\t" +name+ "\t" + grade + "\t" + subject)
        f.write("\n")
        f.close()

    def display(self):
        print("LIST OF TEACHERS ARE")
        try:
            file = open("Teacher.txt", 'r')
            for line in file:
                print(line)
        except FileExistsError:
            print("file doesn't exists")
        finally:
            file.close()

    def Search(self):
        id=input("Enter The Id of Teacher ")
        flag = 1
        try:
            file = open("Teacher.txt", 'r')
            for data in file.readlines():
                data = data.strip()
                l = list(data.split('\t'))
                if l[0] == id:
                    flag = 1
                    print("\nTEACHERS DDETAILS")
                    print("name:", l[1])
                    print("id:", l[0])
                    print("grade:", l[2])
                    print("sub:", l[3])
                else:
                    flag = 0
        except FileExistsError:
            print("above file doesn't exists")

        finally:
            file.close()
        if flag != 1:
            print("")

    def remove(self,id):
        newfile=[]
        try:
            obj=open("Teacher.txt",'r')
            for l in obj.readlines():
                s=list(l.strip().split("\t"))
                if(s[0]==id):
                    pass
                else:
                    newfile.append(s)
        except FileExistsError:
            print("Not Exit")
        finally:
            obj.close()
        try:
            obj=open("Teacher.txt",'w')
            for l in newfile:
                obj.write("\t ".join(l))
                obj.write("\n")
        except FileExistsError:
            print("Not Exit")
        finally:
            obj.close()
            print("Deleted")

ls=[]
child=Student('', '', '', '', '', '', '', '',)
teach=Teacher('', '', '', '')

#this is thw welcome screen
print("|------------------------------------------|--------------------------------------------|----------------------------------------------------|")
print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|WELCOME  TO  STUDENT  &  MANAGEMENT   PORTAL| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
print("|------------------------------------------|____________________________________________|----------------------------------------------------|")
username=input("ENTER YOUR USERNAME ")
pwd =input("ENTER YOUR PASSWORD ")


#this is for Admin Part He/she can access all the parameters
if (username == "admin" and pwd == 'password'):

    print('You are in!')
    while (1):
        print("|----------------------------|..................................|---------------------------|")
        print("|----------------------------| WELCOME    TO     ADMIN    PORTAL|---------------------------|")
        print("|----------------------------|__________________________________|---------------------------|")
        print("1.Enter New Student ")
        print("2.Display Student ")
        print("3.Search Student ")
        print(("4.Update marks"))
        print("5.Enter new Teacher ")
        print("6.Display Teacher ")
        print("7.Search Teacher ")
        print("8.Remove student")
        print("9.Remove Teacher")
        print("10.Exit ")
        ch = int(input("Enter your choice "))
        if (ch == 1):
            id = (input("Enter the Id of student "))
            name = input("Enter the student name ").upper()
            grade = (input("Enter the Class "))
            m1 = (input("Enter the Maths Marks "))
            m2 = (input("Enter the Science Marks "))
            m3 = (input("Enter the English Marks "))
            m4 = (input("Enter the C Programming Marks "))
            m5 = (input("Enter the Python Marks "))
            child.newstudent(id, name, grade, m1, m2, m3, m4, m5)
            Student.backup(id,name)

        elif (ch == 2):
            print(" The Student List \n")
            child.display()
            print("\n")
        elif (ch == 3):
            child.search()
        elif (ch == 4):
            id = input("enter the id to update student")
            m1, m2, m3, m4, m5 = input("enter the new marks").split(',')
            child.update(id, m1, m2, m3, m4, m5)
        elif (ch == 5):
            id = (input("Enter the Id of Teacher "))
            name = input("Enter the Teacher name ")
            grade = input("Enter the Grade ")
            subject = input("Enter the Subject ")
            teach.newteacher(id, name, grade, subject)

        elif (ch == 6):
            print(" The Teacher List \n")
            teach.display()
        elif (ch == 7):
            teach.Search()
        elif(ch==8):
            id=input("Enter the id")
            child.remove(id)
        elif (ch == 10):
            print("Thank You! ")
            exit(0)
        elif(ch==9):
            id=input("Enter the id of Teacher ")
            teach.remove(id)
#This is for Student's Access Part
elif(username == "student" and pwd =="student"):
    while(1):
        print("|----------------------------|..................................|----------------------------|")
        print("|----------------------------| WELCOME    TO    STUDENT   PORTAL|----------------------------|")
        print("|----------------------------|__________________________________|----------------------------|")
        print("1.New Student")           #This for new student who can change there default password '  password  '
        print("2.Get Details")           #here student will get  their details
        print("3.Log Out ")
        i = int(input("ENter your choice "))
        if(i == 1):
            print("Welcome to our Team ")
            passw = input("Enter Your New Password ::>")
            fl = 0
            while True:
                if (len(passw) < 8 and len(passw)>12):
                    fl = -1
                    break
                elif not re.search("[a-z]", passw):
                    fl = -1
                    break
                elif not re.search("[A-Z]", passw):
                    fl = -1
                    break
                elif not re.search("[0-9]", passw):
                    fl = -1
                    break
                elif not re.search("[_@$]", passw):
                    fl = -1
                    break
                elif re.search("\s", passw):
                    fl = -1
                    break
                else:
                    fl = 0
                    print(" This Is Valid Password")
                    n = input("Enter Your Id ")
                    if n.isdigit():
                        remove_pwd = re.compile(n)
                        name = input("Enter your name")
                        with open("Login.txt") as whole:
                            new = ' '
                            for line in whole:
                                if (remove_pwd.match(line)):
                                    x = input("Renter the new  Valid Password")
                                    if(x==passw):
                                        line = line.replace("password", x)
                                    else:
                                        print("Password does't Match")
                                        exit(0)
                                new += line
                        with open("Login.txt", "w") as doc:
                            doc.write(new)
                        print("Password updated")
                        break
            if fl == -1:
                print("Not a Valid Password")


        elif(i==2):
            n=input("Enter the id to search")
            code=input("Enter the password")
            p= open("Login.txt","r")
            for pdata in p.readlines():
                pdata=pdata.strip()
                l=list(pdata.split(' '))
                if(l[0]==n and l[2] == code):
                    child.search()
                    print("Thank You Visit Again")
                else:
                    print(" ")
                    exit(0)

        elif (i == 3):
            print("LOGOUT SUCCESSFULLY")

            exit(0)

#This is for Teacher Login Part
elif(username=="teacher" and pwd=="teacher"):
    while(1):
        print("-----------------------------------TEACHER'S PORTAL--------------------------------------------")
        print("|----------------------------|..................................|-----------------------------|")
        print("|----------------------------| WELCOME    TO    TEACHERS  PORTAL|-----------------------------|")
        print("|----------------------------|__________________________________|-----------------------------|")
        #print("1.Add New Student")
        print("1.Search Student")
        print("2.Update Marks")
        print("3.Log Out")
        ch=int(input("Enter what to do "))
        if(ch==1):
            child.search()
        elif(ch == 2):
            id = input("enter the id to update student")
            m1, m2, m3, m4, m5 = input("enter the new marks").split(',')
            child.update(id, m1, m2, m3, m4, m5)
        elif(ch==3):
            print("LOGOUT SUCCESSFULLY")
            exit(0)

else:
    print('WRONG CREDENTIAL')
    exit(0)
