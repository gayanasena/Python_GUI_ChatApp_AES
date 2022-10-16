from socket import *
import time
import threading
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "127.0.0.1"
portNumber = 7500

clientSocket.connect((hostIp, portNumber))

class App:



    def __init__(self, root):

        #setting title
        root.title("Secure Chat© - Connected To: "+ "hostIp+ :+str(portNumber)")

        #setting window size
        width=346
        height=512
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Send button image
        sendBtnImg = PhotoImage(file="sendMsgImg.png")

        # Fonts
        ft = tkFont.Font(family='Times', size=10)
        ht = tkFont.Font(family = "Times", size=14)

        # Components

        # Listbox
        viewlstbox=tk.Listbox(root, borderwidth = "1px", font =ft, fg = "white", justify = "center")
        viewlstbox.place(x=10,y=60,width=323,height=392)

        # Entry
        inputtxt=tk.Entry(root, borderwidth = "1px", font =ft, fg = "black", justify = "left", text = "Type Message here...")
        inputtxt.place(x=10,y=460,width=254,height=30)

        # Send Button
        sendbtn=tk.Button(root,command = self.sendbtn, text = "Send")
        sendbtn.place(x=270,y=460,width=65,height=31)

        # Header Label
        headerlbl=tk.Label(root, font = ht, fg = "#393d49", justify = "left", text  = "Secure Chat App", relief = "flat")
        headerlbl.place(x=10,y=20,width=133,height=30)

    def sendMessage():
        clientMessage = inputtxt.get()
        txtMessages.insert(END, "\n" + "You: " + clientMessage)
        clientSocket.send(clientMessage.encode("utf-8"))

    btnSendMessage = Button(window, image=sendBtnImg, borderwidth=0, command=sendMessage)
    btnSendMessage.grid(row=1, column=0, padx=10, pady=10)

    def recvMessage():
        while True:
            serverMessage = clientSocket.recv(1024).decode("utf-8")
            print(serverMessage)
            txtMessages.insert(END, "\n" + serverMessage)

    def sendbtn(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
