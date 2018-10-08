import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say stuff")
    audio = r.record(source, 10)
        
with open("result.wav", "wb") as f:
    f.write(audio.get_wav_data())
    print("Recorded file")