import smtplib

def send_email(user_name, password, recipient_email):
    host = "smtp.gmail.com"
    port = 587

    server = smtplib.SMTP(host, port)
    server.starttls()   #initiate TLS mode from gmail server

    server.login(user_name, password)

    from_email = user_name
    message = "Testing automating email!"

    server.sendmail(from_email, recipient_email, message)

    server.close()

