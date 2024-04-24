import speech_recognition as sr
import pyaudio
import serial
import time
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)


try:
    arduino = serial.Serial('COM3', 9600)
    print('Rilevato dispositivo ARDUINO COM3' )
    engine.say('Rilevato dispositivo arduino porta COM3')
    engine.runAndWait()
    print(arduino)
except Exception as e:
    print('Nessun disposito arduino collegato...')
    print(e)
    


time.sleep(2)
text=''
selection=''


while(selection!='exit'):

    engine.say('Seleziona il tipo di operazione')
    engine.runAndWait()

    selection=input('Seleziona il tipo di operazione: ')
    
    engine.say('Hai selezionato il protocollo' + selection)
    engine.runAndWait()
    

    if selection in 'riconoscimento vocale':


        while('exit' not in text):

            init_rec = sr.Recognizer()
            print("Perfetto, ti ascolto")
            engine.say('Perfetto, ti ascolto')
            engine.runAndWait()

            with sr.Microphone() as source:
                
                try:
                    audio_data = init_rec.record(source, duration=10)
                    
                    text = init_rec.recognize_google(audio_data,language="it-IT")
                    
                    print("Sto elaborando...")
                    engine.say('Sto elaborando...' + text)
                    engine.runAndWait()

                    
                    time.sleep(1)
                    print("Verifico disponibilita' operazione per la parola..." + text)
                    engine.say("Verifico disponibilita operazione per la parola..." + text)
                    engine.runAndWait()
                    time.sleep(2)

                except:

                    print('Nessun comando vocale rilevato...')
                    engine.say('Nessun comando vocale rilevato...')
                    engine.runAndWait()
                    exit_snt=''
                    exit_snt=input('Vuoi uscire?: Si/No ')
                    if exit_snt=='Si':
                        text='exit'
                    time.sleep(2)

            if 'luce' in text:
                print("Accendo luce verde ...")
                engine.say('Accendo luce verde ...')
                engine.runAndWait()
                arduino.write(b'1')
                
                time.sleep(2)

                

            
            
            elif 'servo' in text:
                print('Attivazione motore')
                engine.say('Attivazione motore.')
                engine.runAndWait()
                arduino.write(b'3')
                
                time.sleep(2)

            elif 'sonar' in text:
                print('Attivazione sonar')
                engine.say('Attivazione sonar.')
                engine.runAndWait()
                arduino.write(b'4')

                
                time.sleep(2)
                
                data=arduino.readline()
                print(data)

            else:
                print('Nessuna Operazione Rilevata')
                engine.say('Nessuna Operazione Rilevata')
                engine.runAndWait()
                time.sleep(4)

            text=''
            print("Operazione effettuata")
            engine.say('Operazione effettuata, continuo protocollo script piton')
            engine.runAndWait()

                
    arduino.close()


