import eel
import pyowm

owm = pyowm.OWM("f3a3ff0a16d24c5d88a1b5cd947f2a83")

@eel.expose
def get_weather(place):

    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)

    w = observation.weather

    temp = w.temperature('celsius')['temp']
    return "В городе " + place +" сейчас "+str(temp)+" градусов"
    
eel.init("web")

eel.start("main.html", size=(700,500))