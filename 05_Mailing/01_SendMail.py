import pyfiglet
import resend
from apikey import *

#Put Mail together
print(f"{pyfiglet.figlet_format("Send Mail")}\n\n")
target = input("To: ")
subject = input("Subject: ")
print("Message: \n")
message = input()
resend.api_key = apikey
params: resend.Emails.SendParams = {
  "from": f"Comandline <{email}>",
  "to": [target],
  "subject": subject,
  "html": f"<p>{message}</p>"
}

email = resend.Emails.send(params)
print(F"Email sent to {target}")