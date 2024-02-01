import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email = "yourphishingemail@gmail.com"
sender_password = "12345"
recipient_email = "pantechdivya@gmail.com"
subject = "important account date"
message = """
Dear User,
we have noticed some suspicious activity on your account.
Please click the link below to update your account information.
[Malicious Link] - hhtp://fake-phishing-website.com

Thank you,
Your Bank
"""
smtp_server="smtp.gmail.com"
smtp_port = 587
try:
    server = smtplib.SMTP(smtp_server,smtp_port)
    server.startls()
    server.login(sender_email,sender_password)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message,'plain')

    server.sendmail(sender_email,recipient_email,msg.as_string())
               server.quit()

               print("phishing email sent successfully")
except Exception as e:
               print(f"Error:{str(e)}")
