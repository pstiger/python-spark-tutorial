import smtplib
from email.mime.text import MIMEText
import datetime

if __name__ == "__main__":
    print ("In Main")
    currentDT = datetime.datetime.now();
    print ("Now is" + str(currentDT))

def sendTMOSMS():
    currentDT = datetime.datetime.now()

    msg = MIMEText("X1C Carbon In Stock! Time=" + str(currentDT))
    msg["Subject"] = "X1C Carbon in Stock!"
    msg["From"] = "stealthsun@gmail.com"
    msg["To"] = "15082452331@tmomail.net"



    print ("--- In Send TOM SMS. Before Sending Text ---")
    gmail_user = 'stealthsun@gmail.com'
    gmail_password = 'cowgirlsm'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.close()
    print ("--- In Send TOM SMS. After Sending Text ---")

