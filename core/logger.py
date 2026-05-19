# THE MEMORY STAGE.

from pathlib import Path


class ActivityLogger:

    def log_success(self, email_file, category):

        message = (
            f"[SUCCESS] "
            f"{email_file.name} routed to {category}"
        )

        print(message)

        log_path = Path("logs/activity_logs.txt")

        with open(log_path, "a") as file:
            file.write(message + "\n")

    def log_failure(self, email_file, error):

        message = (
            f"[FAILURE] "
            f"{email_file.name} failed: {error}"
        )

        print(message)

        log_path = Path("logs/activity_logs.txt")

        with open(log_path, "a") as file:
            file.write(message + "\n")