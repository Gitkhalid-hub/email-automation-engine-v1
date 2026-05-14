# THE MIGRATION STAGE.
from pathlib import Path

class EmailRouter:
	
	def route(self, email_file, category, destination_folder):
		# define source file
		source_file = email_file
		
		# create target category folder
		target_category = destination_folder / category
		target_category.mkdir(parents=True, exist_ok=True)
		
		# build destination path
		destination_path = target_category / source_file.name
		
		# move the file
		source_file.rename(destination_path)
		
		# print the summary
		print(f"Moved: {source_file.name} -> {category}")
		
		return destination_path