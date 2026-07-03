# Product Requirements Document (PRD)

## Project Name

**Smart Recruitment Agent – AI-Powered Recruitment Automation System**

---

# Project Purpose

The Smart Recruitment Agent is an end-to-end recruitment automation system developed to streamline and automate the candidate recruitment process.

The system generates demonstration candidate applications, processes incoming Gmail messages using Claude AI for free-text analysis, evaluates applicants according to predefined recruitment rules, schedules interviews using Google Calendar, sends interview invitation emails, and generates recruitment reports.

The solution demonstrates workflow automation through the integration of Python, Gmail API, Google Calendar API, Claude AI (Anthropic), OAuth 2.0 authentication, and Excel-based reporting.

The project follows a modular software architecture where each module is responsible for a dedicated stage of the recruitment workflow while maintaining full compatibility through the main application.

---

# Business Problem

Recruitment teams spend significant time performing repetitive administrative activities, including:

- Reading candidate applications.
- Evaluating applicant qualifications.
- Ranking candidates.
- Scheduling interviews.
- Sending interview invitations.
- Maintaining recruitment reports.

Manual recruitment processes increase workload, introduce delays, and may lead to inconsistent candidate evaluation and scheduling.

The Smart Recruitment Agent automates these repetitive tasks using AI-powered free-text analysis, allowing recruiters to focus on candidate selection and decision-making rather than administrative work.

---

# Project Objectives

The system aims to:

- Generate demonstration candidate applications in natural free-text format.
- Read Gmail applications automatically.
- Process only unread Gmail messages.
- Extract candidate information using Claude AI.
- Evaluate and rank candidates.
- Classify recruitment status automatically.
- Schedule interviews automatically.
- Validate Google Calendar availability before creating interview events.
- Automatically search for the next available interview slot when required.
- Schedule interviews at least seven days in advance.
- Skip Friday and Saturday during interview scheduling.
- Create Google Calendar interview events.
- Send interview invitation emails automatically.
- Generate Excel recruitment reports.
- Synchronize invitation status across recruitment reports.
- Prevent duplicate interview scheduling.
- Prevent duplicate invitation emails.
- Execute the complete recruitment workflow through the main application.
---

# Functional Requirements

The system shall provide the following functional capabilities.

---

## Candidate Management

The system shall:

- Generate candidate applications in natural free-text format.
- Read Gmail messages automatically.
- Process only unread Gmail messages.
- Ignore non-recruitment emails.
- Mark processed emails as read automatically.
- Extract structured candidate information using Claude AI.
- Calculate recruitment scores.
- Classify candidates according to predefined recruitment rules.
- Detect and remove duplicate candidates.
- Generate recruitment reports and summary statistics.

---

## Interview Management

The system shall:

- Select High Priority candidates for interviews.
- Validate Google Calendar availability before creating interview events.
- Automatically search for the next available interview slot when required.
- Schedule interviews at least seven days in advance.
- Skip Friday and Saturday during interview scheduling.
- Create interview events in Google Calendar.
- Record interview date and time.
- Update candidate scheduling information.
- Prevent duplicate interview scheduling.
- Generate interview scheduling reports.
- Send an automatic notification email when no interview slot can be scheduled.

---

## Invitation Management

The system shall:

- Send interview invitation emails automatically.
- Send invitations only to candidates with scheduled interviews.
- Record invitation status.
- Record invitation sending date and time.
- Prevent duplicate invitation emails.
- Synchronize invitation status across recruitment reports.

---

## Reporting

The system shall generate the following reports:

- gmail_candidates.xlsx
- interview_candidates.xlsx
- gmail_summary.txt

The reports shall include candidate evaluation results, interview scheduling information, invitation status, and recruitment summary statistics.

---

## Workflow Management

The system shall provide:

- Interactive main menu.
- Individual module execution.
- Complete recruitment workflow execution.
- Required file validation before execution.
- Sequential module execution.
- Runtime error handling.
- Demo Mode.
- Full Recruitment Workflow Mode.
---

# Inputs

The system requires the following inputs:

- Candidate database (Excel)
- Gmail inbox messages (unread only)
- Google Calendar
- Google OAuth 2.0 authentication
- Anthropic Claude API

---

# Outputs

The system generates:

- gmail_candidates.xlsx
- interview_candidates.xlsx
- gmail_summary.txt
- Google Calendar interview events
- Interview invitation emails
- Calendar availability validation results
- Conflict notification emails
- Recruitment summary statistics

---

# Technologies

The project was developed using the following technologies:

- Python 3.13
- Gmail API
- Google Calendar API
- Google OAuth 2.0
- Claude AI (Anthropic)
- Claude API
- Pandas
- OpenPyXL
- Google API Python Client
- Git
- GitHub

---

# System Workflow

The recruitment workflow is executed through the main application and consists of the following stages:

1. Generate demonstration candidate applications (Demo Mode).
2. Read unread recruitment emails from Gmail.
3. Extract candidate information using Claude AI.
4. Evaluate and score candidates.
5. Remove duplicate candidates.
6. Generate recruitment reports.
7. Select High Priority candidates.
8. Validate Google Calendar availability.
9. Automatically search for the next available interview slot when required.
10. Create Google Calendar interview events.
11. Generate interview scheduling reports.
12. Send interview invitation emails.
13. Synchronize invitation status across Excel reports.
14. Display workflow summary information.

The workflow preserves the modular architecture by executing each project module sequentially while maintaining compatibility between all project components.
---

# Success Criteria

The project is considered successful when it can:

- Authenticate successfully with Google APIs.
- Authenticate successfully with the Anthropic Claude API.
- Process Gmail applications automatically.
- Read only unread Gmail messages.
- Mark processed emails as read automatically.
- Extract candidate information from free-text emails using Claude AI.
- Evaluate and classify candidates according to predefined recruitment rules.
- Generate recruitment reports automatically.
- Validate Google Calendar availability before creating interview events.
- Automatically search for the next available interview slot when required.
- Schedule interviews at least seven days in advance.
- Skip Friday and Saturday during interview scheduling.
- Create Google Calendar interview events successfully.
- Send interview invitation emails automatically.
- Synchronize invitation status across recruitment reports.
- Prevent duplicate candidate processing.
- Prevent duplicate interview scheduling.
- Prevent duplicate invitation emails.
- Execute the complete recruitment workflow successfully through the main application.

---

# Final Deliverables

The completed project includes:

- Smart Recruitment Agent main application.
- Recruitment Agent with Claude AI integration.
- Fake Mail Generator with natural free-text email templates.
- Interview Scheduler with Google Calendar availability validation and automatic interview slot selection.
- Google Calendar integration.
- Gmail integration.
- Invitation Sender with Excel synchronization.
- Claude AI integration.
- Automatic interview invitation emails.
- Weekend-aware interview scheduling.
- Seven-day interview scheduling.
- Duplicate prevention mechanisms.
- Excel recruitment reporting.
- Complete project documentation.
- GitHub repository.

---

# Quality Attributes

The completed solution provides:

- Modular software architecture.
- End-to-end recruitment workflow automation.
- AI-powered candidate evaluation.
- Maintainable project structure.
- Reusable software modules.
- Reliable workflow execution.
- Automated reporting.
- Consistent recruitment processing.
- Google service integration.
- Scalable project design.
---

# Project Status

## Status

**Status:** ✅ Completed

The Smart Recruitment Agent project has been successfully designed, implemented, tested, documented, and published.

The completed solution automates the entire recruitment workflow, from candidate application generation through interview invitation delivery, while integrating Artificial Intelligence, Google services, and workflow automation into a single modular system.

---

# System Summary

The Smart Recruitment Agent performs the following end-to-end recruitment workflow:

- Generates demonstration candidate applications.
- Processes unread Gmail recruitment emails.
- Extracts structured candidate information using Claude AI.
- Evaluates and ranks candidates according to predefined recruitment rules.
- Removes duplicate candidate records.
- Generates recruitment reports.
- Validates Google Calendar availability before interview scheduling.
- Automatically searches for the next available interview slot when required.
- Creates Google Calendar interview events.
- Sends interview invitation emails automatically.
- Synchronizes invitation status across recruitment reports.
- Produces workflow summary statistics.

---

# Business Value

The Smart Recruitment Agent provides significant operational benefits by reducing manual recruitment activities and improving workflow efficiency.

The solution enables recruiters to:

- Reduce repetitive administrative work.
- Improve recruitment consistency.
- Minimize scheduling conflicts.
- Automate candidate communication.
- Improve interview scheduling efficiency.
- Centralize recruitment reporting.
- Support AI-assisted candidate processing.
- Improve overall recruitment workflow reliability.

---

# Conclusion

The Smart Recruitment Agent demonstrates the practical integration of Artificial Intelligence with modern cloud services to automate an end-to-end recruitment process.

The project combines Claude AI, Gmail API, Google Calendar API, OAuth 2.0 authentication, Excel reporting, and modular Python components into a unified recruitment automation platform.

The modular software architecture enables independent development, testing, maintenance, and future extension of each project component while preserving full workflow compatibility.

The completed solution demonstrates how AI-powered free-text analysis and workflow automation can significantly improve recruitment efficiency, reduce manual effort, and provide a scalable recruitment management solution suitable for real-world business environments.
