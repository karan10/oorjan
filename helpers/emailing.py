import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from oorjan.settings import EMAIL_USERNAME as username, EMAIL_PASSWORD as password



def send_email( send_to, text, subject, is_html = False ):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = "Report <" + username +  ">"
    msg['To'] = ','.join ( send_to )
    if is_html == True :
        msg.attach( MIMEText(text, 'html') )
    else :
        msg.attach( MIMEText(text, 'plain') )

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls() 
    server.login(username, password)
    server.sendmail('From: Report <' + username + '>', send_to, msg.as_string() )
    server.quit()