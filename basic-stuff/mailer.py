from smtpd import SMTPServer
from smtplib import SMTP_SSL
from ssl import create_default_context

local_address = ('127.0.0.1', 1065)  # Default host and port for local enviroments
remote_address = ('127.0.0.1', 1065)

SMTPServer(local_address, remote_address)

sender_email = # The sender email
sender_password = # The sender password
receiver_email = # The receiver email
email_body = # A plain text email body

smtp_platform = 'smtp.gmail.com'
smtp_port = 465  # Default smtp port when using SSL

context = create_default_context()

with SMTP_SSL(smtp_platform, smtp_port, context=context) as server:
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, email_body)
