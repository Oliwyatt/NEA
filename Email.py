import smtplib, ssl

def SendEmail(Email, *args):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "@gmail.com"
    password = ""

    Message = ""

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, Email, Message)