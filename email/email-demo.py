import os 
import smtplib
import time 
import imghdr

from email.message import EmailMessage

EMAIL_PASSW = os.environ.get('ZOHOPASS')
EMAIL_ADDRESS = "admin@sajacosmetics.com"

msg = EmailMessage()

msg['Subject'] = 'django we\'re almost there'
msg['From'] = f"{EMAIL_ADDRESS}"
msg['To'] = 'agalmameyassine@gmail.com'
msg.set_content('django')

with open('images.png','rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_alternative("""\
        <html>
            <body>
                 <h1 style='color:red'>this is a robot</h1>
            </body>
        </html>""", subtype='html')

msg.add_attachment(file_data,maintype='image', subtype=file_type,filename=file_name)

print(f"From: {msg['From']} -->\n To: {msg['To']}")
with smtplib.SMTP_SSL('smtp.zoho.com', 110) as smtp:
   # smtp.ehlo()
   # smtp.starttls()
   # smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSW)
   # time.sleep(5) 
    smtp.send_message(msg)
    
