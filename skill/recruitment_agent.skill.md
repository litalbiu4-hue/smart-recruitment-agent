# Recruitment Agent Skill

## Name

Recruitment Agent

## Purpose

Automatically process candidate applications received through Gmail, evaluate candidates, and generate recruitment reports.

## Inputs

* Gmail inbox messages
* Candidate application emails
* Candidate database (Excel)

## Processing Steps

1. Connect to Gmail using OAuth 2.0
2. Read incoming candidate emails
3. Extract candidate information
4. Calculate candidate score
5. Rank candidates by suitability
6. Generate Excel reports

## Outputs

* candidate_results.xlsx
* gmail_candidates.xlsx
* gmail_summary.txt

## Technologies

* Python
* Gmail API
* OAuth 2.0
* Pandas
* OpenPyXL

## Success Criteria

* Successful Gmail authentication
* Email processing completed
* Candidate ranking generated
* Excel reports created

## Future Enhancements

* AI-based candidate scoring
* Interview scheduling integration
* Power BI dashboard integration
* Automated recruitment recommendations
