import os
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import simpleaudio as sa
import tkinter as tk



authenticator = IAMAuthenticator('{API_KEY}')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)
text_to_speech.set_service_url('{URL}')



def playFunction(stringVal):


	with open('./responses/hello_world.wav', 'wb') as audio_file:
	    audio_file.write(
	        text_to_speech.synthesize(
	            stringVal,
	            voice='en-US_EmilyV3Voice',
	            accept='audio/wav'        
	        ).get_result().content)


	filename = './responses/hello_world.wav'
	wave_obj = sa.WaveObject.from_wave_file(filename)
	play_obj = wave_obj.play()
	#play_obj.wait_done()


def getValsAndPlay():
	str1 = e1.get()
	playFunction(str1)


'''Storing canned responses'''

def storeFirstCannedResponse(strVal2):

	with open('./responses/firstCannedReponse.wav', 'wb') as audio_file:
	    audio_file.write(
	        text_to_speech.synthesize(
	            strVal2,
	            voice='en-US_EmilyV3Voice',
	            accept='audio/wav'        
	        ).get_result().content)

def getValsAndStore1():
	str2 = e2.get()
	storeFirstCannedResponse(str2)



'''Play the canned responses'''
def playSound1():
	filename = './responses/firstCannedReponse.wav'
	wave_obj = sa.WaveObject.from_wave_file(filename)
	play_obj = wave_obj.play()

'''clear the sound files that have been genereated '''
def clearSoundStorage():
	mydir = './responses'
	filelist = [ f for f in os.listdir(mydir) if f.endswith(".wav") ]
	for f in filelist:
		os.remove(os.path.join(mydir, f))


'''Here, we implement the user interface of the application'''

master = tk.Tk()
tk.Label(master, 
         text="Live statement").grid(row=0)


e1 = tk.Entry(master)
e1.grid(row=0, column=1)

tk.Button(master, 
          text='Play Live statement', command=getValsAndPlay).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)


tk.Label(master, 
         text="First Canned response").grid(row=0)

e2 = tk.Entry(master)
e2.grid(row=0, column=2)

tk.Button(master, 
          text='Store first canned statement', command=getValsAndStore1).grid(row=3, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.Button(master, 
          text='Play first canned statement', command=playSound1).grid(row=4, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.Button(master, 
          text='Clear Sound Storage', command=clearSoundStorage).grid(row=5, 
                                                       column=2, 
                                                       sticky=tk.W, 
                                                       pady=4)
tk.mainloop()