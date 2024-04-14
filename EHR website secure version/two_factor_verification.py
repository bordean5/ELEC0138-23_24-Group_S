import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import secrets

def send_email(recipient_email, flask_app_url,code):
    sender_email = "2412705414@qq.com"
    sender_password = "htzxosplrinvdjih"  # authentication-code

    # Build MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Urgent Security Verification (2FA) Required"

    # The message body content is built in HTML format
    body = f"""\
<html>
<head>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            color: #333;
            padding: 20px;
            margin: 0;
        }}
        .container {{
            background-color: #ffffff;
            max-width: 600px;
            margin: auto;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            background-color: #007BFF;
            color: #ffffff;
            padding: 10px 20px;
            text-align: center;
            font-size: 24px;
        }}
        .content {{
            padding: 20px;
            text-align: center;
        }}
        .footer {{
            font-size: 12px;
            text-align: center;
            color: #777;
            padding: 20px;
        }}
        .button {{
            display: inline-block;
            padding: 10px 20px;
            margin: 20px 0;
            background-color: #28a745;
            color: #ffffff;
            text-decoration: none;
            font-weight: bold;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            Two-Factor Authentication (2FA)
        </div>
        <div class="content">
            <p>Dear Doctor,</p>
            <p>As part of our security measures, you are required to complete a two-factor authentication process to continue using the EHR system.</p>
            <p>Your security code is:</p>
            <h2>{code}</h2>  <!-- Replace with dynamic code generation logic -->
            <p>The code only last for 5 minutes.</p>
            <p>Please enter this code on the provided page to verify your identity.</p>
            <a href="{flask_app_url}" class="button">Verify Now</a>
            <p>If you did not request this verification, please contact our support team immediately.</p>
        </div>
        <div class="footer">
            This is an automated message, please do not reply directly to this email. For assistance, please contact our support team.
        </div>
    </div>
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


def generate_code_secure():
    # generate 6 digit 2FA CODE
    code = secrets.randbelow(1000000) + 100000
    return code



if __name__ == "__main__":
    recipient = "1304448069@qq.com"       #replace with who you want to send to
    flask_app_link = "http://127.0.0.1:5000"
    two_factor_code = generate_code_secure()
    send_email(recipient, flask_app_link,two_factor_code)

