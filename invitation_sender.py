import base64
import os

import pandas as pd

from datetime import datetime

from email.mime.text import MIMEText

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send"
]

print("Invitation Sender Started\n")

# =====================================
# AUTHENTICATION
# =====================================

creds = Credentials.from_authorized_user_file(
    "token.json",
    SCOPES
)

gmail_service = build(
    "gmail",
    "v1",
    credentials=creds
)

# =====================================
# READ EXCEL
# =====================================

df = pd.read_excel(
    "gmail_candidates.xlsx",
    dtype=str
)

df = df.fillna("")

# =====================================
# CREATE REQUIRED COLUMNS
# =====================================

required_columns = [
    "Invitation_Status",
    "Invitation_Sent_Date"
]

for col in required_columns:

    if col not in df.columns:

        df[col] = ""

    df[col] = (
        df[col]
        .fillna("")
        .astype(str)
    )

# =====================================
# SUMMARY COUNTERS
# =====================================

total_candidates = len(df)

sent_count = 0

skipped_count = 0

error_count = 0

# =====================================
# SEND INVITATIONS
# =====================================

for index, row in df.iterrows():

    calendar_status = str(
        df.at[index, "Calendar_Status"]
    ).strip()

    invitation_status = str(
        df.at[index, "Invitation_Status"]
    ).strip()

    candidate_name = str(
        df.at[index, "Candidate_Name"]
    )

    candidate_email = str(
        df.at[index, "Email"]
    )

    position = str(
        df.at[index, "Position"]
    )

    interview_date = str(
        df.at[index, "Interview_Date"]
    )

    interview_time = str(
        df.at[index, "Interview_Time"]
    )

    # =====================================
    # ONLY SCHEDULED CANDIDATES
    # =====================================

    if calendar_status != "Scheduled":

        continue

    # =====================================
    # PREVENT DUPLICATE EMAILS
    # =====================================

    if invitation_status == "Sent":

        skipped_count += 1

        print(
            f"Skipping invitation for "
            f"{candidate_name}"
        )

        continue

    subject = "Interview Invitation"

    body = f"""Hello {candidate_name},

Congratulations.

Your interview has been scheduled.

Position: {position}

Interview Date:
{interview_date}

Interview Time:
{interview_time}

Please arrive 10 minutes before the interview.

Good luck.

HR Department
"""

    message = MIMEText(body)

    message["To"] = candidate_email

    message["Subject"] = subject

    raw_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    try:

        gmail_service.users().messages().send(

            userId="me",

            body={
                "raw": raw_message
            }

        ).execute()

        sent_count += 1

        df.at[
            index,
            "Invitation_Status"
        ] = "Sent"

        df.at[
            index,
            "Invitation_Sent_Date"
        ] = datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )

        print(
            f"Invitation sent to "
            f"{candidate_name}"
        )

    except Exception as e:

        error_count += 1

        print(
            f"Error sending invitation "
            f"to {candidate_name}"
        )

        print(e)
# =====================================
# SAVE UPDATED GMAIL CANDIDATES
# =====================================

df.to_excel(
    "gmail_candidates.xlsx",
    index=False
)

# =====================================
# SYNC INVITATION STATUS TO
# INTERVIEW CANDIDATES FILE
# =====================================

if os.path.exists("interview_candidates.xlsx"):

    df_interview = pd.read_excel(
        "interview_candidates.xlsx",
        dtype=str
    )

    df_interview = df_interview.fillna("")

    if "Invitation_Status" not in df_interview.columns:
        df_interview["Invitation_Status"] = ""

    if "Invitation_Sent_Date" not in df_interview.columns:
        df_interview["Invitation_Sent_Date"] = ""

    for idx, irow in df_interview.iterrows():

        email = str(irow.get("Email", "")).strip()

        match = df[df["Email"].str.strip() == email]

        if not match.empty:

            df_interview.at[
                idx,
                "Invitation_Status"
            ] = match.iloc[0]["Invitation_Status"]

            df_interview.at[
                idx,
                "Invitation_Sent_Date"
            ] = match.iloc[0]["Invitation_Sent_Date"]

    df_interview.to_excel(
        "interview_candidates.xlsx",
        index=False
    )

# =====================================
# PRINT SUMMARY
# =====================================

print()

print("========================")
print("Invitation Sender Completed")
print("========================")

print(
    f"Total Candidates: "
    f"{total_candidates}"
)

print(
    f"Invitations Sent: "
    f"{sent_count}"
)

print(
    f"Skipped Invitations: "
    f"{skipped_count}"
)

print(
    f"Errors: "
    f"{error_count}"
)

print()

print("Updated Files")

print(
    "- gmail_candidates.xlsx"
)

if os.path.exists("interview_candidates.xlsx"):

    print(
        "- interview_candidates.xlsx"
    )

print()

print("Invitation Sender Finished Successfully")
