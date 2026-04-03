import smtplib

your_email = input("Enter your e-mail address: ");
password = input("Enter your password: ")
recipient_email = input("Enter the email of the receiver: ");
message = input("Enter the message: ");

def send_email(your_email, password, recipient_email, message):
    '''
    :param your_email: email address for the gmail account you want to send from
    :type your_email: string
    :param password: password for the gmail account you want to send from
    :type password: string
    :param recipient_email: recipient's email address
    :type recipient_email: string
    :param message: the body of the email you want to send
    :type message: string
    '''
    host = "smtp.mail.yahoo.com"
    port = 587

    server = smtplib.SMTP(host, port)
    server.starttls()   #initiate TLS mode from gmail server

    server.login(your_email, password)

    server.sendmail(your_email, recipient_email, message)

    server.close()

send_email(your_email, password, recipient_email, message);