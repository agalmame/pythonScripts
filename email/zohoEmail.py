import smtplib
from email.mime.text import MIMEText

# Define to/from
sender = 'agalmameyassine@gmail.com'
recipient = 'oussamazouaki4@gmail.com'

# Create message
msg = MIMEText("Message text")
msg['Subject'] = "Sent from python"
msg['From'] = sender
msg['To'] = recipient

# Create server object with SSL option
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# Perform operations via server
server.login('agalmameyassine@gmail.com', 'qbtspyuxylqkspar')
server.sendmail(sender, [recipient], msg.as_string())
server.quit()
 
