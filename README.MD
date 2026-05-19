# EMAIL AUTOMATION ENGINE V1

A Python-based automation system that reads sample email files, classifies them using keyword rules, routes them into category folders, and prints execution summaries.

---

# Features

- Reads sample email files from an inbox folder
- Classifies emails using keyword-based rules
- Automatically creates category folders
- Routes emails into matching folders
- Handles unknown classifications safely
- Prints processing summaries
- Includes basic feedback/error handling
- Records persistent activity logs

---

# Project Structure

```text
EMAIL_AUTOMATION_ENGINE_V1/
│
├── core/
│   ├── __init__.py
│   ├── inbox_reader.py
│   ├── email_classifier.py
│   ├── email_router.py
│   └── logger.py
│
├── sample_inbox/
│
├── organized_emails/
│   ├── urgent/
│   ├── finance/
│   ├── work/
│   ├── promotions/
│   ├── personal/
│   └── others/
│
├── logs/
│   └── activity_logs.txt
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── pseudocode.txt
```

---

# System Flow

```text
sample_inbox
↓
InboxReader
↓
EmailClassifier
↓
EmailRouter
↓
ActivityLogger
↓
organized_emails
↓
summary reporting
```

---

# Responsibility Separation

## InboxReader

Responsible for:
- detecting email files
- returning inbox email paths

Does NOT know:
- classification rules
- routing logic
- summary tracking

---

## EmailClassifier

Responsible for:
- checking keywords
- deciding categories

Does NOT know:
- file movement
- inbox scanning
- summary reporting

---

## EmailRouter

Responsible for:
- creating category folders
- moving email files into matching folders

Does NOT know:
- keyword logic
- classification reasoning
- overall workflow state

---

## ActivityLogger

Responsible for:
- recording success/failure events
- writing execution history into log files

Does NOT know:
- classification rules
- routing decisions
- workflow orchestration

---

## main.py

Responsible for:
- orchestrating the workflow
- tracking execution state
- handling feedback/errors
- updating summary state
- printing summaries

---

# Categories

Current supported categories:

- urgent
- finance
- work
- promotions
- personal
- others

---

# Example Output

```text
Moved: invoice_email.txt -> finance
Moved: discount_offer.txt -> promotions
Moved: family_hello.txt -> personal

10
10
{'finance', 'promotions', 'personal', 'work', 'others'}

ALL COMPLETED!
```

---

# Testing Insight

During testing, some emails were routed to `others` because the classifier checks the email content, not the filename.

This revealed an important systems principle:

- input quality affects classification accuracy
- missing keywords lead to fallback routing
- dirty or inconsistent data can affect automation results

For V1, unmatched emails are handled safely by routing them into the `others` category.

---

# Technologies Used

- Python
- pathlib
- Object-Oriented Programming (OOP)
- File System Automation

---

# Learning Focus

This project was built to practice:

- systems thinking
- responsibility separation
- data flow architecture
- workflow orchestration
- filesystem automation
- modular backend design
- feedback system design
- observability concepts
- persistent logging systems

---

# V1.1 Upgrade — Activity Logging

The system now records success and failure events into a persistent log file.

Instead of only printing feedback to the terminal, the engine also writes execution history into:

```text
logs/activity_logs.txt
```

Example log entries:

```text
[SUCCESS] invoice_email.txt routed to finance
[FAILURE] corrupted_email.txt failed: error details
```

This improves:
- observability
- debugging
- execution history
- system transparency

---

# Future Improvements

Potential future upgrades:

- duplicate email handling
- recursive inbox scanning
- real Gmail/API integration
- smarter intent detection
- priority scoring
- email normalization pipeline
- analytics dashboard
- database persistence

---

# Project Status

V1 — Keyword-based email classification and routing workflow  
V1.1 — Added persistent activity logging

---

# Author

Khalid Ishola Abdulkadir