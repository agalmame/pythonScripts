import smtplib, ssl
import imaplib
port = 993  # For starttls
smtp_server = "imap.gmail.com"
sender_email = "agalmameyassine@gmail.com"
receiver_email = "agalmameyassine@gmail.com"
password = 'qbtspyuxylqkspar'
message = """\
        Subject: Hi there

        This message is sent from Python."""

server = imaplib.IMAP4_SSL(smtp_server, port)
server.login(sender_email, password)
server.select('INBOX')
server.send('hellooo')
server.logout()
