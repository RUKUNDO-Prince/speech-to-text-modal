import speech_recognition as sr
import pyttsx3

# INITIALIZE RECOGNIZER
r = sr.Recognizer()

def record_text():
    # LOOP IN CASE OF ERRORS
    while(1):
        try:
            #USE MICROPHONE AS THE SOURCE OF INPUT
            with sr.Microphone() as source2:
                # PREPARE RECOGNIZER TO RECEIVE INPUT
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # LISTENS FOR THE USER'S INPUT
                audio2 = r.listen(source2)

                # USE GOOGLE TO RECOGNIZE AUDIO
                MyText = r.recognize_google(audio2)

                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown error occured")


    return

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()

    return

while(1):
    text = record_text()
    output_text(text)

    print("Wrote text")