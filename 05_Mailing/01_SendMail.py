import pyfiglet
import sys
import os

# Go to the project root folder
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

# Now import from /requirements
from requirements import config
from requirements.gateway import GatewayClient

# Initialize gateway client
gateway = GatewayClient(
    base_url=config.GATEWAY_URL,
    username=config.GATEWAY_USERNAME,
    password=config.GATEWAY_PASSWORD
)

#Put Mail together
print(pyfiglet.figlet_format("Mailing"))
target = input("To\n")
subject = input("Subject\n")
message = input("Message\n")

# Send email via gateway
try:
    result = gateway.send_email(
        to=[target],
        subject=subject,
        html=f"<p>{message}</p>",
        from_email=config.EMAIL_FROM
    )
    print(f"Email sent to {target}")
    if result.get("email_id"):
        print(f"Email ID: {result['email_id']}")
except Exception as e:
    print(f"Error sending email: {e}")