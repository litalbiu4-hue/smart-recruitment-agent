# Product Requirements Document (PRD)

## Project Name

**Smart Recruitment Agent – AI-Powered Recruitment Automation System**

---

## Project Purpose

The Smart Recruitment Agent is an end-to-end recruitment automation system developed to streamline and automate the candidate recruitment process.

The system simulates candidate applications, processes incoming Gmail messages, evaluates applicants according to predefined business rules, schedules interviews in Google Calendar, sends interview invitation emails, and generates recruitment reports.

The project demonstrates workflow automation through the integration of multiple Google services and Python-based business logic.

---

## Business Problem

Recruitment teams spend a significant amount of time performing repetitive administrative tasks such as:

* Reading candidate applications.
* Evaluating applicant qualifications.
* Ranking candidates.
* Scheduling interviews.
* Sending interview invitations.
* Maintaining recruitment reports.

Manual processing increases workload, introduces delays, and may result in inconsistent decision-making.

The Smart Recruitment Agent automates these repetitive tasks, allowing recruiters to focus on candidate selection rather than administrative work.

---

## Project Objectives

The system aims to:

* Generate demonstration candidate applications.
* Read Gmail applications automatically.
* Extract candidate information.
* Evaluate and rank candidates.
* Classify recruitment status.
* Schedule interviews automatically.
* Create Google Calendar interview events.
* Send interview invitation emails automatically.
* Generate Excel recruitment reports.
* Prevent duplicate interviews.
* Prevent duplicate invitation emails.
* Execute the complete recruitment workflow through a single application.

---

## Functional Requirements

The system shall:

### Candidate Management

* Generate candidate applications.
* Read Gmail messages.
* Extract candidate information.
* Calculate recruitment scores.
* Classify candidates into recruitment categories.

---

### Interview Management

* Select High Priority candidates.
* Schedule interviews automatically.
* Create Google Calendar events.
* Record interview information.

---

### Invitation Management

* Send interview invitation emails.
* Update invitation status.
* Record invitation dates.
* Prevent duplicate invitations.

---

### Reporting

Generate:

* gmail_candidates.xlsx
* interview_candidates.xlsx
* gmail_summary.txt

---

### Workflow Management

The system shall provide:

* Interactive main menu.
* Individual module execution.
* Complete workflow execution.
* Required file validation.
* Runtime error handling.

---

## Inputs

* Candidate database (Excel)
* Gmail inbox messages
* Google Calendar
* Google OAuth authentication

---

## Outputs

The system generates:

* Candidate ranking report
* Interview report
* Recruitment summary
* Google Calendar events
* Interview invitation emails
* Excel recruitment reports

---

## Technologies

* Python 3.13
* Gmail API
* Google Calendar API
* Google OAuth 2.0
* Pandas
* OpenPyXL
* Google API Python Client
* GitHub

---

## Success Criteria

The project is considered successful when it can:

* Authenticate successfully with Google APIs.
* Process Gmail applications automatically.
* Evaluate and classify candidates.
* Generate recruitment reports.
* Schedule interviews automatically.
* Create Google Calendar events.
* Send interview invitations automatically.
* Prevent duplicate interview scheduling.
* Prevent duplicate invitation emails.
* Execute the complete workflow successfully through the Main application.

---

## Final Deliverables

The completed project includes:

* Recruitment Agent
* Fake Mail Generator
* Interview Scheduler
* Invitation Sender
* Main Workflow Manager
* Gmail Integration
* Google Calendar Integration
* Excel Reporting
* Complete Project Documentation

---

## Project Status

**Status:** ✅ Completed

The Smart Recruitment Agent project has been fully implemented, tested, documented, and published.

The final solution provides a complete recruitment automation workflow from candidate application generation through interview invitation delivery.
