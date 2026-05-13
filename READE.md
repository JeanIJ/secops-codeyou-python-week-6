Incident Triage Tracker
A small Python program that reads raw security alerts from a file, converts them into structured objects, classifies them by severity, and writes a clean summary report.
Built for Code:You SecOps Python Assignment 6.
What It Does
Reads alerts.txt, a comma separated file of security events
Parses each line into an Alert object using a simple Python class
Classifies each alert by severity (HIGH, MEDIUM, LOW)
Determines if the indicator is an internal IP, external IP, or N/A
Prints a clean summary to the terminal
Writes the same summary to incident_summary.txt
Files
incident_tracker.py: Main script
alerts.txt: Input data with 5 sample security alerts
incident_summary.txt: Output report generated automatically
How to Run
Type this command in your terminal:
plain
Copy
python3 incident_tracker.py
Press Enter when asked for a filter to show all alerts. Or type HIGH, MEDIUM, or LOW to filter.
Sample Output
plain
Copy
Loaded 5 alerts.

Incident Triage Summary
========================================
2026-01-03 [LOW] login_failure on bob -> 8.8.8.8
   Classification: external

2026-01-03 [LOW] login_success on alice -> 192.168.1.25
   Classification: internal

2026-01-03 [HIGH] file_hash_detected on workstation-7 -> 275a021bbfb6483e2f3b2ed34a59dcdf57f7e3c2efb8fe2bc5e756e508d2f5a9
   Classification: N/A

2026-01-03 [MEDIUM] dns_query on finance-laptop -> ms-secure-login.net
   Classification: N/A

2026-01-03 [MEDIUM] port_scan on web-server-1 -> 185.220.101.6
   Classification: external

Total alerts processed: 5
HIGH:   1
MEDIUM: 2
LOW:    2
Internal: 1 | External: 2 | N/A: 2

Report saved to incident_summary.txts
Concepts Practiced
Python Classes and Objects: Alert class bundles data and behavior
init: constructor that initializes each alert
str: clean string representation for printing
Enum: AlertType prevents typos and centralizes valid alert types
File I/O: reading alerts.txt and writing incident_summary.txt
Conditionals: severity and classification logic
Loops and Lists: processing and counting multiple alerts
Challenges Completed
A: Internal vs External. Classifies indicators as internal, external, or N/A based on IP patterns
B: str Method. Produces clean human readable output when printing an alert
Reflection
Using a class made it easier to bundle each alert's data and behavior together, so I could call alert.severity() instead of writing separate functions for every alert. The hardest part was understanding why self.alert_type.value was needed in str because enums store a label and a string value separately. To make this better, I would add error handling for malformed lines in alerts.txt so the program does not crash if a line is missing a comma.