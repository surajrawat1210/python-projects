
#      **OTP VARIFICATION ON EMAIL USING PYTHON:-**
##### OTP varification is a process in which user verify itself through otp before completing any payment or registration or when we forget password. .

> ###### we are creating a program that can send otp and verify the otp whether it is correct or not.
>- Generate otp.
>- Store otp as a message.
>- Take receiver email id as input.
>- Send message to the receiver email id
>- Write otp send on receiver email


> # Generate OTP :-
```sh
OTP=str(random.randint(100000,999999))
otp = OTP + " is your OTP"
msg= otp
```
### Python library we need to import  for our project :-
```bash
import math
import random
import smtplib
```
##### before we go ahead, you need to have your Google app password to be able to send emails using your Gmail account.
>- Go to your Google Account.
>-- Select Security.

>- Under "Signing in to Google," select App Passwords. You may need to sign in. If
you don’t have this option, it might be because:
>-- 2-Step Verification is not set up for your account.
>- 2-Step Verification is only set up for security keys.
>- Your account is through work, school, or other organization.
>- You turned on Advanced Protection.
>- At the bottom, choose Select app and choose the app you using and then Select device and choose the device you’re using and then Generate.
>- Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
>- Tap Done.

```sh 
# create smtp session 
j= smtplib.SMTP("smtp.gmail.com" , 587)  # 587 is a port number
# start TLS for E-mail security 
j.starttls()
# Log in to your gmail account
j.login("sender_email" , "sender_email_password")
```

> **Also before executing this code please make sure that you have replaced the sender_email by your own email id, sender_email_password by password of that email id,**
---
#### ``THANKYOU FOR WATCHING:-``

     
