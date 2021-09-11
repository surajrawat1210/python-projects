import math
import random
import smtplib
OTP=str(random.randint(100000,999999))
otp = OTP + " is your OTP"
msg= otp
#create smtp session
j =smtplib.SMTP('smtp.gmail.com', 587)
#start tls for security
j.starttls()
j.login("your email addresss ","app password(16 digit yellow color code)")

emailid = input("Enter your email: ")
j.sendmail('Generating otp',emailid,msg)
# s.sendmail("surajrawat9817@gmail.com",emailid,,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
