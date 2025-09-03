import sys
from networksecurity.logger.logger import logger

class NetworkSecurityException(Exception):
    """Custom Exception for capturing detailed error information in network security-related scripts."""

    def __init__(self, error_message: str, error_details: sys):
        super().__init__(error_message)
        self.error_message = str(error_message)

        # Extract traceback info
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno if exc_tb else None
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "<unknown>"

    def __str__(self) -> str:
        return (
            f"\n📌 NetworkSecurityException Occurred!\n"
            f"   📝 File      : {self.file_name}\n"
            f"   📍 Line No   : {self.lineno}\n"
            f"   ❌ Message   : {self.error_message}\n"
        )

# Example usage
if __name__ == "__main__":
    try:
        logger.info("enter the try block")
        a = 1 / 0  # Intentional error
        print("This will not be printed: ", a)
    except Exception as e:
        logger.info("raised an error")
        raise NetworkSecurityException(e, sys)
