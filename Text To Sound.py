#Text To Sound v 0.2
from tika import parser
from gtts import gTTS, gTTSError
from playsound import playsound, PlaysoundException

#FUTURES IMPORTS 
#for IA and Text Recognition Pattern
#from texts import text_counter, text_training
#from sklearn.feature_extraction.text 

#Giving a name to the file
filename = input ("Write a name to your File: ")

#Write a path to look the file up
file = input ("Enter the path of your File: ")

parser = parser.from_file(file)
txt = parser['content']
speech = gTTS(text = txt, lang = 'es')
speech.save(filename +".mp3")

print('Blow your speakers out!')
print ("Enjoy! =D")

#Turning the Musiiiiiic up! (Well, technically it's a book) xD
playsound(filename+".mp3")
