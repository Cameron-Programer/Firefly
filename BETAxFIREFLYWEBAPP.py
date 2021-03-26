import requests
import easygui
import os
import sys
#welcome message 
Startup = easygui.enterbox("welcome to firefly web app V2.","Firefly Webapp")

if Startup == ("Start"):
    #Edit directory below to where you stored the HTML file
   os.startfile(r"C:\%USERPROFILE%\Documents\Fireflyxwebappxpublic.html ")
   #this stops the program after an if statment there is proably a better way to do this but this is what you deserve
    sys.exit
  
#read the bit in speach marks it will make sense your a big boy you dont need me to spell it out 
else:
    easygui.msgbox("When prompted click on 'click here'","Firefly Webapp")
    easygui.msgbox("Redirecting....","Firefly Webapp")
    easygui.msgbox("Transfering you now have a good day","Firefly Webapp")
    #Opens the HTML file / Edit directory below to where you stored the HTML file
    os.startfile(r"C:\%USERPROFILE%\Documents\Fireflyxwebappxpublic.html ")

#Updated to use the %USERPROFILE% Var

    
