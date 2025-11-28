import pyfiglet
import resend
import sys
import os

# Go to the project root folder
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Now import from /requirements
from requirements import apikeys

#Put Mail together
print(f"{pyfiglet.figlet_format("Send Mail")}\n\n")
target = input("To: ")
subject = input("Subject: ")
print("Message: ")
message = input()
resend.api_key = apikeys.apikey_mail
params: resend.Emails.SendParams = {
  "from": f"Comandline <{apikeys.email}>",
  "to": [target],
  "subject": subject,
  "html": f"<p>{message}</p>"
}

email = resend.Emails.send(params)
print(F"Email sent to {target}")