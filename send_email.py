import smtplib, ssl
import os
import st

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = st.username
    password = st.password
    receiver = st.receiver
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
