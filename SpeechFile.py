import pyttsx3


def Voicesay():
    engine.say(text)
    engine.runAndWait()


def RateChangeFunction():
    rate_change = int(input("Select the rate between 100 to 200:\n"))
    engine.setProperty('rate', rate_change)


def VoiceChangeFunction():
    voice_change = int(input("Select '1' for Female Voice Or Select '0' for male Voice\n "))
    engine.setProperty('voice', voices[voice_change].id)


engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
yes = ['yes', 'y']

text = input("Enter the text You wanted to convert to speech:\n")

while True:
    choice = input("Would you like to listen the audio file? Y or N to create a audio file \n")
    if choice.lower() in yes:
        Voicesay()
        changes_choice = input("Would you like to change the speed of the voice or change the voice to male or female?\n")
        if changes_choice.lower() in yes:
            RateChangeFunction()
            Voicesay()
            VoiceChangeFunction()
            Voicesay()
    elif choice.lower() in ['no', 'n']:
        file_name = input("Name Your Mp3 file:\n")
        engine.save_to_file(text, file_name + '.mp3')
        engine.runAndWait()
        break
