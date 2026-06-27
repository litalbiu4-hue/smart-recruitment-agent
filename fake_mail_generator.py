import pandas as pd
import base64
import random

from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send"
]

print("Starting Fake Mail Generator")

# Authentication
creds = Credentials.from_authorized_user_file(
    "token.json",
    SCOPES
)

gmail_service = build(
    "gmail",
    "v1",
    credentials=creds
)

# Read candidates
df = pd.read_excel("candidates.xlsx")

print(f"Found {len(df)} candidates")

sent_count = 0

# Email templates for natural free-text emails
def generate_email_body(
    candidate_name,
    candidate_email,
    position,
    region,
    experience,
    education,
    skills
):

    templates = [

        f"""Hello,

My name is {candidate_name} and I am writing to express my interest in the {position} position.

I have {experience} years of experience in the field and hold a {education} degree.
I am based in the {region} region.

My key skills include {skills}.

I believe my background makes me a strong candidate for this role.
I would welcome the opportunity to discuss how I can contribute to your team.

Please feel free to contact me at {candidate_email}.

Best regards,
{candidate_name}""",

        f"""To Whom It May Concern,

I came across the opening for {position} and would like to apply.

A bit about me:
- Name: {candidate_name}
- Location: {region}
- Education: {education}
- Years of Experience: {experience}
- Skills: {skills}

You can reach me at {candidate_email}.

Thank you for your consideration.

Sincerely,
{candidate_name}""",

        f"""Hi,

I'm {candidate_name}, currently based in {region}.
I'm very interested in the {position} role you have available.

I bring {experience} years of hands-on experience and a {education} degree.
My technical skills cover {skills}.

I'm excited about the possibility of joining your team.
Please contact me at {candidate_email} for any further information.

Warm regards,
{candidate_name}""",

        f"""Dear Hiring Manager,

Please consider my application for the {position} position.

I have been working in this field for {experience} years.
I completed my {education} and have developed strong expertise in {skills}.
I am located in {region}.

I am confident that my experience and skills align well with your requirements.

Looking forward to hearing from you.

Contact: {candidate_email}

Regards,
{candidate_name}"""

    ]

    return random.choice(templates)
# Send emails
for _, row in df.iterrows():

    candidate_name = str(row["Full_Name"])
    candidate_email = str(row["Email"])
    position = str(row["Position"])
    region = str(row["Region"])
    experience = str(row["Experience_Years"])
    education = str(row["Education"])
    skills = str(row["Skills"])

    subject_templates = [
        f"Application for {position} Position",
        f"Job Application – {position}",
        f"Applying for {position} Role",
        f"Interest in {position} Opening",
        f"Candidate Application: {position}"
    ]

    subject = random.choice(subject_templates)

    body = generate_email_body(
        candidate_name,
        candidate_email,
        position,
        region,
        experience,
        education,
        skills
    )

    message = MIMEText(body)

    message["to"] = "litalbiu4@gmail.com"
    message["subject"] = subject

    raw_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    gmail_service.users().messages().send(
        userId="me",
        body={"raw": raw_message}
    ).execute()

    sent_count += 1

    print(f"Sent {sent_count}: {candidate_name}")

print("\n========================")
print("PROCESS COMPLETED")
print("========================")
print(f"Emails Sent: {sent_count}")
