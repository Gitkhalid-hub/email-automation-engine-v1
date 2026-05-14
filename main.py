#PROJECT: Email Automation Engine V1

#V1 GOAL:
#Read sample email files, classify them by keywords, route them into category folders, and print summary.

from core.inbox_reader import InboxReader
from core.email_classifier import EmailClassifier
from core.email_router import EmailRouter
from pathlib import Path

inbox_folder_path = Path("C:\\Users\\KHIDDAFA\\PycharmProjects\\Email_Automation_Engine_v1\\sample_inbox")
destination_folder = Path("organized_emails")

reader = InboxReader()
classifier = EmailClassifier()
router = EmailRouter()

emails = reader.read(inbox_folder_path)

total_emails = len(emails)
processed_count = 0
categories_used = set()

for email in emails:
	try:
		email_content = email.read_text()
		category = classifier.classify(email_content)
		router.route(email, category, destination_folder)
		
		processed_count += 1
		categories_used.add(category)
		
		print("Successfully Added!")
	
	except Exception as err:
		print(f"Error: {err}")
		continue
		
print(total_emails)
print(processed_count)
print(categories_used)
print("ALL COMPLETED!")