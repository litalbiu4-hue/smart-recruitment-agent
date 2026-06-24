# Smart Meeting Agent

## Overview

Smart Meeting Agent is a recruitment automation system developed in Python using Gmail API, OAuth 2.0, Pandas, and Excel.

The system simulates a recruitment workflow by generating candidate applications, sending them through Gmail, reading incoming emails, extracting candidate information, scoring applicants, and generating recruitment reports automatically.

---

## Project Workflow

1. Create candidate database in Excel
2. Generate candidate application emails
3. Send applications using Gmail API
4. Read Gmail inbox automatically
5. Extract candidate information
6. Calculate candidate scores
7. Rank candidates
8. Generate Excel reports

---

## Main Components

### Gmail Integration

* OAuth 2.0 authentication
* Gmail API connection
* Inbox access
* Email sending

### Candidate Processing

* Candidate data extraction
* Candidate scoring
* Priority classification
* Recruitment analysis

### Reporting

* Excel report generation
* Candidate ranking reports
* Recruitment summaries

---

## Main Files

| File                   | Description                        |
| ---------------------- | ---------------------------------- |
| main.py                | Main recruitment workflow          |
| create_token.py        | OAuth token generation             |
| test_gmail.py          | Gmail connection testing           |
| fake_mail_generator.py | Candidate email generator          |
| recruitment_agent.py   | Candidate processing and reporting |

---

## Output Files

| File                   | Purpose                                    |
| ---------------------- | ------------------------------------------ |
| candidate_results.xlsx | Candidate evaluation results               |
| gmail_candidates.xlsx  | Candidate information extracted from Gmail |
| gmail_summary.txt      | Recruitment summary                        |
| candidates.xlsx        | Candidate source database                  |

---

## Technologies

* Python
* Gmail API
* OAuth 2.0
* Pandas
* OpenPyXL
* Google Cloud Platform

---

## Project Status

✅ Gmail API Connected

✅ OAuth Authentication Implemented

✅ Automated Candidate Email Generation

✅ Automated Inbox Processing

✅ Candidate Scoring System

✅ Excel Report Generation

---

## Future Enhancements

* AI-based candidate ranking
* Interview scheduling automation
* Power BI dashboard integration
* Advanced recruitment analytics
