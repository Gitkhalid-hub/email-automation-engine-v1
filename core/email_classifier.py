# THE CATEGORY DECISION STAGE.

class EmailClassifier:
	
	def classify(self, email_content):
		# defined category rules
		category_rules = {
			"urgent": ["urgent", "asap", "immediately"],
			"finance": ["invoice", "payment", "receipt"],
			"work": ["meeting", "project", "deadline"],
			"promotions": ["discount", "sale", "offer"],
			"personal": ["friend", "family", "hello"]
		}
		
		converted_email = email_content.lower()
		
		for category, keywords in category_rules.items():
			for keyword in keywords:
				if keyword in converted_email:
					return category
		return "others"