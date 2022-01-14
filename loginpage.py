import random
import string
from tkinter import *
from result import *
import database
from exam import *

db=database.Database()

def code():
    harfler= string.ascii_letters
    sonuc=''.join(random.sample(harfler,5))
    return sonuc

def questionAdd():
    global window
    window = Tk()
    window.title("QuizPROJECT")
    window.geometry("1200x500")
    def trueAnswer():
        if selected.get()==1:
            label9.config(text=ent3.get())
            return ent3.get()
        elif selected.get()==2:
            label9.config(text=ent4.get())
            return ent4.get()
        elif selected.get() == 3:
            label9.config(text=ent5.get())
            return ent5.get()
        elif selected.get() == 4:
            label9.config(text=ent6.get())
            return ent6.get()
        elif selected.get() == 5:
            label9.config(text=ent7.get())
            return ent7.get()
        else:
            print("Doğru cevabı işaretleyiniz...")



    Lb= Label(window)
    Lb.config(text="Code:", font=("Times New Roman",12))
    Lb.grid(row=0,column=0)


    global codeX
    codeX=code()
    codeExamLb = Label(window)
    codeExamLb.config(text=codeX,font=("Times New Roman",12))
    codeExamLb.grid(row=0,column=1)

    label2=Label(window)
    label2.config(text="Question",font=("Times New Roman",12))
    label2.grid(row=1,column=0)
    ent2=Entry(window,width=50,font=("Times New Roman",12))
    ent2.grid(row=1,column=1)

    selected=IntVar(window)

    rButton=Radiobutton(window,text="Answer 1:",value=1,variable=selected,command=trueAnswer)
    rButton.grid(row=2,column=0)
    ent3 = Entry(window,width=50, font=("Times New Roman", 12))
    ent3.grid(row=2,column=1)

    rButton2 = Radiobutton(window,text="Answer 2:",value=2,variable=selected,command=trueAnswer)
    rButton2.grid(row=3,column=0)
    ent4 = Entry(window,width=50, font=("Times New Roman", 12))
    ent4.grid(row=3,column=1)

    rButton3 = Radiobutton(window,text="Answer 3:",value=3,variable=selected,command=trueAnswer)
    rButton3.grid(row=4,column=0)
    ent5 = Entry(window,width=50, font=("Times New Roman", 12))
    ent5.grid(row=4,column=1)

    rButton4 = Radiobutton(window,text="Answer 4:",value=4,variable=selected,command=trueAnswer)
    rButton4.grid(row=5,column=0)
    ent6 = Entry(window,width=50, font=("Times New Roman", 12))
    ent6.grid(row=5,column=1)

    rButton5 = Radiobutton(window,text="Answer 5:",value=5,variable=selected,command=trueAnswer)
    rButton5.grid(row=6,column=0)
    ent7 = Entry(window,width=50, font=("Times New Roman", 12))
    ent7.grid(row=6,column=1)
    label8 = Label(window)
    label8.config(text="True Answer:",font=("Times New Roman",12))
    label8.grid(row=7,column=0)
    label9 = Label(window,width=50, font=("Times New Roman", 12))
    label9.grid(row=7,column=1)
    label10 = Label(window,text="Point:",width=70,font=("Times New Roman",12))
    label10.grid(row=8,column=0)
    entPoint = Entry(window,width=50,font=("Times New Roman",12))#eklendi
    entPoint.grid(row=8,column=1)#eklendi



    def buttonClick():
        true=trueAnswer()

        print(type(true))
        db.buttonclick(codeX,0,ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent6.get(),ent7.get(),true,entPoint.get())

        print("Adding DATA")
        label9.config(text="") #Butona basıldıktan sonra entry'lerin içinin sıfırlanması için
        entPoint.delete(0, 'end')#eklendi
        ent7.delete(0, 'end')
        ent6.delete(0, 'end')
        ent5.delete(0, 'end')
        ent4.delete(0, 'end')
        ent3.delete(0, 'end')
        ent2.delete(0, 'end')

    button= Button(window,text="Add",command=buttonClick)
    button.grid(row=9,column=1)




def mainscreen():
    global screen
    screen=Tk()
    screen.geometry("300x300")
    screen.resizable(False,False)
    screen.title("Giriş Seçenekleri")
    screen.config(background="black")
    mainlabel=Label(screen,text="Daha önce kayıt olmadıysanız \n'Kayıt OL' butonuna tıklayınız",width="300",height="2",bg="black",fg="white",font=("Calibri", 13))
    mainlabel.pack()

    logbtn=Button(screen,text="Giriş",height="2",width="30",command=chooselogin,font=("Calibri",10))
    logbtn.pack(pady="30")

    registerbtn=Button(screen,text="Kayıt OL",height="2",width="30",command=chooseregister,font=("Calibri",10))
    registerbtn.pack()

    text = "Created by Melih Balta- Muhammed Fatih Yılmaz"

    text = (' ' * 40) + text + (' ' * 40)

    marquee = Text(screen, height=1, width=40)
    marquee.place(y=250)

    i = 0

    def command(x, i):
        marquee.insert("1.1", x)
        if i == len(text):
            i = 0
        else:
            i = i + 1
        screen.after(100, lambda: command(text[i:i +50], i))

    command(text[i:i + 10], i)


    screen.mainloop()

def chooseregister():
    global screen2
    screen2=Toplevel(screen,bg="#f7d4d4")

    screen2.title("Kayıt Seçimi")
    screen2.geometry("300x300")
    label = Label(screen2, text="Seçim yapınız", width="300", height="2",bg="#f7d4d4",
                      font=("Calibri", 13))
    label.pack()
    teacherbtn=Button(screen2,text="Öğretmen Kayıt",height="2", width="30",command=teacher_register)
    stdntbtn = Button(screen2, text="Öğrenci Kayıt", height="2", width="30",command=stdnt_register)
    teacherbtn.pack(pady="30")
    stdntbtn.pack()
def stdnt_register():
    global screen1
    screen1=Toplevel(screen2,bg="#a5f7b7")
    screen1.title("Öğrenci Kayıt")
    screen1.geometry("300x400")
    global nameent,surnameent,lersa
    name=StringVar()
    surname=StringVar()
    password=StringVar()
    passwordcont=StringVar()
    Label(screen1,text="Lütfen bilgileri giriniz",bg="#a5f7b7").pack()
    Label(screen1, text="",bg="#a5f7b7").pack()
    Label(screen1,text="Adınızı Giriniz:",bg="#a5f7b7").pack()
    nameent=Entry(screen1,textvariable=name)
    nameent.pack()
    Label(screen1,text="Soyadınızı Giriniz:",bg="#a5f7b7").pack()
    surnameent=Entry(screen1,textvariable=surname)
    surnameent.pack()
    Label(screen1,text="Şifre Giriniz",bg="#a5f7b7").pack()
    global passent
    passent=Entry(screen1,textvariable=password,show="*")
    passent.pack()
    Label(screen1,text="Şifrenizi Tekrar Giriniz",bg="#a5f7b7").pack()
    global repassent
    repassent=Entry(screen1,textvariable=passwordcont,show="*")
    repassent.pack()
    Label(screen1, text="",bg="#a5f7b7").pack()
    submitbtn=Button(screen1,text="Kaydol",height="2", width="20",command=stdnt_registercontrol)
    submitbtn.pack()
    lersa = Label(screen1, text="", font={"Calibri", 8}, bg="#a5f7b7")
    lersa.pack()

def teacher_register():
    global screen3
    screen3 = Toplevel(screen2, bg="#a5f7b7")
    screen3.title("Öğretmen Kayıt")
    screen3.geometry("400x400")
    global nameentteach, surnameentteach,warnlabel
    name = StringVar()
    surname = StringVar()
    password = StringVar()
    branches=StringVar()
    passwordcont = StringVar()
    Label(screen3, text="Kayıt Ekranı(Öğretmen)", bg="#a5f7b7",font={"Calibri",8}).pack()
    Label(screen3, text="", bg="#a5f7b7").pack()
    Label(screen3, text="Adınızı Giriniz:", bg="#a5f7b7").pack()
    nameentteach = Entry(screen3, textvariable=name)
    nameentteach.pack()
    Label(screen3, text="Soyadınızı Giriniz:", bg="#a5f7b7").pack()
    surnameentteach = Entry(screen3, textvariable=surname)
    surnameentteach.pack()
    Label(screen3, text="Branşınızı Giriniz:", bg="#a5f7b7").pack()
    global branch
    branch=Entry(screen3,textvariable=branches)
    branch.pack()
    Label(screen3, text="Şifre Giriniz", bg="#a5f7b7").pack()
    global passentteach
    passentteach = Entry(screen3, textvariable=password, show="*")
    passentteach.pack()
    Label(screen3, text="Şifrenizi Tekrar Giriniz", bg="#a5f7b7").pack()
    global repassentteach
    repassentteach = Entry(screen3, textvariable=passwordcont, show="*")
    repassentteach.pack()
    Label(screen3, text="", bg="#a5f7b7").pack()
    submitbtn = Button(screen3, text="Kaydol", height="2", width="20", command=teacher_registercontrol)
    submitbtn.pack()
    warnlabel = Label(screen3, text="", font={"Calibri", 8}, bg="#a5f7b7")
    warnlabel.pack()


def stdnt_registercontrol():
    warning = StringVar()
    bg="red"
    if(passent.get()==repassent.get()):
        name=str(nameent.get())
        surname=str(surnameent.get())
        password=str(passent.get())
        if(name=="" or surname==""):
            warning="Ad Soyad Boş Bırakılamaz"
            lersa.config(text=warning,bg=bg)
        else:
            db.add_stdnt(name, surname, password)
            text = db.renenow()
            warning=f"Kayıt Başarılı \n ID = {text} \nLütfen ID nizi not alınız"
            bg = "aqua"
            lersa.config(text=warning,bg=bg)


    else:
        warning="Şifreler uyuşmuyor"
        lersa.config(text=warning,bg=bg)


def teacher_registercontrol():
    warning = StringVar()
    bg = "red"
    if ( passentteach.get()==repassentteach.get()):
        name = str(nameentteach.get())
        surname = str(surnameentteach.get())
        password = str(passentteach.get())
        tchr_branch=str(branch.get())
        if (name == "" or surname == "" or tchr_branch=="" or password==""):
            warning = "Ad,Soyad,Branş ve Şifre Boş Bırakılamaz"
            warnlabel.config(text=warning,bg="red")
        else:
            db.add_teacher(name,surname,password,tchr_branch)
            text = db.retteacherno()
            warning = f"Kayıt Başarılı \n ID = {text} \nLütfen ID nizi not alınız"
            bg = "aqua"
            warnlabel.config(text=warning, bg=bg)
    else:
        warning = "Şifreler uyuşmuyor"
        warnlabel.config(text=warning, bg="red")


def chooselogin():
    global screen4
    screen4 = Toplevel(screen, bg="#acafe2")
    screen4.title("Giriş Seçimi")
    screen4.geometry("300x300")

    label = Label(screen4, text="Seçim yapınız", width="300", height="2", bg="#acafe2",
                  font=("Calibri", 13))
    label.pack()
    teacherbtn = Button(screen4, text="Öğretmen Giriş", height="2", width="30",command=loginteacher)
    stdntbtn = Button(screen4, text="Öğrenci Giriş", height="2", width="30",command=loginstudent)
    teacherbtn.pack(pady="30")
    stdntbtn.pack()

def loginstudent():
    global screen5,ident,passentrystd,warnloginstd
    stdid=StringVar()
    stdpass=StringVar()
    screen5=Toplevel(screen4,bg="#CCF392")
    screen5.title("Öğrenci Giriş")
    screen5.geometry("300x300")
    Label(screen5,text="Giriş Ekranı",width="300",height="2",bg="#CCF392",font=("Calibri", 14)).pack()
    Label(screen5, text="ID Giriniz:", bg="#CCF392", font=("Calibri", 10)).pack()
    ident=Entry(screen5,textvariable=stdid)
    ident.pack()
    Label(screen5, text="", bg="#CCF392").pack()
    Label(screen5, text="Şifrenizi Giriniz:", bg="#CCF392", font=("Calibri", 10)).pack()
    passentrystd=Entry(screen5,textvariable=stdpass,show="*")
    passentrystd.pack()
    stdloginbtn=Button(screen5,text="Giriş", height="2", width="10",command=logincontrol)
    stdloginbtn.pack(pady=20)
    warnloginstd=Label(screen5,text="",font={"Calibri", 10},bg="#CCF392")
    warnloginstd.pack()

def loginteacher():
    global screen6, identeacher, passentryteacher,warnlogin
    stdid = StringVar()
    stdpass = StringVar()
    screen6 = Toplevel(screen4, bg="#CCF392")
    screen6.title("Öğretmen Giriş")
    screen6.geometry("300x300")
    Label(screen6, text="Giriş Ekranı", width="300", height="2", bg="#CCF392", font=("Calibri", 14)).pack()
    Label(screen6, text="ID Giriniz:", bg="#CCF392", font=("Calibri", 10)).pack()
    identeacher = Entry(screen6, textvariable=stdid)
    identeacher.pack()
    Label(screen6, text="", bg="#CCF392").pack()
    Label(screen6, text="Şifrenizi Giriniz:", bg="#CCF392", font=("Calibri", 10)).pack()
    passentryteacher = Entry(screen6, textvariable=stdpass,show="*")
    passentryteacher.pack()
    stdloginbtn = Button(screen6, text="Giriş", height="2", width="10", command=logincontrolteacher)
    stdloginbtn.pack(pady=20)
    warnlogin=Label(screen6,text="", font={"Calibri", 10}, bg="#CCF392")
    warnlogin.pack()

def interface_student(y):
    global interface_s
    interface_s=Toplevel(screen4,bg="#FD7704")
    interface_s.title("Öğrenci Arayüzü")
    interface_s.geometry("350x350")
    Label(interface_s, text="Öğrenci Arayüzü", width="300", height="2", bg="#FD7704", font=("Calibri", 14)).pack()
    config = Label(interface_s, text=y, bg="#FD7704", font=("Calibri", 14, "bold"))
    config.pack()
    showexam= Button(interface_s, text="Sınava Gir", height="2", width="20",command=Exam)
    learnresult= Button(interface_s, text="Not Bilgisi", height="2", width="20",command=show_std_result)
    changepass=Button(interface_s,text="Şifre Değiştir", height="2", width="20",command=changepasstd)
    showexam.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    learnresult.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    changepass.place(relx = 0.5, rely = 0.7, anchor = CENTER)
def show_std_result():
    result("students",ident.get())
def changepasstd():
    global changewindowstd
    changewindowstd=Toplevel(interface_s)
    global stdID,passwordstc
    ıd=StringVar(changewindowstd)
    newpass=StringVar(changewindowstd)
    changewindowstd.title("Şifre Değiştir")
    changewindowstd.geometry("300x300")
    changewindowstd.resizable(False,False)
    Label(changewindowstd, text="ID'nizi girin", width="20", height="2", font=("Calibri", 10)).pack()
    stdID=Entry(changewindowstd,textvariable=ıd)
    stdID.pack()
    Label(changewindowstd, text="Yeni şifrenizi girin", width="20", height="2", font=("Calibri", 10)).pack()
    passwordstc=Entry(changewindowstd,textvariable=newpass)
    passwordstc.pack()
    commitbtn = Button(changewindowstd, text="Şifre değiştir", height="2", width="20", command=passchangecontrolstd)
    commitbtn.pack()
def passchangecontrolstd():
    if ident.get()==stdID.get():

        if (stdID.get() == "" or passwordstc.get() == ""):
            tkinter.messagebox.showerror("HATA", "ID veya Şifre Boş Bırakılamaz",parent=changewindowstd)
        else:
            db.chng_pwd("students",stdID.get(),passwordstc.get())
            tkinter.messagebox.showinfo("BAŞARILI","Şifreniz değiştirildi",parent=changewindowstd)
            interface_s.destroy()
    else:
        tkinter.messagebox.showerror("HATA", "Girdiğiniz hesabın IDsi uyuşmuyor",parent=changewindowstd)


def addsoru():
    questionAdd()
    mainloop()
def interface_teacher(y):
    global interface_t
    interface_t=Toplevel(screen4,bg="#fd6d5a")
    interface_t.title("Öğretmen Arayüzü")
    interface_t.geometry("350x350")
    Label(interface_t, text="Öğretmen Arayüzü", width="300", height="2", bg="#fd6d5a", font=("Calibri", 14)).pack()
    config=Label(interface_t,text=y,bg="#fd6d5a", font=("Calibri", 14,"bold"))
    config.pack()
    addquestion= Button(interface_t, text="Sınav Oluştur", height="2", width="20",command=addsoru)
    fetchresult=Button(interface_t,text="Öğrenci Notları Göster", height="2", width="20",command=show_result)
    changepass=Button(interface_t,text="Şifre Değiştir", height="2", width="20",command=changepasteacher)
    addquestion.place(relx = 0.5, rely = 0.3, anchor = CENTER)
    fetchresult.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    changepass.place(relx = 0.5, rely = 0.7, anchor = CENTER)


def changepasteacher():
    global changewindow
    changewindow=Toplevel(interface_t)
    changewindow.config(bg="#0cc7a8")
    global teacherID,passwordc
    ıd=StringVar(changewindow)
    newpass=StringVar(changewindow)
    changewindow.title("Şifre Değiştir")
    changewindow.geometry("300x300")
    changewindow.resizable(False,False)
    Label(changewindow, text="ID'nizi girin", width="20", height="2", font=("Calibri", 12),bg="#0cc7a8").pack(pady=5)
    teacherID=Entry(changewindow,textvariable=ıd)
    teacherID.pack()
    Label(changewindow, text="Yeni şifrenizi girin",width="20", height="2", font=("Calibri", 12),bg="#0cc7a8").pack(pady=5)
    passwordc=Entry(changewindow,textvariable=newpass)
    passwordc.pack()
    commitbtn = Button(changewindow, text="Şifre Değiştir", height="2", width="20", command=passchangecontroltch)
    commitbtn.pack(pady=10)


def passchangecontroltch():
    if identeacher.get()==teacherID.get():

        if (teacherID.get() == "" or passwordc.get() == ""):
            tkinter.messagebox.showerror("HATA", "ID veya Şifre Boş Bırakılamaz",parent=changewindow)
        else:
            db.chng_pwd("teachers",teacherID.get(),passwordc.get())
            tkinter.messagebox.showinfo("BAŞARILI","Şifreniz değiştirildi",parent=changewindow)
            interface_t.destroy()
    else:
        tkinter.messagebox.showerror("HATA", "Girdiğiniz hesabın IDsi uyuşmuyor",parent=changewindow)

def resulting():
    if(db.fetch_result(examCode.get())):
        result("teachers", examCode.get())
    else:
        tkinter.messagebox.showerror("HATA","Böyle bir sınav kodu bulunmamaktadır",parent=resultwindow)

def show_result():
    global resultwindow
    resultwindow = Toplevel(interface_t)
    global examCode
    examCodex = StringVar(resultwindow)
    resultwindow.title("Öğrenci Notları Görüntüleme")
    resultwindow.config(bg="grey")
    resultwindow.geometry("400x400")
    resultwindow.resizable(False, False)
    Label(resultwindow, text="Sınav Kodunu Giriniz", width="20", height="2", font=("Calibri", 14)).pack()
    examCode = Entry(resultwindow, textvariable=examCodex)
    examCode.pack(pady=10)
    commitbtn = Button(resultwindow, text="Öğrenci Notları Göster", height="2", width="20",
                       command=resulting)
    commitbtn.pack(pady=5)

def logincontrolteacher():
    passcontrol = passentryteacher.get()
    idcontrol = identeacher.get()
    warn = StringVar()
    bg = "red"
    if (passcontrol == "" or idcontrol == ""):
        warn = "Değer Girmediniz"
        warnlogin.config(text=warn, bg=bg)
    else:
        if (db.controllogin("teachers",idcontrol, passcontrol)):
            warn = "Giriş Başarılı"
            bg = "green"
            warnlogin.config(text=warn,bg=bg)
            y=db.getnamesurname("teachers",idcontrol)
            interface_teacher(y)



        else:
            warn = "Öğretmen ID veya Şifre yanlış !"
            bg = "red"
            warnlogin.config(text=warn, bg=bg)


def logincontrol():
    passcontrol=passentrystd.get()
    idcontrol=ident.get()
    warn=StringVar()
    bg="red"
    if(passcontrol=="" or idcontrol==""):
        warn = "Değer Girmediniz"
        warnloginstd.config(text=warn,bg=bg)
    else:
        if(db.controllogin("students",idcontrol,passcontrol)):
            warn="Giriş Başarılı"
            bg="green"
            warnloginstd.config(text=warn, bg=bg)

            with open("ogrenci_no.txt","w") as file:
                file.write(idcontrol)
            x=db.getnamesurname("students",idcontrol)
            interface_student(x)


        else:
            warn="Öğrenci ID veya Şifre yanlış !"
            bg="red"
            warnloginstd.config(text=warn, bg=bg)


mainscreen()