import pyttsx3
import pyowm

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


owm = pyowm.OWM('432bf8fe56c1cdb618a5cf45e8fbbe9b')

speak("enter the place::")

a=input("enter the place::")
boston = owm.weather_at_place(a)
weather = boston.get_weather()
speak("the current temperature  is:") 
speak(weather.get_temperature('celsius')['temp'])
speak("the sunrise time:") 
speak(weather.get_sunrise_time(timeformat='iso'))
speak("the sunset time  is :") 
speak(weather.get_sunset_time(timeformat='iso'))