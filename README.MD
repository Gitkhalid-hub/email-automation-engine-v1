# EMAIL AUTOMATION ENGINE V1

A Python-based automation system that reads sample email files, classifies them using keyword rules, routes them into category folders, and generates execution summaries.

---

# Features

- Reads sample email files from an inbox folder
- Classifies emails using keyword-based rules
- Automatically creates category folders
- Routes emails into matching folders
- Handles unknown classifications safely
- Generates processing summaries
- Includes controlled feedback and failure handling
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
├── pseudocode.txt
├── breakdown_engine.md
├── requirements.txt
└── .gitignore
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
workflow summary generation
```

---

# 🧠 Architecture

The system is built with layered automation design and clear responsibility separation.

### Architecture Layers

| Layer | Responsibility |
|---|---|
| `inbox_reader.py` | Detects valid email files from the inbox |
| `email_classifier.py` | Decides categories using keyword rules |
| `email_router.py` | Routes email files into category folders |
| `logger.py` | Records persistent success/failure events |
| `main.py` | Orchestrates workflow execution and summary state |
| `pseudocode.txt` | Planning and workflow reasoning |
| `breakdown_engine.md` | Deep engineering analysis, debugging cognition, edge cases, and system reasoning |

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

=== EMAIL AUTOMATION SUMMARY ===

Total Emails: 10
Processed Emails: 10
Categories Used: {'finance', 'promotions', 'personal', 'work', 'others'}

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
- Logging / Observability Concepts

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

# Breakdown Engine

The project includes a dedicated engineering investigation document:

[breakdown_engine.md](breakdown_engine.md)

This file dissects the system using a technical detective approach.

It analyzes:

- surface behavior
- line-by-line execution
- variable purpose
- system flow
- edge cases
- structural patterns
- classification reasoning
- routing behavior
- observability design
- complexity analysis
- Cognition and Intelligence Engineering
- Ethics and Safety Considerations

This improves:

- debugging cognition
- architectural understanding
- reasoning transparency
- workflow observability
- system extensibility

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