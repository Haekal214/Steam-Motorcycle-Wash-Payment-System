from pathlib import Path
from tkinter import *
import tkinter as tk
import csv
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Figma\LOGIN\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def menu_home():
    jenisMotor = []
    homepage = Tk()
    homepage.title("PROGRAM KASIR")
    homepage.geometry("720x480")
    homepage.configure(bg="#FFFFFF")
    global combo_image, combo1

    def inputdata():
        platM = inputP.get()
        namaM = inputP2.get()
        global jenisM
        if len(jenisMotor) != 0:
            for i in range(len(jenisMotor) - 1, len(jenisMotor)):
                jenisM = jenisMotor[i]
            if platM == "" or namaM == "" or jenisM == "":
                messagebox.showerror("WARNING", "Ada data yang belum diinput!")
            else:
                if jenisM == 'Motor Kecil':
                    with open('databaseM.csv', 'a', newline='') as file:
                        fieldnames = ['PlatM', 'NamaM', 'jenisM', 'Harga']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writerow({'PlatM': platM, 'NamaM': namaM, 'jenisM': jenisM, 'Harga': 15000})
                elif jenisM == 'Motor Besar':
                    with open('databaseM.csv', 'a', newline='') as file:
                        fieldnames = ['PlatM', 'NamaM', 'jenisM', 'Harga']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writerow({'PlatM': platM, 'NamaM': namaM, 'jenisM': jenisM, 'Harga': 18000})
                elif jenisM == 'Motor Trail':
                    with open('databaseM.csv', 'a', newline='') as file:
                        fieldnames = ['PlatM', 'NamaM', 'jenisM', 'Harga']
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writerow({'PlatM': platM, 'NamaM': namaM, 'jenisM': jenisM, 'Harga': 22000})
                jenisMotor.pop(0)
                global combo_image, combo1
                combo1.destroy()
                combo_image = PhotoImage(file=relative_to_assets("combobox.png"))
                combo1 = Button(framecombo, image=combo_image, borderwidth=0, highlightthickness=0, command=comboboxD,relief="flat")
                combo1.place(x=0.0, y=0.0, width=209.0, height=40.0)
                inputP.delete(0, END)
                inputP2.delete(0, END)
                messagebox.showinfo("Information", "Data berhasil diinput!")
        else:
            messagebox.showerror("WARNING", "Ada data yang belum diinput!")

    def comboboxD():
        global image_image_2, comboTimage, comboGimage, comboKimage, frameisiC
        frameisiC = Frame(homepage, width=143, height=111, bg="white", highlightthickness=1,highlightbackground="black")
        frameisiC.place(x=318.0, y=302.0)
        comboTimage = PhotoImage(file=relative_to_assets("combotrail.png"))
        comboT = Button(frameisiC, image=comboTimage, borderwidth=0, highlightthickness=0, command=opsicombo3,relief="flat")
        comboT.place(x=0.0, y=72.0, width=140.0, height=37.0)
        comboGimage = PhotoImage(file=relative_to_assets("combogede.png"))
        comboG = Button(frameisiC, image=comboGimage, borderwidth=0, highlightthickness=0, command=opsicombo2,relief="flat")
        comboG.place(x=0.0, y=40.0, width=140.0, height=31.0)
        comboKimage = PhotoImage(file=relative_to_assets("combokecil.png"))
        comboK = Button(frameisiC, image=comboKimage, borderwidth=0, highlightthickness=0, command=opsicombo1,relief="flat")
        comboK.place(x=0.0, y=0.0, width=140.0, height=39.0)

    def opsicombo1():
        global combo_image, combo1
        frameisiC.destroy()
        combo1.destroy()
        combo_image = PhotoImage(file=relative_to_assets("Motor_Kecil.png"))
        combo1 = Button(framecombo, image=combo_image, borderwidth=0, highlightthickness=0, command=comboboxD,relief="flat")
        combo1.place(x=0.0, y=0.0, width=209.0, height=40.0)
        jenisMotor.append("Motor Kecil")

    def opsicombo2():
        global combo_image, combo1
        frameisiC.destroy()
        combo1.destroy()
        combo_image = PhotoImage(file=relative_to_assets("Motor_Besar.png"))
        combo1 = Button(framecombo, image=combo_image, borderwidth=0, highlightthickness=0, command=comboboxD,relief="flat")
        combo1.place(x=0.0, y=0.0, width=209.0, height=40.0)
        jenisMotor.append("Motor Besar")

    def opsicombo3():
        global combo_image, combo1
        frameisiC.destroy()
        combo1.destroy()
        combo_image = PhotoImage(file=relative_to_assets("Motor_Trail.png"))
        combo1 = Button(framecombo, image=combo_image, borderwidth=0, highlightthickness=0, command=comboboxD,relief="flat")
        combo1.place(x=0.0, y=0.0, width=209.0, height=40.0)
        jenisMotor.append("Motor Trail")

    def exitMenu():
        msg_box = tk.messagebox.askquestion('Keluar Aplikasi', 'Apakah ingin keluar dari aplikasi?',icon='warning')
        if msg_box == 'yes':
            homepage.destroy()
        else:
            pass

    def homeMenu():
        global textTM
        try:
            textTM2.destroy()
            frameB.destroy()
            frameBD.destroy()
            textTM = Label(frameM, text="MENU UTAMA")
            textTM.config(font=("Open Sans", 24, 'bold'), fg="white", bg="#6E8C91")
            textTM.place(x=410.0, y=14.0)
        except:
            pass

    def bayarMenu():
        global textTM2
        data = []
        def bayar():
            total_tmp = []
            total = 0
            temp1 = open('databaseM.csv', 'r')
            harga = listboks.curselection()
            valhps = list(harga)
            for b in range(len(valhps), 0, -1):
                hps = valhps[b - 1]
                total_tmp = data[hps]
                total += int(total_tmp["harga"])
            msg_box = tk.messagebox.askquestion('PEMBAYARAN', total)
            temp1.close()
            if msg_box == 'yes':
                for b in range(len(valhps), 0, -1):
                    data.pop(hps)
                with open('databaseM.csv', 'w', newline='') as temp2:
                    kolom = ['plat', 'nama', 'jenis', 'harga']
                    databaru = csv.DictWriter(temp2, kolom)
                    databaru.writeheader()
                    for jumlah in data:
                        databaru.writerow(jumlah)
                temp2.close()
                for k in harga[::-1]:
                    listboks.delete(k)
            else:
                pass

        def hapusdata():
            msg_box = tk.messagebox.askquestion('HAPUS DATA', 'Apakah ingin menghapus data?', icon='warning')
            if msg_box == 'yes':
                temp1 = open('databaseM.csv', 'r')
                nilaihps = listboks.curselection()
                valhps = list(nilaihps)
                temp1.readlines()
                for b in range(len(valhps), 0,-1):
                    hps = valhps[b-1]
                    data.pop(hps)
                temp1.close()
                with open('databaseM.csv', 'w', newline = '') as temp2 :
                    kolom = ['plat','nama','jenis','harga']
                    databaru = csv.DictWriter(temp2, kolom)
                    databaru.writeheader()

                    for jumlah in data:
                        databaru.writerow(jumlah)
                temp2.close()
                for k in nilaihps[::-1]:
                    listboks.delete(k)
            else:
                pass

        textTM.destroy()
        textTM2 = Label(frameM, text="MENU BAYAR")
        textTM2.config(font=("Open Sans", 24, 'bold'), fg="white", bg="#6E8C91")
        textTM2.place(x=410.0, y=14.0)
        #frame bawah bayar
        def isitabel():
            global listboks, frameB, frameBD, butbayarIM, buthapusIM
            frameB = Frame(homepage, width=720, height=410, bg="white")
            frameB.place(x=0, y=70)
            frameBD = Frame(frameB, width=430, height=348, bg="white", highlightthickness=1, highlightbackground="black")
            frameBD.place(x=40.0, y=30)
            #scrollbar
            scrolly = Scrollbar(frameBD, orient=VERTICAL)
            scrolly.pack(side=RIGHT, fill=BOTH)
            scrollx = Scrollbar(frameBD, orient=HORIZONTAL)
            scrollx.pack(side=BOTTOM, fill=BOTH)
            #listboks
            listboks = Listbox(frameBD, selectmode=MULTIPLE, yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, width=60, height=20, font="Arial 10")
            listboks.pack(expand=YES, fill=BOTH, side=LEFT)
            # scrollbar config
            scrolly.config(command=listboks.yview)
            scrollx.config(command=listboks.xview)
            #data
            with open('databaseM.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    data.append(row)
                for x in range(0, len(data)):
                    listboks.insert(END, data[x])
                    listboks.itemconfig(x, bg="white")
            # tombol
            butbayarIM = PhotoImage(file=relative_to_assets("tombolbayar.png"))
            butbayar = Button(frameB, image=butbayarIM, borderwidth=0, highlightthickness=0, command=bayar,relief="flat")
            butbayar.place(x=557.0, y=130.0, width=130.0, height=39.0)

            buthapusIM = PhotoImage(file=relative_to_assets("hapus.png"))
            button_2 = Button(frameB, image=buthapusIM, borderwidth=0, highlightthickness=0, command=hapusdata,relief="flat")
            button_2.place(x=557.0, y=200.0, width=130.0, height=39.0)
        try:
            frameB.destroy()
            isitabel()
        except:
            isitabel()

    canvasH = Canvas(homepage, bg="#FFFFFF", height=480, width=720, bd=0, highlightthickness=0, relief="ridge")
    canvasH.place(x=0, y=0)
    # entry1
    inputP_image = PhotoImage(file=relative_to_assets("home_entry1.png"))
    inputP_BG = canvasH.create_image(206.5, 169.0, image=inputP_image)
    inputP = Entry(bd=0, bg="#BEDCE1", fg="#000716", highlightthickness=0, font=("Arial 12"))
    inputP.place(x=114.0, y=150.0, width=185.0, height=38.0)
    # entry2
    inputP_image2 = PhotoImage(file=relative_to_assets("home_entry1.png"))
    inputP_BG2 = canvasH.create_image(208.5, 241.0, image=inputP_image2)
    inputP2 = Entry(bd=0, bg="#BEDCE1", fg="#000716", highlightthickness=0, font=("Arial 12"))
    inputP2.place(x=116.0, y=222.0, width=185.0, height=38.0)
    # combobox
    framecombo = Frame(homepage, width=209.0, height=40, bg="white")
    framecombo.place(x=104.0, y=301.0)
    combo_image = PhotoImage(file=relative_to_assets("combobox.png"))
    combo1 = Button(framecombo, image=combo_image, borderwidth=0, highlightthickness=0, command=comboboxD,relief="flat")
    combo1.place(x=0.0, y=0.0, width=209.0, height=40.0)
    # button input data
    dataimage = PhotoImage(file=relative_to_assets("input_data.png"))
    dataButton = Button(image=dataimage, borderwidth=0, highlightthickness=0, command=inputdata, relief="flat")
    dataButton.place(x=449.0, y=218.0, width=186.0, height=45.0)
    # Text di home
    canvasH.create_text(109.0, 124.0, anchor="nw", text="Plat Motor", fill="#000000",font=("OpenSansRoman Bold", 14 * -1))
    canvasH.create_text(109.0, 198.0, anchor="nw", text="Nama Motor", fill="#000000",font=("OpenSansRoman Bold", 14 * -1))
    canvasH.create_text(109.0, 274.0, anchor="nw", text="Jenis Motor", fill="#000000",font=("OpenSansRoman Bold", 14 * -1))
    # tempat menu
    frameM = Frame(homepage, width=720, height=70, bg="#6E8C91")
    frameM.place(x=0,y=0)
    global textTM, garis
    textTM = Label(frameM, text="MENU UTAMA")
    textTM.config(font=("Open Sans", 24,'bold'), fg="white", bg="#6E8C91")
    textTM.place(x=410.0, y=14.0)
    garisIM = PhotoImage(file=relative_to_assets("garis.png"))
    garis = Label(frameM, image=garisIM, bg="#6E8C91")
    garis.place(x=315.0, y=6.0)
    # tombol exit
    exitBut = PhotoImage(file=relative_to_assets("exit.png"))
    exitB = Button(image=exitBut, borderwidth=0, highlightthickness=0, command=exitMenu,relief="flat")
    exitB.place(x=22.0, y=8.0, width=55.0, height=55.0)
    # tombol home
    homeBut = PhotoImage(file=relative_to_assets("home.png"))
    homeB = Button(image=homeBut, borderwidth=0, highlightthickness=0, command=homeMenu, relief="flat")
    homeB.place(x=109.0, y=8.0, width=55.0, height=55.0)
    # tombol bayar
    bayarBut = PhotoImage(file=relative_to_assets("bayar.png"))
    bayarB = Button(image=bayarBut, borderwidth=0, highlightthickness=0, command=bayarMenu, relief="flat")
    bayarB.place(x=196.0, y=8.0, width=55.0, height=55.0)
    #setting page home
    homepage.resizable(False, False)
    homepage.mainloop()

username = ['user1', 'user2']
password = ['123', '456']
login = Tk()
login.title("ADMIN LOGIN")
login.geometry("266x367")
login.configure(bg="#FFFFFF")

def checkpass():
    nama = nameI.get()
    passwordD = passI.get()
    if nama in username or passwordD in password:
        if nama == "" or passwordD == "":
            messagebox.showerror("WARNING", "Username atau Password belum diinput!")
        else:
            ceknama = username.index(nama)
            if nama == username[ceknama] and passwordD == password[ceknama]:
                login.destroy()
                menu_home()
            else:
                messagebox.showerror("WARNING", "Username atau Password salah!")
    else:
        messagebox.showerror("WARNING", "Username atau Password salah!")

canvasL = Canvas(login, bg="#FFFFFF", height=367, width=266, bd=0, highlightthickness=0, relief="ridge")
canvasL.place(x=0, y=0)
# Entry 1 username
nameIM = PhotoImage(file=relative_to_assets("input_login.png"))
nameBG = canvasL.create_image(130.0, 131.0, image=nameIM)
nameI = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
nameI.place(x=57.0, y=116.0, width=146.0, height=30.0)
# Entry 2 password
passIM = PhotoImage(file=relative_to_assets("input_login.png"))
passBG = canvasL.create_image(130.0, 213.0, image=passIM)
passI = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, show ='*')
passI.place(x=57.0, y=198.0, width=146.0, height=30.0)
#Teks
canvasL.create_text(45.0, 170.0, anchor="nw", text="Password", fill="#000000", font=("OpenSansRoman Bold", 14 * -1))
canvasL.create_text(21.0, 32.0, anchor="nw", text="ADMIN LOGIN", fill="#000000", font=("OpenSansRoman Bold", 32 * -1))
canvasL.create_text(45.0, 90.0, anchor="nw", text="Username", fill="#000000", font=("OpenSansRoman Bold", 14 * -1))
# Button login
loginIM = PhotoImage(file=relative_to_assets("login.png"))
loginI = Button(image=loginIM, borderwidth=0, highlightthickness=0, command=checkpass, relief="flat")
loginI.place(x=52.0, y=270.0, width=163.0, height=64.0)
login.resizable(False, False)
#START PROGRAM
login.mainloop()