import IdentificationServiceHttpClientHelper
import sys
import speech_recognition as sr


cogkey = "4cd15a3619394e3898164401d7386ad5"

def create_profile(subscription_key, locale):
    """Creates a profile on the server.

    Arguments:
    subscription_key -- the subscription key string
    locale -- the locale string
    """
    getAudio()
    
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        subscription_key)

    creation_response = helper.create_profile(locale)

    print('Profile ID = {0}'.format(creation_response.get_profile_id()))
    
    profileid = creation.response.get_profile_id()

    enrollment_response = helper.enroll_profile(
        profileid,
        "result.wav",
        force_short_audio.lower() == "true")
    
    print('Total Enrollment Speech Time = {0}'.format(enrollment_response.get_total_speech_time()))
    print('Remaining Enrollment Time = {0}'.format(enrollment_response.get_remaining_speech_time()))
    print('Speech Time = {0}'.format(enrollment_response.get_speech_time()))
    print('Enrollment Status = {0}'.format(enrollment_response.get_enrollment_status()))
    

def getAudio():
    
    with sr.Microphone() as source:
        mic = sr.Microphone()
        for device_index in mic.list_working_microphones():
            m = mic(device_index=device_index)
            break
        else:
            print("No working microphones found!")
        
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say stuff")
        audio = r.listen(source)
        
    with open("result.wav", "wb") as f:
        f.write(audio.get_wav_data())
    print("Recorded file")
    
    try:
        data = r.recognize_google(audio)
        print("Heard: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

#create_profile(cogkey, 'en-us')

getAudio()