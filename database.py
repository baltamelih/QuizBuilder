import mysql.connector
import random

class Database():
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database="student"
                )
            self.mycursor = self.mydb.cursor()
            question="CREATE TABLE if not exists question (codeExam VARCHAR(10),id_question INT,question VARCHAR (200),answer1 VARCHAR (255),answer2 VARCHAR (255),answer3 VARCHAR (255),answer4 VARCHAR (255),answer5 VARCHAR (255),trueAnswer VARCHAR(100),point INT)"
            answer="CREATE TABLE if not exists answer (id_answer VARCHAR(10),soru_id INT(50),student_no VARCHAR (11),true_answer VARCHAR (255),student_answer VARCHAR(100),point INT(4))"
            sorgu_stdnt="CREATE TABLE if not exists students (id_no VARCHAR(255),name VARCHAR(255),surname VARCHAR (255),password VARCHAR (255))"
            sorgu_teacher = "CREATE TABLE if not exists teachers (id_no VARCHAR(255),name VARCHAR(255),surname VARCHAR (255),password VARCHAR (255),branch VARCHAR(255))"
            self.mycursor.execute(question)
            self.mycursor.execute(answer)
            self.mycursor.execute(sorgu_teacher)
            self.mycursor.execute(sorgu_stdnt)
        except:
            print("Hata Oluştu ...")

    def add_stdnt(self,name,surname,password):
        newno=random.randint(10000000000,99999999999)
        global newnos
        newnos=str(newno)
        self.mycursor.execute("SELECT id_no from students ")
        self.myresult = self.mycursor.fetchall()
        for x in self.myresult:
            if(x==newnos):
                newnos=str(random.randint(10000000000,99999999999))
            else:
                continue
        sorgu="INSERT INTO students (id_no,name,surname,password) values (%s,%s,%s,%s)"
        val=(newnos,name,surname,password)
        self.mycursor.execute(sorgu,val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "record inserted.")
    def renenow(self):
        return newnos
    def remove_stdnt(self,std_no):
        sql="DELETE FROM students WHERE id_no = %s"
        no=(std_no,)
        self.mycursor.execute(sql,no)
        self.mydb.commit()

    def add_teacher(self,name,surname,password,branch):
        global newnot
        newno = random.randint(10000000000, 99999999999)
        newnot=str(newno)
        self.mycursor.execute("SELECT id_no from teachers ")
        myresult = self.mycursor.fetchall()
        for x in myresult:
            if (x == newno):
                newno+=2
            else:
                continue
        sorgu = "INSERT INTO teachers (id_no,name,surname,password,branch) values (%s,%s,%s,%s,%s)"
        val = (str(newno), name, surname, password,branch)
        self.mycursor.execute(sorgu, val)
        self.mydb.commit()
    def retteacherno(self):
        return newnot
    def controllogin(self,who,idcontrol,passcontrol):
        try:
            if(who=="teachers"):

                val=(idcontrol,passcontrol)
                query="SELECT password from teachers WHERE id_no=%s AND password=%s"
                self.mycursor.execute(query,val)
                result=self.mycursor.fetchone()
                if result:
                    return True
                else:
                    return False
            elif(who=="students"):
                val = (idcontrol, passcontrol)
                query = "SELECT password from students WHERE id_no=%s AND password=%s"
                self.mycursor.execute(query, val)
                result = self.mycursor.fetchone()
                if result:
                    return True
                else:
                    return False
        except:
            print("Hata meydana geldi!.")

    def add_choice(self,codeExamentry,soru_id,student_no,trueAnswers,sel,point):
        sql = "INSERT INTO answer (id_answer,soru_id,student_no,true_answer,student_answer,point) values (%s,%s,%s,%s,%s,%s)"
        val=(codeExamentry,soru_id,student_no,trueAnswers,sel,point,)
        self.mycursor.execute(sql,val)
        self.mydb.commit()

    def buttonclick(self,codeExam,idquestion,question,ans1,ans2,ans3,ans4,ans5,truans,point):
        sql="INSERT INTO question (codeExam,idquestion,question,answer1,answer2,answer3,answer4,answer5,trueAnswer,point) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(codeExam,idquestion,question,ans1,ans2,ans3,ans4,ans5,truans,point)
        self.mycursor.execute(sql,val)
        self.mydb.commit()
    def fetch_question(self,x):

        query = "SELECT * FROM question WHERE codeExam = %s"
        self.mycursor.execute(query, (x,))
        y = self.mycursor.fetchall()
        return y
    def result(self,codeExam,no,name,surname,total):
        query="INSERT INTO result (code_exam,student_no,student_name,student_surname,total_point) values (%s,%s,%s,%s,%s)"
        val=(codeExam,no,name,surname,total)
        self.mycursor.execute(query,val)
        self.mydb.commit()
    def fetch_result_control(self,codeex,stdno):
        query="SELECT * FROM result WHERE code_exam=%s and student_no=%s"
        self.mycursor.execute(query,(codeex,stdno,))
        result=self.mycursor.fetchall()
        if(result):
            return True
        else:
            return False
    def getnamesurname(self,who,id_no):

        query=f"SELECT name,surname from {who} WHERE id_no=%s "
        self.mycursor.execute(query,(id_no,))
        y=self.mycursor.fetchall()
        return y
    def chng_pwd(self,who,id_no,newpwd):
        if who=="teachers":
            val = (newpwd, id_no)
            sorgu = "UPDATE teachers SET password=%s WHERE id_no=%s"
            self.mycursor.execute(sorgu, val)
            self.mydb.commit()
        elif(who=="students"):
            val = (newpwd, id_no)
            sorgu = "UPDATE students SET password=%s WHERE id_no=%s"
            self.mycursor.execute(sorgu, val)
            self.mydb.commit()
    def delete(self):
        query="DELETE from answer"
        self.mycursor.execute(query)
        self.mydb.commit()
    def fetch_result(self,codeEx):
        query4 = ("SELECT * From result WHERE code_exam=%s")
        self.mycursor.execute(query4,(codeEx,))
        myresult = self.mycursor.fetchall()
        return myresult
    def fetch_resultstd(self,stdno):
        query="SELECT * FROM result WHERE student_no=%s"
        self.mycursor.execute(query,(stdno,))
        result=self.mycursor.fetchall()
        return result
    def fetch_point(self,examNo,studentNo):
        query = ("SELECT point From answer WHERE true_answer = student_answer AND id_answer = %s AND student_no = %s")
        self.mycursor.execute(query, (examNo, studentNo,))
        myresult = self.mycursor.fetchall()
        return myresult


databes=Database()

databes.controllogin("teachers","33624165197","123")


