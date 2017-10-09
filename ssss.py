#!/usr/bin/env python2.7  
# tweetpic.py take a photo with the Pi camera and tweet it  
# by Alex Eames http://raspi.tv/?p=5918  
import tweepy  
from subprocess import call  
from datetime import datetime
import os
img= "3.jpg"
os fswebcam -F 


   
i = datetime.now()               #take time and date for filename  
now = i.strftime('%Y%m%d-%H%M%S')  
photo_name = now + '3.jpg'  
cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + photo_name   
call ([cmd], shell=True)         #shoot the photo  
  
# Consumer keys and access tokens, used for OAuth  
consumer_key = '
consumer_secret = '  
access_token = '
access_token_secret = '
  
# OAuth process, using the keys and tokens  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
   
# Creation of the actual interface, using authentication  
api = tweepy.API(auth)  
  
# Send the tweet with photo  
photo_path = '/home/pi/' + "3.jpg"  
status = 'Photo auto-tweet from Pi: ' + i.strftime('%Y/%m/%d %H:%M:%S')   
api.update_with_media(photo_path, status=status)  
