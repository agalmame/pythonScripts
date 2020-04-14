import os 
import smtplib
import time 
import imghdr

from email.message import EmailMessage

EMAIL_PASSW = os.environ.get('PASSW')
EMAIL_ADDRESS = os.environ.get('EUSER')

msg = EmailMessage()

msg['Subject'] = 'Grab dinner this weekend?'
msg['From'] = 'EMAIL_ADDRESS'
msg['To'] = 'yassine-boss4@hotmail.fr'
msg.set_content('how about dinner at 5pm this monday')

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

print(f'password:{EMAIL_PASSW} \n address:{EMAIL_ADDRESS}')
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
   # smtp.ehlo()
   # smtp.starttls()
   # smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSW)
   # time.sleep(5) 
    smtp.send_message(msg)
    
