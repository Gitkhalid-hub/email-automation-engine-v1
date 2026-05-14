# EMAIL DETECTION STAGE.

class InboxReader:

    def read(self, inbox_folder_path):

        if not inbox_folder_path.exists():
            raise FileNotFoundError(
                f"Input folder does not exist: {inbox_folder_path}"
            )

        # get all text email files
        email_files = [
            file
            for file in inbox_folder_path.iterdir()
            if file.is_file() and file.suffix == ".txt"
        ]

        return email_files