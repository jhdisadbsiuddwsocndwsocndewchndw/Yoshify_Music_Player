import tkinter as tk
from databaseV2 import addUser, checkUser
from YoshifyV2 import open_player


# class used to store a user's login details as an object
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


root = tk.Tk()
root.title("Yoshify Login")
root.geometry("500x600")
root.configure(bg="purple")

# make column 0 expand equally on both sides so widgets sit centered
root.grid_columnconfigure(0, weight=1)

# this frame holds all the login screen widgets
loginFrame = tk.Frame(root, bg="purple")
loginFrame.grid(row=0, column=0)


def signup():
    # gets text from the entry boxes and creates a User object
    username = usernameEntry.get()
    password = passwordEntry.get()
    newUser = User(username, password)

    # saves the new user to the database
    addUser(newUser.username, newUser.password)
    messageLabel.config(text="Account created")


def login():
    # gets text from the entry boxes and creates a User object
    username = usernameEntry.get()
    password = passwordEntry.get()
    user = User(username, password)

    # checks the database to see if the login details are correct
    if checkUser(user.username, user.password):
        messageLabel.config(text="Login successful")
        loginFrame.grid_forget()   # hides the login screen
        open_player(root)          # opens the music player from YoshifyV2.py
    else:
        messageLabel.config(text="Wrong username or password")


titleLabel = tk.Label(loginFrame, text="Yoshify Login", font=("Arial", 24, "bold"), bg="purple", fg="white")
titleLabel.grid(row=0, column=0, pady=20)

usernameLabel = tk.Label(loginFrame, text="Username", bg="purple", fg="white")
usernameLabel.grid(row=1, column=0)

usernameEntry = tk.Entry(loginFrame)
usernameEntry.grid(row=2, column=0, pady=5)

passwordLabel = tk.Label(loginFrame, text="Password", bg="purple", fg="white")
passwordLabel.grid(row=3, column=0)

passwordEntry = tk.Entry(loginFrame, show="*")
passwordEntry.grid(row=4, column=0, pady=5)

loginBtn = tk.Button(loginFrame, text="Login", command=login)
loginBtn.grid(row=5, column=0, pady=5)

signupBtn = tk.Button(loginFrame, text="Sign Up", command=signup)
signupBtn.grid(row=6, column=0, pady=5)

messageLabel = tk.Label(loginFrame, text="", bg="purple", fg="white")
messageLabel.grid(row=7, column=0, pady=10)

root.mainloop()
