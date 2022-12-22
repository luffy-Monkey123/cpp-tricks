import pyttsx3 as p
from pyttsx3 import engine

salva=p.init()#initializing the voice engine
voices=salva.getProperty("voices")#setting the engine properties
salva.setProperty("voice",voices[1].id)
salva.setProperty("rate",120)

salva.say("""
    Batch Operating System
Multiprogramming Operating System
Time-Sharing OS
Multiprocessing OS
Distributed OS
Network OS
Real Time OS
Embedded OS 
""") #Words to say

salva.runAndWait()#run until finished
