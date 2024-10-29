from api import fetchmeme
from mail import send_mail

HTML = """
    <html>
        <head></head>
        <body>
            <p>hey this meme is for you 😁"</p>
            <img src="{}">
        </body>
    </html>
"""


while True:
    action = input("""
        What do you want to Do? 
        1. Share a meme with a friend
        2. Quit the App.
    """)

    if action == "1":
        meme_name = input("\nName of the meme you want to send\n")
        meme = fetchmeme(meme_name)
        if meme:
            friend_email = input("\nEnter email of your friend\n")
            send_mail(friend_email, subject="MEME from your friend", body=HTML.format(meme))
            print("meme shared successfully")
    elif action == "2": 
        print("\nYou are Quitting App\n")
        break