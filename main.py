"""
Main entry point for the Convert CV to QR Code project.
It generates a QR code from a PDF URL and sends it via email.
"""

from generate_qrcode_from_pdf import generate_qr
from send_qr_code_via_email import send_email


def main():
    try:
        print("Generating QR code...")
        generate_qr()
        print("Sending email with QR code...")
        send_email()
        print("Process completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
