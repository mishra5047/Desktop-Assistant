import os
import webbrowser

print("Hey There, I Am Your Assistant")
input = input("Enter Your Choice  ")

if("brave" in input):
    os.system("brave-browser")
     
elif("android" in input):
    os.system("android-studio")

elif("telegram" in input):
    os.system("telegram-desktop")

elif("office" in input or "libre" in input):
    os.system("libreoffice")

elif("search" in input):
    key = input[6::]
    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' %key)

elif("anydesk" in input or "desk" in input):
    os.system("libreoffice")

elif("filezilla" in input or "zilla" in input):
    os.system("filezilla")    

elif("camera" in input):
    os.system("cheese")

elif("teamviewer" in input):
    os.system("teamviewer")

elif("code" in input or "editor" in input or "visual" in input or "studio" in input):
    os.system("code")    

elif (input == ""):
    print("enter valid choice")