# PROJECT: Email Automation Engine V1.1

# V1 GOAL:
# Read sample email files, classify them using keyword rules,
# route them into category folders, log execution history,
# and print workflow summaries.

from pathlib import Path

from core.inbox_reader import InboxReader
from core.email_classifier import EmailClassifier
from core.email_router import EmailRouter
from core.logger import ActivityLogger

# SOURCE / DESTINATION PATHS
inbox_folder_path = Path(
    "C:\\Users\\KHIDDAFA\\PycharmProjects\\Email_Automation_Engine_v1\\sample_inbox"
)

destination_folder = Path("organized_emails")

# SYSTEM COMPONENTS
reader = InboxReader()
classifier = EmailClassifier()
router = EmailRouter()
logger = ActivityLogger()

# READ EMAIL FILES
emails = reader.read(inbox_folder_path)

# SUMMARY STATE
total_emails = len(emails)
processed_count = 0
categories_used = set()

# WORKFLOW PIPELINE
for email in emails:

    try:
        # READ EMAIL CONTENT
        email_content = email.read_text()

        # CLASSIFY EMAIL
        category = classifier.classify(email_content)

        # ROUTE EMAIL
        router.route(email, category, destination_folder)

        # LOG SUCCESS EVENT
        logger.log_success(email_file=email, category=category)

        # UPDATE SUMMARY STATE
        processed_count += 1
        categories_used.add(category)

        print("Successfully Added!")

    except Exception as err:

        # LOG FAILURE EVENT
        logger.log_failure(email_file=email, error=err)

        print(f"Error: {err}")

        continue

# FINAL SUMMARY REPORT
print("\n=== EMAIL AUTOMATION SUMMARY ===")

print("Total Emails:", total_emails)
print("Processed Emails:", processed_count)
print("Categories Used:", categories_used)

print("\nALL COMPLETED!")