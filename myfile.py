#!/usr/bin/python3
import smtplib               #import smtp library
s = smtplib.SMTP('smtp.gmail.com',587)
s.hello()
s.starttls()                  #to get access to security
s.login('username','password')#login details
s.sendmail('from','to','msg') #add recievers email id abd message
s.close()
