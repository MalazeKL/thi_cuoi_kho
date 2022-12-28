from tkinter import *
import json

win = Tk()
win.title("Login")
win.geometry("545x545")
accounts = []
with open("sample.json") as outfile:
    accounts.append(json.load(outfile))
def window_login_successful(i):
    def des():
        login_successfulcessful.destroy()
    login_successfulcessful = Tk()
    login_successfulcessful.title("Login Successful")
    login_successfulcessful.geometry("545x545")
    title = Label(login_successfulcessful, text = "Your Infomation", font = ("Arial", 25)).place(x = 200, y = 40)

    lab_name = Label(login_successfulcessful, text = "Your name: ", font = ("Arial")).place(x = 20, y = 120)
    lab_user = Label(login_successfulcessful, text = "User name:", font = ("Arial")).place(x = 20, y = 150)
    lab_pwsm = Label(login_successfulcessful, text = "Your Birth day:", font = ("Arial")).place(x = 20, y = 180)

    name = Label(login_successfulcessful, text = accounts[i]['name'], font = ("Arial")).place(x = 160, y = 120)
    user = Label(login_successfulcessful, text = accounts[i]['email'], font = ("Arial")).place(x = 160, y = 150)
    bd = Label(login_successfulcessful, text = accounts[i]['bd'], font = ("Arial")).place(x = 160, y = 180)

    button = Button(login_successfulcessful, text = "cancel ",command = des).place(x = 200, y = 220)
def forget_password():
    fg = Tk()
    fg.geometry("545x545")
    def show_pw():
        for i in range(len(accounts)):
            if accounts[i]['email'] == user_var.get():
                show_p = Label(fg, text = "password of account " + accounts[i]['email'] + " is: " + accounts[i]['pw'], font = ("Arial", 12)).place(x = 110, y = 220)
                hidden = Label(fg, text = "                                                       ").place(x = 180, y = 2)
            elif i == len(accounts) - 1:
                error = Label(fg, text = "Account name not found", fg = "red").place(x = 180, y = 2)
    user_var = StringVar(fg)
    name_title = Label(fg, text = "Forget Password", font = ("Arial", 20)).place(x = 150, y = 40)
    user = Label(fg, text = "the username whose password you forgot: ", font = ("Arial")).place(x = 120, y = 120)
    en_user = Entry(master = fg, width = 50, textvariable = user_var).place(x = 110, y = 150)
    button_fg = Button(fg, text = "show", command = show_pw)
    button_fg.place(x = 200, y = 180)
def check_login():
    for i in range(len(accounts)):
        if login_u.get() == accounts[i]['email']:
            if login_p.get() == accounts[i]['pw']:
                window_login_successful(i)
            else:
                error = Label(win, text = "           wrong password                        ", fg = "red").place(x = 180, y = 2)
                forget_pw = Button(win, text = "forget password?", command = forget_password)
                forget_pw.place(x = 400, y = 180)
        elif i == len(accounts) - 1:
            error = Label(win, text = "Account name not found", fg = "red").place(x = 180, y = 2)
def cre_account():
    def sign_up():
        if var_p.get() != var_s.get():
            wrong_pw = Label(cre, text = "wrong password", fg = "red", anchor = "n").place(x = 180, y = 2)
            return 0
        else:
            acc = {
                'name': var_n.get(),
                'email': var_u.get(),
                'pw': var_p.get(),
                'bd': var_bd.get()
            }
            json_object = json.dumps(acc, indent=4)
            with open("sample.json", "w") as outfile:
                outfile.write(json_object)

            accounts.append(acc)
            cre.destroy()
    cre = Tk()
    cre.title("Create Account")
    cre.geometry("545x545")
    var_n = StringVar(cre)
    var_u = StringVar(cre)
    var_p = StringVar(cre)
    var_s = StringVar(cre)
    var_bd = StringVar(cre)

    name_cre = Label(cre, text = "Sign Up", font = ("Arial", 25)).place(x = 200, y = 40)

    lab_name = Label(cre, text = "Your name: ", font = ("Arial")).place(x = 20, y = 120)
    lab_user = Label(cre, text = "User name:", font = ("Arial")).place(x = 20, y = 150)
    lab_pw = Label(cre, text = "Password:", font = ("Arial")).place(x = 20, y = 180)
    lab_pwsm = Label(cre, text = "Password Submit:", font = ("Arial")).place(x = 20, y = 210)
    lab_pwsm = Label(cre, text = "Your Birth day:", font = ("Arial")).place(x = 20, y = 240)

    lab_name = Entry(master = cre, width = 50, textvariable = var_n).place(x = 160, y = 120)
    en_user = Entry(master = cre, width = 50, textvariable = var_u).place(x = 160, y = 150)
    en_pw = Entry(master = cre, width = 50, textvariable = var_p, show = "*").place(x = 160, y = 180)
    lab_pwsm = Entry(master = cre, width = 50, textvariable = var_s, show = "*").place(x = 160, y = 210)
    lab_bd = Entry(master = cre, width = 50, textvariable = var_bd).place(x = 160, y = 240)
    
    button_Login = Button(cre, text = "Login", font = ("Arial"), command = sign_up)
    button_Login.place(x = 200, y = 280)
login_u = StringVar(win)
login_p = StringVar(win)

name = Label(win, text = "Login", font = ("Arial", 25)).place(x = 200, y = 40)
lab_user = Label(win, text = "Users name:", font = ("Arial")).place(x = 20, y = 120)
lab_pw = Label(win, text = "Password:", font = ("Arial")).place(x = 20, y = 150)
en_user = Entry(master = win, width = 50, textvariable = login_u).place(x = 130, y = 120)
en_user = Entry(master = win, width = 50, textvariable = login_p, show = "*").place(x = 130, y = 150)
cre_acc = Button(win, text = "create account", font = ("Arial"), command = cre_account)
cre_acc.place(x = 400, y = 60)
button_Login = Button(win, text = "Login", font = ("Arial"), command = check_login)
button_Login.place(x = 200, y = 220)
win.mainloop()
