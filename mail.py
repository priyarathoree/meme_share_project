import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_MAIL = 'youremail@gmail.com'
SENDER_PASSWORD = "xxxx xxxx xxxx xxxx"

def send_mail(friend_mail, subject="Meme from a friend", body=""):
    msg = MIMEMultipart()
    msg['From'] = SENDER_MAIL
    msg['To'] = friend_mail
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    try:
        # Set up the server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SENDER_MAIL, SENDER_PASSWORD)  # Login to the email account
            server.sendmail(SENDER_MAIL, friend_mail, msg.as_string())  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

