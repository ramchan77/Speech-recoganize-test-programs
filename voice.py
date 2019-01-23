import speech_recognition as sr  

# get audio from the microphone                                                                       
r = sr.Recognizer()
captcha_a = sr.AudioFile('myfile3.wav')
with captcha_a as source:                                                                       
    #print("Speak:")
    #r.adjust_for_ambient_noise(source)
    audio = r.record(source)
try:
    print("You said " + r.recognize_bing(audio,key='4782f102dcf4453d939624cdda8d8e63'))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
