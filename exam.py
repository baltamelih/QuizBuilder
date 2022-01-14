import random
import string
import sys
import tkinter
from tkinter import*
import tkinter.messagebox
import re
import mysql.connector
from database import *
db = Database()

class Exam():
    def __init__(self):
        global p,windos
        p=-1
        windos = Tk()
        windos.title("QuizPROJECT")
        windos.geometry("800x300")

        label = Label(windos, text="Sınav Kodu")
        label.grid(row=0, column=0)

        global question, answer1, answer2, answer3, answer4, answer5, soru_ids, student_no, point, trueAnswers, selected
        global var
        p=-1
        var = tkinter.StringVar(windos)

        global label8,student_no
        with open("ogrenci_no.txt","r") as f:
            x=f.readline()
        student_no =x




        def sel():

            return var.get()

        def sistem(question,answer1,answer2,answer3,answer4,answer5):
            global R1,R2,R3,R4,R5,label1
            label1 = Label(windos, text=question,font=("Calibri", 14))
            label1.grid(row=2, column=1)

            R1 = Radiobutton(windos, text=answer1, variable=var, value=answer1, font=("Calibri", 10),
                         command=sel)
            R1.grid(row=3, column=0)

            R2 = Radiobutton(windos, text=answer2, variable=var, value=answer2,font=("Calibri", 10),
                             command=sel)
            R2.grid(row=4, column=0)

            R3 = Radiobutton(windos, text=answer3, variable=var, value=answer3,font=("Calibri", 10),
                             command=sel)
            R3.grid(row=5, column=0)

            R4 = Radiobutton(windos, text=answer4, variable=var, value=answer4,font=("Calibri", 10),
                             command=sel)
            R4.grid(row=6, column=0)

            R5 = Radiobutton(windos, text=answer5, variable=var, value=answer5,font=("Calibri", 10),
                             command=sel)
            R5.grid(row=7, column=0)

            label8 = Label(windos)
            label8.grid(row=8, column=0)

        def exam():

            if(db.fetch_result_control(codeExamEntry.get(),student_no)):
                tkinter.messagebox.showerror("Sınav Hatası","Sınava daha önce giriş yaptınız.")

            else:
                def point():
                    myresult = db.fetch_point(x, student_no)

                    totalpoint = 0
                    for i in myresult:
                        print(i)
                        totalpoint += int(i[0])
                    print(totalpoint)

                    myresult2 = db.getnamesurname("students", student_no)
                    for t, y in myresult2:
                        name = t
                        surname = y
                    try:
                        db.result(x, student_no, name, surname, totalpoint)
                    except:
                        tkinter.messagebox.showerror("HATA","Hatalı sınav kodu girdiniz",parent=windos)

                sayac = 0
                x = str(codeExamEntry.get())
                veri = []
                y = db.fetch_question(x)
                global p
                p += 1
                for i in y:
                    veri.append(i)
                    sayac = sayac + 1

                if p < sayac:
                    soru_ids = veri[p][1]
                    question = veri[p][2]
                    answer1 = veri[p][3]
                    answer2 = veri[p][4]
                    answer3 = veri[p][5]
                    answer4 = veri[p][6]
                    answer5 = veri[p][7]
                    trueAnswers = veri[p][8]
                    point = veri[p][9]
                    sistem(question, answer1, answer2, answer3, answer4, answer5)
                elif (p == sayac):
                    point()
                    windos.destroy()

                def choice():

                    db.add_choice(codeExamEntry.get(), soru_ids, student_no, trueAnswers, sel(), point)

                    print("Adding DATA")

                    def delete():
                        label1.config(text="")
                        R1.config(text="")
                        R2.config(text="")
                        R3.config(text="")
                        R4.config(text="")
                        R5.config(text="")
                        exam()

                    delete()

                try:
                    yazdir2 = Button(windos, command=choice, text="Cevapla")
                    yazdir2.grid(row=9, column=1)
                except:
                    print("Sınav bitmiştir")




        codeExamEntry = Entry(windos)
        codeExamEntry.grid(row=0, column=1)

        control = Button(windos, text="Sınavı göster")
        control.config(command=exam)
        control.grid(row=1, column=1)

        windos.mainloop()


