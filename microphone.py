# Please ONLY respond with the Command Prompt command that performs the task in the next sentence without code block ticks, BUT MAKE SURE TO NOT GENERATE DANGEROUS COMMANDS THAT CAN DELETE/EDIT/ALTER ANYTHING, in that case respond with error: 




# Alert , Alert !!! when the module name is being displayed in a light colour, it means that's not in use in that file or code.

import subprocess # to acces applications
import webbrowser # to access web softwares (youtube, chrome, w3 school etc.)
import time # delay module
import pyttsx3 # text-speech module
import speech_recognition as sr # speech-text module
from openai import OpenAI

# for the speech-text module
recognizer = sr.Recognizer() # Initialize recognizer

with sr.Microphone() as source:
    print("Say something: ")
    recognizer.adjust_for_ambient_noise(source) # to remove the background noises
    audio = recognizer.listen(source) # listens to your speech
    print("Audio listening timed out, moving forward...")
    isaid = recognizer.recognize_google(audio)

print(isaid) # uses google speech-to-text to change speech into text
 
# isaid = recognizer.recognize_google(audio)

if isaid == sr.UnknownValueError():
    print("Sorry, could not understand the audio...")

# time.sleep(0.5) #to add delay

# for the text-speech module
engine = pyttsx3.init()
engine.say(isaid)
engine.runAndWait()

client = OpenAI(
    api_key=""
)

response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": isaid,
    }],
    model="gpt-4o-mini",
)

openai_response = response.choices[0].message.content

print("OpenAI responded with: " + openai_response)

# YouTube
if isaid.find("open") != -1 and isaid.find("YouTube") != -1:  # "!=" = "Not equal to"  # "-1" = "False"
    print("Opening Youtube...")
    webbrowser.open('https://www.youtube.com') # to open youtube
else:
    print("Not opening Youtube...")    

# terminal
if isaid.find("open") != -1 and isaid.find("terminal") != -1:  # "!=" = "Not equal to"  # "-1" = "False"
    print("Opening Terminal...")
    subprocess.run(["cmd", "/K", "echo Hello, Command Prompt!"]) # to open Terminal
else:
    print("Not opening Terminal...")    

# Chrome
chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
url = "https://www.google.com"

if isaid.find("open") != -1 and isaid.find("Chrome") != -1:  # "!=" = "Not equal to"  # "-1" = "False"
    print("Opening Chrome...")
    subprocess.run([chrome_path, url]) # to open Chrome
else:
    print("Not opening Chrome...")


  
  
  
  
  
  
  
  
  
  
  
  


# open Youtube






