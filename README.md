# Convert PDF to QR Code and Send

This project automates converting a PDF (such as a CV) into a QR code and sending that QR code via email. It leverages Python libraries for QR code generation and email sending, using SMTP with Gmail as the email provider.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview

The project consists of two primary functionalities:
1. **QR Code Generation**: Generates a QR code from a public URL of a PDF file.
2. **Email Sending**: Sends an email with the generated QR code attached using SMTP.

An optional `main.py` script can orchestrate these tasks, providing a single entry point to run the entire workflow.

## Features

- **QR Code Generation**: Uses the `qrcode` Python library to convert a PDF URL into a QR code image (`cv_qr.png`).
- **Email Sending**: Uses Python’s `smtplib` to send an email with the QR code as an attachment.
- **Configuration via Environment Variables**: Credentials and configuration details are stored in a `.env` file for security and flexibility.
- **Modular Design**: Separate scripts for QR code generation and email sending, with an optional main script to run them sequentially.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/Convert_PDF_to_QRcode_and_Send.git
   cd Convert_PDF_to_QRcode_and_Send