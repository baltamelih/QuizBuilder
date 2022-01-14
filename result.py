import functools
import random
import string
import tkinter
from database import *
from tkinter import*
from tkinter import ttk
class result():
    def __init__(self,who,code):
        db = Database()
        ws = Tk()
        ws.title('Result')
        ws.geometry('600x400')
        ws['bg'] = '#AC99F2'
        quiz_frame = Frame(ws)
        quiz_frame.pack()
        quiz_scroll = Scrollbar(quiz_frame)
        quiz_scroll.pack(side=RIGHT, fill=Y)

        quiz_scroll = Scrollbar(quiz_frame, orient='horizontal')
        quiz_scroll.pack(side=BOTTOM, fill=X)

        my_quiz = ttk.Treeview(quiz_frame, yscrollcommand=quiz_scroll.set, xscrollcommand=quiz_scroll.set)
        my_quiz.pack()

        quiz_scroll.config(command=my_quiz.yview)
        quiz_scroll.config(command=my_quiz.xview)
        my_quiz['columns'] = ('code_exam', 'student_no', 'student_name', 'student_surname', 'total_point')

        my_quiz.column("#0", width=0, stretch=NO)
        my_quiz.column("code_exam", anchor=CENTER, width=110)
        my_quiz.column("student_no", anchor=CENTER, width=110)
        my_quiz.column("student_name", anchor=CENTER, width=110)
        my_quiz.column("student_surname", anchor=CENTER, width=110)
        my_quiz.column("total_point", anchor=CENTER, width=110)

        my_quiz.heading("#0", text="", anchor=CENTER)
        my_quiz.heading("code_exam", text="Sınav Kodu", anchor=CENTER)
        my_quiz.heading("student_no", text="Öğrenci No", anchor=CENTER)
        my_quiz.heading("student_name", text="Ad", anchor=CENTER)
        my_quiz.heading("student_surname", text="Soyad", anchor=CENTER)
        my_quiz.heading("total_point", text="Toplam Puan", anchor=CENTER)
        if(who=="students"):
            myresult4=db.fetch_resultstd(code)
        elif(who=="teachers"):
            myresult4 = db.fetch_result(code)

        sayac = 0
        for a1, a2, a3, a4, a5 in myresult4:
            sayac += 1
            codeE = a1
            sNo = a2
            sName = a3
            sSurname = a4
            tPoint = a5
            my_quiz.insert(parent='', index='end', iid=sayac, text='',
                           values=(codeE, sNo, sName, sSurname, tPoint))


        mainloop()
