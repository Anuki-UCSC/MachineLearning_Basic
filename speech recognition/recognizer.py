import speech_recognition as sr



def main():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adgust_for_ambient_noise(source)

    print("please say somthing")

    audio=r.listen(source)

    try:
        print("you have said : \n " +r.recognize_google(audio))


    except Exception as e:
        print("Error :" +str(e))


if __name__=="__main__":
        main()