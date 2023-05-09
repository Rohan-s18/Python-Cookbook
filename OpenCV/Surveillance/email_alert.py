
#  Imports
import smtplib

def send_email_alert():

    #These lines are for the email 
    user = "" # replace with your CWRU email address
    pwd = "" # replace with your CWRU password
    recipient = "" # replace with the recipient's email address

    subject = 'Intruder Alert Email' 
    text = 'An intruder has been detected in the warehouse facility' 

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (user, recipient, subject, text)

    try:
        # Email server
        emserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        emserver.ehlo()

        #Logging in
        emserver.login(user, pwd)

        #Sending email
        emserver.sendmail(user, recipient, email_text)
        emserver.close()
        print("Email Sent")
    except Exception as e:
        print("Email wasn't sent due to:", e)



# Main Function for testing
def main():

    send_email_alert()


if __name__ == "__main__":
    main()