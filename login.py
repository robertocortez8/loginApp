from tkinter import * 
import os
def main_menu():
	global main_window
	main_window = Tk()
	main_window.geometry("300x300")
	main_window.title("login system")
	Label1 = Label(main_window,text="Choose an option" , bg="gray" , fg="blue")
	Label1.pack(fill=X, pady=20)
	login_btn = Button(main_window,text="login",width="30", height="2", command=login)
	login_btn.pack(pady=20)
	new_user_btn = Button(main_window,text="New User",width="30", height="2", command=new_user)
	new_user_btn.pack(pady=20)
	main_window.mainloop()

def new_user():
	global username
	global password
	global fullname
	global username_entry
	global password_entry
	global fullname_entry
	global new_user_window


	new_user_window=Toplevel(main_window)
	new_user_window.title("New User")
	new_user_window.geometry("500x500")

	username= StringVar()
	password=StringVar()
	fullname=StringVar()
	label2 = Label(new_user_window,text="Please fill in the info below", bg="red" , fg="yellow")
	label2.pack(fill=X, pady=20)

	user_info_panel= Frame(new_user_window)
	user_info_panel.pack(pady=20)
	
	username_label=Label(user_info_panel,text="Username: ")
	username_label.grid(row=0,column=0)
	username_entry= Entry(user_info_panel, textvariable=username)
	username_entry.grid(row=0,column=1)

	Label(user_info_panel, text="").grid(row=1)

	password_label=Label(user_info_panel,text="Password: ")
	password_label.grid(row=2,column=0)
	password_entry= Entry(user_info_panel, textvariable=password)
	password_entry.grid(row=2,column=1)

	Label(user_info_panel, text="").grid(row=1)

	fullname_label=Label(user_info_panel,text="Full name ")
	fullname_label.grid(row=3,column=0)
	fullname_entry= Entry(user_info_panel, textvariable=fullname)
	fullname_entry.grid(row=3,column=1)

	register_btn = Button(new_user_window, text="Register",command=register)
	register_btn.pack()
def register():
	registered = False
	username_text= username.get()
	password_text=password.get()
	name_text=fullname.get()
	file = open("credential.txt","a")
	for line in open("credential.txt","r").readlines():
		login_info = line.split()
		if username_text == login_info[1]:
			registered=True
	if registered:
		file.close()
		username_entry.delete(0,END)
		password_entry.delete(0,END)
		fullname_entry.delete(0,END)
		print("user already exists")
		failed_register_window = Toplevel(new_user_window)
		failed_register_window.geometry("300x300")
		failed_register_window.title("you are being warned")
		Label(failed_register_window, text="username already exists bro quit playing!",bg="purple").pack(fill=X,pady=20)
		ok_btn = Button(failed_register_window, text="keep trying", width="20" ,command = lambda :failed_register_window.destroy())
		ok_btn.pack(pady=20)

	else:
		file.write("Username: "+username_text+" Password: "+password_text+" Name: "+name_text+"\n")
		file.close()
		username_entry.delete(0,END)
		password_entry.delete(0,END)
		fullname_entry.delete(0,END)
		successful_register_window = Toplevel(new_user_window)
		successful_register_window.geometry("300x300")
		successful_register_window.title("JOY!")
		Label(successful_register_window, text="Successful register!",bg="purple").pack(fill=X,pady=20)
		ok_btn = Button(successful_register_window, text="OK", width="20" ,command = lambda :successful_register_window.destroy())
		ok_btn.pack(pady=20)

def login():
	global username_verify
	global username_verify_entry
	global password_verify
	global password_verify_entry
	global login_window
	login_window = Toplevel(main_window)
	login_window.geometry("400x400")
	login_window.title("log on in")
	label2 = Label(login_window,text="Please enter your credentials below", bg="gray", fg="blue")
	label2.pack(fill=X, pady=20)

	credentials_panel= Frame(login_window)
	credentials_panel.pack(pady=20)

	username_verify=StringVar()
	password_verify=StringVar()

	username_label=Label(credentials_panel,text="Username: ")
	username_label.grid(row=0,column=0)
	username_verify_entry= Entry(credentials_panel, textvariable=username_verify)
	username_verify_entry.grid(row=0,column=1)

	Label(credentials_panel, text="").grid(row=1)

	password_label=Label(credentials_panel,text="Password: ")
	password_label.grid(row=2,column=0)
	password_verify_entry= Entry(credentials_panel, textvariable=password_verify, show="*")
	password_verify_entry.grid(row=2,column=1)

	login_btn = Button(login_window, text="Login", command = login_verify)
	login_btn.pack(pady=20)

def login_verify():
	user=username_verify.get()
	pswrd= password_verify.get()
	login=False
	for line in open("credential.txt","r").readlines():
		login_info = line.split()
		if user == login_info[1] and pswrd == login_info[3]:
			login = True
	if login:
		Label1 = Label(login_window,text="Successful login" ,fg="green")
		Label1.pack()
	else:
		failed_login_window = Toplevel(login_window)
		failed_login_window.geometry("200x200")
		failed_login_window.title("Warning!")
		Label(failed_login_window, text="Try Again!",bg="gray" ,fg="blue").pack(fill=X,pady=20)
		ok_btn = Button(failed_login_window, text="OK", width="20", command = lambda :failed_login_window)
		ok_btn.pack(pady=20)
main_menu()