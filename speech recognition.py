import speech_recognition as SR
a=SR.Recognizer()
with SR.Microphone() as source:
    print("Speak Anything:")
    audio = a.listen(source)
    try:
        text = a.recognize_google(audio)
        print("You Said:", text)
    except:
        print("Sorry! could not recognize your voice")
    import webbrowser

    text = a.recognize_google(audio)
    webbrowser.open("https://google.co.in/search?q="+text)