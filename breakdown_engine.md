# 🧩 Breakdown Engine — Email Automation Engine

> **Technical Detective Lens:** This document dissects each module of the project, highlighting functionality, structure, edge cases, design patterns, complexity, cognition, and ethics.

---

## Module Links

- 🛠️ [InboxReader — `core/inbox_reader.py`](core/inbox_reader.py)
- 🛠️ [EmailClassifier — `core/email_classifier.py`](core/email_classifier.py)
- 🛠️ [EmailRouter — `core/email_router.py`](core/email_router.py)
- 🛠️ [ActivityLogger — `core/logger.py`](core/logger.py)
- 🛠️ [Orchestration — `main.py`](main.py)
- 🛠️ [Pseudocode — `pseudocode.txt`](pseudocode.txt)

---

## 1️⃣ Surface Behavior

> What does the project output at a glance?

<details>
<summary>Email Automation Engine</summary>

```python
emails = reader.read(inbox_folder_path)

for email in emails:
    email_content = email.read_text()
    category = classifier.classify(email_content)
    router.route(email, category, destination_folder)
    logger.log_success(email_file=email, category=category)
```

This system:

- Reads `.txt` sample email files from an inbox folder.
- Extracts each email's content.
- Classifies the content using keyword rules.
- Routes emails into category folders.
- Logs success and failure events.
- Tracks processed email count.
- Tracks categories used.
- Prints a final workflow summary.

</details>

---

## 2️⃣ Line-by-Line Behavior

> Inspect each major module for concrete action.

<details>
<summary>InboxReader — Detecting Email Files</summary>

```python
class InboxReader:
```

Creates the inbox detection component.

```python
def read(self, inbox_folder_path):
```

Defines a method that receives the inbox folder path.

```python
if not inbox_folder_path.exists():
    raise FileNotFoundError(
        f"Input folder does not exist: {inbox_folder_path}"
    )
```

Checks whether the inbox folder exists. If not, it raises a clear file error.

```python
email_files = [
    file
    for file in inbox_folder_path.iterdir()
    if file.is_file() and file.suffix == ".txt"
]
```

Scans the inbox folder and keeps only `.txt` files.

This means the project treats text files as sample emails.

```python
return email_files
```

Returns the detected email file paths.

</details>

<details>
<summary>EmailClassifier — Keyword-Based Category Decision</summary>

```python
category_rules = {
    "urgent": ["urgent", "asap", "immediately"],
    "finance": ["invoice", "payment", "receipt"],
    "work": ["meeting", "project", "deadline"],
    "promotions": ["discount", "sale", "offer"],
    "personal": ["friend", "family", "hello"]
}
```

Defines category rules using keywords.

```python
converted_email = email_content.lower()
```

Converts email content to lowercase so matching becomes case-insensitive.

Example:

```text
"URGENT" → "urgent"
"Invoice" → "invoice"
```

```python
for category, keywords in category_rules.items():
```

Loops through each category and its keyword list.

```python
for keyword in keywords:
```

Loops through every keyword inside the current category.

```python
if keyword in converted_email:
    return category
```

If a keyword appears in the email content, return the matching category.

```python
return "others"
```

If no keyword matches, fallback safely to `others`.

</details>

<details>
<summary>EmailRouter — Moving Email Files</summary>

```python
source_file = email_file
```

Stores the current email file being routed.

```python
target_category = destination_folder / category
```

Creates the destination category folder path.

Example:

```text
organized_emails/finance
organized_emails/work
organized_emails/others
```

```python
target_category.mkdir(parents=True, exist_ok=True)
```

Creates the folder if it does not already exist.

```python
destination_path = target_category / source_file.name
```

Builds the final destination path for the email file.

```python
source_file.rename(destination_path)
```

Moves the email file into the category folder.

```python
print(f"Moved: {source_file.name} -> {category}")
```

Prints visible routing feedback.

```python
return destination_path
```

Returns where the file was moved.

</details>

<details>
<summary>ActivityLogger — Persistent Execution Memory</summary>

```python
message = (
    f"[SUCCESS] "
    f"{email_file.name} routed to {category}"
)
```

Creates a success log message.

```python
print(message)
```

Displays the message in the terminal.

```python
log_path = Path("logs/activity_logs.txt")
```

Defines where activity logs should be stored.

```python
with open(log_path, "a") as file:
    file.write(message + "\n")
```

Appends the success message to the activity log file.

The `"a"` mode means:

```text
append new log
do not erase old logs
```

Failure logging follows the same structure:

```python
message = (
    f"[FAILURE] "
    f"{email_file.name} failed: {error}"
)
```

This captures the failed email and error reason.

</details>

<details>
<summary>main.py — Workflow Orchestration</summary>

```python
reader = InboxReader()
classifier = EmailClassifier()
router = EmailRouter()
logger = ActivityLogger()
```

Creates all system components.

```python
emails = reader.read(inbox_folder_path)
```

Loads email file paths from the inbox folder.

```python
total_emails = len(emails)
processed_count = 0
categories_used = set()
```

Creates runtime summary state.

```python
for email in emails:
```

Processes emails one at a time.

```python
email_content = email.read_text()
```

Reads the text content from the current email file.

```python
category = classifier.classify(email_content)
```

Classifies the email based on its content.

```python
router.route(email, category, destination_folder)
```

Moves the email into the correct category folder.

```python
logger.log_success(email_file=email, category=category)
```

Records successful routing in the activity log.

```python
processed_count += 1
categories_used.add(category)
```

Updates summary state.

```python
except Exception as err:
```

Catches failures so one bad email does not crash the full workflow.

```python
logger.log_failure(email_file=email, error=err)
```

Records failure into the activity log.

```python
continue
```

Moves to the next email after a failure.

</details>

---

## 3️⃣ Variable Purpose

<details>
<summary>Important Variables</summary>

| Variable | Purpose |
|---|---|
| `inbox_folder_path` | Source folder where sample email files are stored |
| `destination_folder` | Root output folder for categorized emails |
| `emails` | List of detected `.txt` email files |
| `email` | Current email file being processed |
| `email_content` | Text content read from the email file |
| `category_rules` | Keyword map used for classification |
| `converted_email` | Lowercase email text for case-insensitive matching |
| `category` | Classification result for one email |
| `target_category` | Folder for a specific category |
| `destination_path` | Final moved email path |
| `logger` | Component that records success/failure events |
| `processed_count` | Number of emails successfully processed |
| `categories_used` | Set of categories encountered during execution |
| `total_emails` | Number of detected emails before processing |

</details>

---

## 4️⃣ System Flow

<details>
<summary>Full Workflow</summary>

```text
main.py
↓
set inbox path and destination folder
↓
InboxReader.read(inbox_folder_path)
↓
return .txt email files
↓
for each email
↓
read email content
↓
EmailClassifier.classify(email_content)
↓
return category
↓
EmailRouter.route(email, category, destination_folder)
↓
move email into category folder
↓
ActivityLogger.log_success(...)
↓
update summary state
↓
print final summary
```

</details>

<details>
<summary>Failure Flow</summary>

```text
error occurs
↓
except block catches error
↓
ActivityLogger.log_failure(email_file, error)
↓
print error
↓
continue to next email
```

This keeps the system from crashing completely because of one failed email.

</details>

---

## 5️⃣ Edge Cases

<details>
<summary>Possible Failures</summary>

- Inbox folder does not exist.
- Inbox contains no `.txt` files.
- Email content is empty.
- Email content has no matching keywords.
- Email filename suggests a category, but content does not.
- Destination folder cannot be created.
- Email file cannot be moved because it is open elsewhere.
- Log folder does not exist before writing.
- `logs/activity_logs.txt` cannot be written due to permission issues.
- Multiple categories match the same email; first matching category wins.

</details>

---

## 6️⃣ Structural Pattern

<details>
<summary>Reader → Classifier → Router → Logger Pattern</summary>

The project uses a four-stage automation pipeline:

```text
read
↓
classify
↓
route
↓
log
```

Each module owns one responsibility:

| Module | Responsibility |
|---|---|
| `InboxReader` | Detect sample email files |
| `EmailClassifier` | Decide category from content |
| `EmailRouter` | Move email file into category folder |
| `ActivityLogger` | Record execution history |
| `main.py` | Connect the workflow |

</details>

<details>
<summary>Keyword Rule Mapping</summary>

```python
category_rules = {
    "urgent": ["urgent", "asap", "immediately"],
    "finance": ["invoice", "payment", "receipt"],
    "work": ["meeting", "project", "deadline"],
    "promotions": ["discount", "sale", "offer"],
    "personal": ["friend", "family", "hello"]
}
```

This creates a simple symbolic decision system:

```text
keyword signal
↓
category decision
```

</details>

<details>
<summary>Fallback Routing Pattern</summary>

```python
return "others"
```

If no keyword matches, the email is safely routed to `others`.

This avoids:

```text
unclassified file
crash
silent failure
```

</details>

<details>
<summary>Persistent Logging Pattern</summary>

```python
with open(log_path, "a") as file:
    file.write(message + "\n")
```

This gives the system memory beyond terminal output.

Terminal output disappears after execution.

Log files persist.

</details>

---

## 7️⃣ Reframe / Visualize

<details>
<summary>Category Table</summary>

| Keyword Example | Category |
|---|---|
| `urgent`, `asap`, `immediately` | urgent |
| `invoice`, `payment`, `receipt` | finance |
| `meeting`, `project`, `deadline` | work |
| `discount`, `sale`, `offer` | promotions |
| `friend`, `family`, `hello` | personal |
| no match | others |

</details>

<details>
<summary>Input Quality Example</summary>

| Filename | Email Content | Result |
|---|---|---|
| `urgent_server_issue.txt` | `Server is broken.` | others |
| `urgent_server_issue.txt` | `Urgent server issue ASAP.` | urgent |
| `invoice_email.txt` | `Payment receipt attached.` | finance |

This shows why content quality matters more than filename.

</details>

---

## 8️⃣ Project Data Shape

<details>
<summary>Before Run</summary>

```text
sample_inbox/
├── invoice_email.txt
├── urgent_server_issue.txt
├── discount_offer.txt
└── family_hello.txt
```

</details>

<details>
<summary>After Run</summary>

```text
organized_emails/
├── finance/
│   └── invoice_email.txt
│
├── urgent/
│   └── urgent_server_issue.txt
│
├── promotions/
│   └── discount_offer.txt
│
└── personal/
    └── family_hello.txt
```

</details>

<details>
<summary>Activity Log Shape</summary>

```text
[SUCCESS] invoice_email.txt routed to finance
[SUCCESS] discount_offer.txt routed to promotions
[FAILURE] corrupted_email.txt failed: error details
```

</details>

---

## 9️⃣ Insights & Recommendations

- ✅ `InboxReader` keeps file detection isolated.
- ✅ `EmailClassifier` uses simple, readable keyword rules.
- ✅ `EmailRouter` owns movement and folder creation.
- ✅ `ActivityLogger` adds persistent observability.
- ✅ `main.py` owns orchestration and summary state.
- ⚠️ Log folder should exist before logger writes to it.
- ⚠️ Keyword matching is simple and may create false positives.
- ⚠️ First matching category wins if multiple categories match.
- ⚠️ Classification depends on content quality, not filename.
- ⚠️ Duplicate email filenames may need safe renaming in a future upgrade.

---

## 🔟 Complexity Analysis

<details>
<summary>Time and Space Complexity</summary>

Let:

```text
n = number of email files
k = number of category keywords
m = average email content size
```

### Time Complexity

Inbox reading scans files once:

```text
O(n)
```

Classification checks each email against category keywords:

```text
O(n × k × m)
```

In simpler V1 terms:

```text
more emails + more keywords + larger email content
=
more processing time
```

Routing and logging each email are approximately linear relative to number of emails:

```text
O(n)
```

### Space Complexity

The system stores the email file list:

```text
O(n)
```

It also stores summary state:

```text
O(c)
```

where:

```text
c = number of categories used
```

Since categories are limited, this is small.

</details>

---

## 1️⃣1️⃣ Cognition & Intelligence Engineering

<details>
<summary>Cognition Layer</summary>

### Prediction

The system predicts that certain keywords imply a category.

Example:

```text
invoice → finance
urgent → urgent
sale → promotions
```

### Error

Possible reasoning errors:

- Email has no keyword signal.
- Filename suggests one category, but content suggests another.
- Multiple categories appear in the same email.
- Keyword appears in the wrong context.

Example:

```text
"not an urgent issue"
```

could still match `urgent`.

### Compression

The system compresses full email content into one category.

```text
many words
↓
single category
```

### Context

The system uses content context only.

It does not currently use:

- sender
- subject
- timestamp
- priority
- thread history

### Meta

The system can be observed through logs.

This means the automation is not silent; its behavior can be reviewed later.

### Application

The system models a simple version of real email triage:

```text
incoming message
↓
intent/category detection
↓
routing decision
↓
audit trail
```

</details>

---

## 1️⃣2️⃣ Ethics / Safety Filter

<details>
<summary>Ethical and Safety Considerations</summary>

This project is local and sample-based, but the idea maps to real email automation.

Important safety points:

- Do not process real emails without user consent.
- Do not store sensitive email contents unnecessarily.
- Avoid routing important messages silently without review.
- Keep logs careful; logs can expose private filenames or error data.
- Add safeguards before connecting to Gmail or real inbox APIs.
- Always allow fallback routing for uncertain cases.

Ethical automation rule:

```text
When confidence is low, route safely instead of pretending certainty.
```

For V1, `others` acts as the safety fallback category.

</details>

---

## ⚡ 8-Step Truth-Finding Approach

Use this when debugging or extending the project:

1. Surface Behavior
2. Line-by-Line Behavior
3. Variable Purpose
4. System Flow
5. Edge Cases
6. Structural Pattern
7. Reframe / Visualize
8. Insights & Recommendations

---

## 🧠 Final Detective Summary

Email Automation Engine is a local sample-based email routing system.

Its core intelligence comes from:

```text
content reading
↓
keyword detection
↓
category decision
↓
file routing
↓
activity logging
```

The biggest lesson from this project is:

```text
input quality affects automation quality
```

If content does not contain usable signals, classification falls back to `others`.

The V1.1 activity logging upgrade improves:

```text
observability
debugging
execution memory
system transparency
```

The key engineering idea:

```text
Automation should not only act.
Automation should explain what it did.
```