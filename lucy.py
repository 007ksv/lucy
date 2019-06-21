import gtts
import speech_recognition as sr
import os


def speak(data):
	tts=gtts.gTTS(data,'en')
	tts.save("/home/ksv/python/personal_assistant/audios/speak_audio.mp3")
	os.system("mpg123 /home/ksv/python/personal_assistant/audios/speak_audio.mp3")

def speech_recognize():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("Speak now...")
		audio=r.listen(source)
		data=""
		try:
			data = r.recognize_google(audio)
			print("You said "+data)
		except:
			print("Error while getting your sound...")
			speech_recognize()

def lucy(data):
	if "how are you" in data:
		speak("i am fine")
	if  "what is the time" in data:
		speak(os.system("time"))
	if "search google for" is data:
		data = data.split(" ")
		query= data[3]
		os.system("firefox www.google.com/"+query)
	if "what is your name" is data:
		speak("my name is lucy and i am your personal assistant")

def main():
	data=speech_recognize()
	lucy(data)

main()