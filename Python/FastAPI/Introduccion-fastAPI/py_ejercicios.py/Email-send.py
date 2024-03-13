import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

your_email = '0humor23@gmail.com'
your_pssrd = 'rujn rkqw vdrj kyrr'

recipent = 'juanfrallamojajavier@gmail.com'
message = MIMEMultipart()
message['From'] = your_email
message['To'] = recipent
message['Subject'] = 'Email de Prueba'

body = 'La aplicacion funciona correctamente'
message.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(your_email, your_pssrd)

smtp_server.sendmail(your_email, recipent, message.as_string())
smtp_server.quit()
print('Email enviado correctamente')