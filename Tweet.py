"""
Twitter
"""
import tweepy #libreria twitter
import os #directorio
import RPi.GPIO as GPIO #raspberry pines
from subprocess import call #ejecutar cosas del comand window
import time #tiempo
import MFRC522 #rfid
import signal #rfid

continue_reading = True #funcion rfid
def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()


# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

#Directory
os.chdir(r'/home/pi/Documents/TWEET')

# Consumer keys and access tokens, used for OAuth
consumer_key='RP57gxOUiDeTq0JSAPWf4oQ9n'
consumer_secret='SYScTBa0C1eUz0NrGn2YkkAFhvOhOwvRCbcidVOQKgOHpWnLpI'
access_token_key='1002004607722192903-Cd271PhLxtMxwZGtix8CGiCaJpGvRF'
access_token_secret='hFXN570qoTfj38mnuW8elHqBKF3pOpviK6r10uasAGk6J'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Creates the user object. The me() method returns the user whose authentication keys were used.
user = api.me()
 
#print('Name: ' + user.name)
#print('Location: ' + user.location)
#print('Friends: ' + str(user.friends_count))
 
# Sample method, used to update a status

# Scan for cards    
    



img_counter=0
while True:
##    if GPIO.input(TRIG)==True:
##        print("Sensor Leido")
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print("Card detected")
        img_name = "try_{}.png".format(img_counter)
        print(img_name)
        ret=call(["fswebcam",img_name])#ejecutando desde el comand window fswebcam
        time.sleep(0.5)
        print("{} written!".format(img_name))
        
        # load image
        imagePath = "try_{}.png".format(img_counter)
        status = "Hi! POSTING PICTURE FROM RASPBERRI try_{}.png".format(img_counter)
        # Send the tweet.
        try: api.update_with_media(imagePath, status)
        except:
            print("Intente")
            time.sleep(8)
            print("Matando")
            call(["fswebcam",img_name])
            time.sleep(0.5)
            api.update_with_media(imagePath, status)
        print("Twitteando")
        img_counter += 1
##    break



