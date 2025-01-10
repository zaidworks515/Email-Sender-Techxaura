import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import sender, password
import time


def email_sender(company_name, website, emails_list, problems, content_message):
    email = None
    try:
        msg = MIMEMultipart()
        msg.set_unixfrom('author')
        msg['From'] = sender 
        msg['To'] = email 
        msg['Subject'] = problems
        message = content_message
        msg.attach(MIMEText(message))

        mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
        mailserver.ehlo()  
        mailserver.login(sender, password)

        for email in emails_list:
            try:
                email = email.lstrip()
                mailserver.sendmail(sender, email, msg.as_string())
                print(f"Email sent successfully to {email}")
                print(f"==============================================")
                time.sleep(2)
            except Exception as e:
                print(f"Failed to send email to {email}: {e}")
        
        mailserver.quit()
        
        return 'success'

    except smtplib.SMTPServerDisconnected as e:
        print(f"SMTPServerDisconnected: {e}")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTPAuthenticationError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
