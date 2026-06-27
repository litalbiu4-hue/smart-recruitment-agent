# Recruitment Agent Skill

## Name
Recruitment Agent

---

## Purpose
The Recruitment Agent is responsible for automatically processing candidate applications received through Gmail.
It uses Claude LLM to extract candidate information from natural free-text emails, evaluates candidates according to predefined business rules, calculates recruitment scores, classifies applicants, removes duplicate candidates, and generates recruitment reports that are used by the remaining modules of the Smart Recruitment Agent system.

---

## Responsibilities
The Recruitment Agent performs the following tasks:

* Connect to Gmail using Google OAuth 2.0.
* Read only unread candidate application emails.
* Use Claude LLM to extract candidate information from free-text emails.
* Mark emails as read after processing.
* Calculate recruitment scores.
* Classify candidates.
* Remove duplicate applications.
* Generate Excel recruitment reports.
* Generate recruitment summary reports.

---

## Inputs

* Gmail inbox messages (unread only)
* Candidate application emails (natural free-text format)
* Candidate database (Excel)
* Anthropic Claude API

---

## Processing Steps

1. Authenticate with Gmail API.
2. Read unread candidate emails only.
3. Send email content to Claude LLM for analysis.
4. Extract candidate information from free-text using Claude.
5. Mark email as read after processing.
6. Validate candidate data.
7. Calculate recruitment scores.
8. Classify recruitment status.
9. Remove duplicate candidates.
10. Generate recruitment reports.

---

## Outputs

The Recruitment Agent generates:

* gmail_candidates.xlsx
* gmail_summary.txt

These files are later used by:

* Interview Scheduler (with Calendar Conflict Detection)
* Invitation Sender (with Dual Excel Sync)
* Main Workflow

---

## Technologies

* Python 3.13
* Gmail API
* Google OAuth 2.0
* Claude AI (Anthropic)
* Anthropic Python SDK
* Pandas
* OpenPyXL

---

## Success Criteria

The module is considered successful when it:

* Authenticates successfully with Gmail.
* Reads only unread candidate emails.
* Extracts candidate information from free-text emails using Claude LLM.
* Marks emails as read after processing.
* Processes all candidates.
* Calculates recruitment scores.
* Classifies candidates correctly.
* Removes duplicate candidates.
* Generates Excel recruitment reports.

---

## Integration

The Recruitment Agent is fully integrated with:

* Interview Scheduler (with Calendar Conflict Detection and Weekend-Aware Scheduling)
* Invitation Sender (with Dual Excel Sync)
* Main Workflow Manager
* Claude AI API

It represents the first processing stage of the complete recruitment workflow.

---

## Future Enhancements

Potential future improvements include:

* Advanced CV parsing using more powerful LLM models.
* Machine Learning candidate evaluation.
* LinkedIn API integration.
* Power BI recruitment dashboard.
* Candidate recommendation engine.
* Cloud deployment.

---

## Status

**Status:** ✅ Completed

The Recruitment Agent has been fully implemented with Claude LLM integration, tested, documented, and integrated into the Smart Recruitment Agent recruitment workflow.
