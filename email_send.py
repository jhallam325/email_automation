import smtplib

def sendEmail():
    host = "smtp.gmail.com"
    port = 587

    server = smtplib.SMTP(host, port)
    server.starttls()   #initiate connection to gmail server

    user_name = "user_name"
    password = "password"

    server.login(user_name, password)

    from_email = "sender_email"
    to_email = "recipient_email"
    message = "Testing automating email!"

    server.sendmail(from_email, to_email, message)

    server.close()

