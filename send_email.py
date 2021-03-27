import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import os
from dotenv import load_dotenv  # pip install python-dotenv


# Encoding email headers
# https://docs.python.org/3/library/email.header.html


def send_mail_yahoo(subject, msg_body):
    # SEND FROM YAHOO ACCOUNT

    load_dotenv("E:/Python/EnvironmentVariables/.env")
    YAHOO_SENDER = os.getenv("SMTP_YAHOO_SENDER")
    YAHOO_USERNAME = os.getenv("SMTP_YAHOO_USERNAME")
    YAHOO_EMAIL = os.getenv("SMTP_YAHOO_EMAIL")
    YAHOO_PASSWORD = os.getenv("SMTP_YAHOO_PASSWORD")
    YAHOO_RECIPIENT = os.getenv("SMTP_YAHOO_RECIPIENT")

    # This message works 27/03/2021

    # Compile email headers
    # Subject is encoded to allow non-ASCII characters (RFC2047)
    message = MIMEMultipart()
    message["From"] = f"\"{YAHOO_SENDER}\" <{YAHOO_EMAIL}>"
    message["To"] = f"{YAHOO_RECIPIENT}"
    message["Subject"] = Header(s=subject, charset="utf-8")
    # message["Bcc"] = f"{YAHOO_RECIPIENT}"

    # Add the text message
    msg_text = MIMEText(_text=f"{msg_body}", _subtype="plain", _charset="utf-8")
    message.attach(msg_text)

    # # Add an image as attachment
    # with open('./images/boxplot.png', 'rb') as file:
    #     img = MIMEImage(file.read())
    #     img.add_header('Content-Disposition', 'attachment', filename="boxplot.png")
    #     message.attach(img)

    # print(message)

    # Send the email
    with smtplib.SMTP(host="smtp.mail.yahoo.co.uk", port=587) as connection:
        # Secure the connection
        connection.starttls()
        connection.login(user=YAHOO_USERNAME, password=YAHOO_PASSWORD)
        connection.sendmail(from_addr=YAHOO_EMAIL, to_addrs=YAHOO_RECIPIENT, msg=message.as_string())


def send_mail_plusnet(subject, msg_body):
    # SEND FROM PLUSNET ACCOUNT

    load_dotenv("E:/Python/EnvironmentVariables/.env")
    PLUS_SENDER = os.getenv("SMTP_PLUS_SENDER")
    PLUS_USERNAME = os.getenv("SMTP_PLUS_USERNAME")
    PLUS_EMAIL = os.getenv("SMTP_PLUS_EMAIL")
    PLUS_PASSWORD = os.getenv("SMTP_PLUS_PASSWORD")
    PLUS_RECIPIENT = os.getenv("SMTP_PLUS_RECIPIENT")

    # Compile email headers
    # Subject is encoded to allow non-ASCII characters (RFC2047)
    message = MIMEMultipart()
    message["From"] = f"\"{PLUS_SENDER}\" <{PLUS_EMAIL}>"
    message["To"] = f"{PLUS_RECIPIENT}"
    message["Subject"] = Header(s=subject, charset="utf-8")
    # message["Bcc"] = f"{PLUS_RECIPIENT}"

    # Add the text message
    msg_text = MIMEText(_text=f"{msg_body}", _subtype="plain", _charset="utf-8")
    message.attach(msg_text)

    # # Add an image as attachment
    # with open('./images/boxplot.png', 'rb') as file:
    #     img = MIMEImage(file.read())
    #     img.add_header('Content-Disposition', 'attachment', filename="boxplot.png")
    #     message.attach(img)

    # print(message)

    # Send the email
    with smtplib.SMTP("relay.plus.net") as connection:
        # Secure the connection
        connection.starttls()
        connection.login(user=PLUS_USERNAME, password=PLUS_PASSWORD)
        connection.sendmail(from_addr=PLUS_EMAIL, to_addrs=PLUS_RECIPIENT, msg=message)


def send_mail_gmail(subject, msg_body):
    # SEND FROM GMAIL ACCOUNT

    load_dotenv("E:/Python/EnvironmentVariables/.env")
    GMAIL_SENDER = os.getenv("SMTP_GMAIL_SENDER")
    GMAIL_USERNAME = os.getenv("SMTP_GMAIL_USERNAME")
    GMAIL_EMAIL = os.getenv("SMTP_GMAIL_EMAIL")
    GMAIL_PASSWORD = os.getenv("SMTP_GMAIL_PASSWORD")
    GMAIL_RECIPIENT = os.getenv("SMTP_GMAIL_RECIPIENT")

    # # This doesn't work 26/03/2021
    #
    # # Compile email headers
    # # Subject is encoded to allow non-ASCII characters (RFC2047)
    # message = MIMEMultipart()
    # print(message)
    # message["From"] = f"\"{GMAIL_SENDER}\" <{GMAIL_EMAIL}>"
    # print(message)
    # message["To"] = f"{GMAIL_RECIPIENT}"
    # print(message)
    # message["Subject"] = Header(s=subject, charset="utf-8")
    # print(message)
    # # message["Bcc"] = f"{GMAIL_RECIPIENT}"
    #
    # # Add the text message
    # msg_text = MIMEText(_text=f"{msg_body}", _subtype="plain", _charset="utf-8")
    # message.attach(msg_text)
    #
    # # Content-Type: multipart/mixed; boundary="===============4573739701760715565=="
    # # MIME-Version: 1.0
    # # From: "Python" <jwmp5051@gmail.com>
    # # To: j_patmore@yahoo.co.uk
    # # Subject: =?utf-8?q?Message_from_Web-form?=
    # #
    # # --===============4573739701760715565==
    # # Content-Type: text/plain; charset="utf-8"
    # # MIME-Version: 1.0
    # # Content-Transfer-Encoding: base64
    # #
    # # TmFtZTogYmVydGhhCkVtYWlsOiBiQGIuY29tClBob25lOiAKTWVzc2FnZTogCml1ZWRna2pucXcz
    # # bW5oYiANCnNrZGNqbiBhZXJvaWhmDQp2ZCxtbmtkZnY=
    # #
    # # --===============4573739701760715565==--
    #
    # # # Add an image as attachment
    # # with open('./images/boxplot.png', 'rb') as file:
    # #     img = MIMEImage(file.read())
    # #     img.add_header('Content-Disposition', 'attachment', filename="boxplot.png")
    # #     message.attach(img)

    # This simple message works 26/03/2021

    message = f"From: \"{GMAIL_SENDER}\" <{GMAIL_EMAIL}>\n" \
              f"To: {GMAIL_RECIPIENT}\n" \
              f"Subject: {subject}\n\n" \
              f"{msg_body}".encode("utf-8")

    print(message)

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_USERNAME, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=GMAIL_EMAIL, to_addrs=GMAIL_RECIPIENT, msg=message)
