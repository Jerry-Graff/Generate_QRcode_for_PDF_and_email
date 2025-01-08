"""
This script generates a QR code from a PDF URL and saves it as an image file.

It performs the following steps:
1. Retrieves a public PDF URL from an environment variable or directly provided value.
2. Configures and creates a QR code that encodes the PDF URL.
3. Generates an image of the QR code with specified colors.
4. Saves the generated QR code image as 'cv_qr.png'.

Ensure that the environment variable PUBLIC_URL is set to the public PDF link,
or modify the script to directly assign the PDF URL to the 'pdf_url' variable.
"""

import qrcode
import os


def generate_qr():
    pdf_url = os.getenv("PUBLIC_URL")  # Ensure PUBLIC_URL is set
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(pdf_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="orange")
    img.save("cv_qr.png")
    print("QR code generated and saved as cv_qr.png.")
