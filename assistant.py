import os
import webbrowser
import speech_recognition as s_r

def search(input):

    if (input == ""):
        print("enter valid choice")

    elif("brave" in input):
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

    elif("vlc" in input):
        os.system("vlc")

    elif("teams" in input):
        os.system("teams")

print("Hey There, I Am Your Assistant")
choice = int(input("Enter Your Choice \n 1. Voice Based \n 2. Text Based\n\n"))

if(choice == 1):
    
    mic = s_r.Microphone()
    r = s_r.Recognizer()
    my_mic = s_r.Microphone()

    with my_mic as source:
        print("Speak Your Desire")
        r.pause_threshold = 1
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') 
            print(f"User said: {query}\n")
        
        except Exception as e:
            print("Please Say That Again")


elif(choice == 2):
    
    data = input("What Can I Do For You\n")
    search(data)    