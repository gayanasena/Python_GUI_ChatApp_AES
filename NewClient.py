from socket import *
from threading import *
from tkinter import *
import tkinter.font as tkFont
from Crypto.Cipher import AES
import base64

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

hostIp = "127.0.0.1"
portNumber = 7500

# make connection
try:
    clientSocket.connect((hostIp, portNumber))
except:
    print("Server not ready")

root = Tk()

# setting title
root.title("Secure Chat© - IP: " +hostIp+":"+str(portNumber))

# setting window size
width = 346
height = 512
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

# Send button image
sendBtnImg = PhotoImage(file="sendMsgImg.png")

# Fonts
ft = tkFont.Font(family='Times', size=10)
ht = tkFont.Font(family="Times", size=14)

# Components
# Entry
inputtxt = Entry(root,borderwidth = "1px", font = ft, fg = "black" )
inputtxt.place(x=10,y=460,width=254,height=30)

# Listbox
viewlstbox = Listbox(root, borderwidth = "1px", font = ft, fg = "black")
viewlstbox.place(x=10,y=60,width=323,height=392)

# Header Label
headerlbl = Label(root, font=ht, fg="#393d49", justify="left", text="Secure Chat App", relief="flat")
headerlbl.place(x=10, y=20, width=133, height=30)

def sendMessage():
    clientMessage = inputtxt.get()
    viewlstbox.insert(END, "\n" + "You: " + clientMessage)
    clientSocket.send(clientMessage.encode("utf-8"))
    inputtxt.delete(0,END)

# Send Button
btnSendMessage = Button(root, image=sendBtnImg, borderwidth=0, command=sendMessage)
btnSendMessage.place(x=270, y=460, width=65, height=31)


def recvMessage():
    try:
        serverMessage = clientSocket.recv(1024).decode("utf-8")
        print(serverMessage)
        viewlstbox.insert(END, "\n" + serverMessage)
    except:
        viewlstbox.insert(END, "\n" + "Server not connected")

# Create thread for massage recv
recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()

root.mainloop()
