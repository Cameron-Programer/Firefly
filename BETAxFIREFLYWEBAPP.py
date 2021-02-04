import requests
import easygui
import os
import sys

Startup = easygui.enterbox("welcome to firefly web app V2.")

if Startup == ("Start"):
    os.startfile(r"C:\Users\Cameron\Documents\Code\Fireflyxwebappxpublic.html")
    sys.exit
  

else:
    easygui.msgbox("When prompted click on 'click here'")
    easygui.msgbox("Redirecting....")
    easygui.msgbox("Transfering you now have a good day")
    os.startfile(r"C:\Users\Cameron\Documents\Code\Fireflyxwebappxpublic.html ")



    