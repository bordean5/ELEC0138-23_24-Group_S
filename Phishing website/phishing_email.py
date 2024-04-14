import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient_email, flask_app_url):
    sender_email = "2412705414@qq.com"
    sender_password = "kiewqlxoayeqdiha"  # authentication-code

    # Build MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Important: Upgrade Required for EHR System Stability"

    # The message body content is built in HTML format
    body = f"""\
<html>
<head></head>
<body>
<p>Dear Doctors,</p>
<p>I hope this message finds you well. We have received several reports from colleagues experiencing slowdowns, unresponsiveness, and other issues while using the EHR system. To ensure the stability and functionality of our system, an upgrade is necessary.</p>
<p>Please ensure that you complete the upgrade by clicking on the link below before you leave today. This is crucial for maintaining our service quality and your seamless experience.</p>
<p><a href="{flask_app_url}">Click here to upgrade now</a></p>
<p>Thank you for your cooperation and prompt attention to this matter.</p>
<p>Best regards,</p>
<p>Ming Li<br>
EHR System Administrator</p>
</body>
</html>
"""

    # Append the message body to the email
    msg.attach(MIMEText(body, 'html'))

    # send email
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)  # use SSL
    try:
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    recipient = "2412705414@qq.com"  #the recipient of the phishing email
    flask_app_link = "http://127.0.0.1:5000"
    send_email(recipient, flask_app_link)
