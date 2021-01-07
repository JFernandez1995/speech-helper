# SpeechHelper

This python application uses the simpleaudio, tkinter, and IBM Watson APIs.
The main intent is to help those with troubles of speaking, voice out their 
statemets using a vitrual synthesizer.

The user can create live statements for realtime usability or
generate canned repsonses for common statements used in their day-to-day lives

#To Run:
python speechHelper.py

#Dependencies:
You may want to install the 'simpleaudio', 'tkinter', and 'ibm_watson' dependencies using pip.

To obatin the {apikey} and {url} variables, you need to create an IBM cloud account and enable the 'Text to Speech' service in your account. 

#You're going to need to downgrade pyJWT for this project:
	pip install PyJWT==1.7.1
