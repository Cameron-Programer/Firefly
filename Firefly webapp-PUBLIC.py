import webbrowser        
import easygui
import os
import requests

#Cameron Mackie (C)2020 GNU Genral Public License v3.0
#All modifcations to this code must be releaced under this license and must be autharised by Cameron mackie to be Uploaded for redistrbuction 

print("Go to https://discord.gg/EXcdae2mWa for support ")
helppage = easygui.enterbox("Welcome to the Unoficial Firefly webapp. If you need any help type 'Help' for more the help page.","Firefly")
if helppage == ("Help"):
    easygui.msgbox("The browsers that we support are: Crome/Cromeum, Edge, Firefox and Opra and the redownload the files and more support go to https://discord.gg/EXcdae2mWa","Webapp Support")
gh = ("The program has been ran +1 times")
#if helppage == ("FIRST"):
 #   Namer = eaesygui.enterbox("Please enter the diretory name for your account")
Uname = easygui.enterbox("Enter your username here", "Firefly")

Pword = easygui.passwordbox("Enter your password", "Firefly")
#Cameron Mackie (C)2020 GNU Genral Public License v3.0
easygui.msgbox("When Promted click 'login' ","Firefly")
easygui.msgbox("Redirecting...", "Firefly")

#Cameron Mackie (C)2020 GNU Genral Public License v3.0
webbrowser.open('file://' + os.path.realpath(r"C:\Users\camer\Downloads\Firefly web app\Requiredxfiles\Firefly HTML app-PUBLIC.html"))
 
#Cameron Mackie (C)2020 GNU Genral Public License v3.0

with open("runtimedata.txt","w")as a:
    a.write(gh)
