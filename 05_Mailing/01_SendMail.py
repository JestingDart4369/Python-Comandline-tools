import pyfiglet
import resend
import sys
import os

# Go to the project root folder
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Now import from /requirements
from requirements import apikey

#Put Mail together
print(pyfiglet.figlet_format("Mailing"))
target = input("To\n")
subject = input("Subject\n")
message = input("Message\n")
resend.api_key = apikey.apikey_mail
params: resend.Emails.SendParams = {
  "from": f"Comandline <{apikey.email}>",
  "to": [target],
  "subject": subject,
  "html": f"<p>{message}</p>"
}

email = resend.Emails.send(params)
print(F"Email sent to {target}")