import smtplib

def send_email(your_email, password, recipient_email):
    '''
    :param your_email: email address for the gmail account you want to send from
    :type your_email: string
    :param password: password for the gmail account you want to send from
    :type password: string
    :param recipient_email: recipient's email address
    :type recipient_email: string
    '''
    host = "smtp.gmail.com"
    port = 587

    server = smtplib.SMTP(host, port)
    server.starttls()   #initiate TLS mode from gmail server

    server.login(your_email, password)

    message = "Testing automating email!"

    server.sendmail(your_email, recipient_email, message)

    server.close()
