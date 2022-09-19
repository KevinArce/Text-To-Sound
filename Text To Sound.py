#Text To Sound
from tika import parser
from gtts import gTTS, gTTSError
from playsound import playsound, PlaysoundException
import os.path

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
speech = gTTS(text = txt, lang = 'en')
speech.save(f"{filename}.mp3")

#Path to save the file
directory = input('Enter a path to save the New File: ')
os.path.join(directory ,filename)
if not os.path.isdir(directory):
    os.mkdir(directory)

print('Your AudioBook has been saved here: ')
print(directory)

print('Blow your speakers out!')
print ("Enjoy! =D")

#Turning up the Musiiiiiic! (Well, technically it's a book) xD
playsound(f"{filename}.mp3")
