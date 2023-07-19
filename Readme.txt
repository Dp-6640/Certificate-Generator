# Certificate Management Web Application

Welcome to the Certificate Management Web Application! This Django-based web application allows users to generate, verify, and customize certificates. It provides an easy-to-use interface for generating PDF certificates and enables users to verify existing certificates securely.

## Features

- User registration and login functionality for certificate generation and customization.
- Certificate generation feature that allows users to create new certificates as PDFs.
- Certificate verification functionality that prevents tampering using secure token-based verification.
- Ability for users to customize their certificates without altering the original content.
- Bonus feature JWT token-based verification for added security.

## Prerequisites

- Python 3.x
- Django 3.x
- ReportLab (for PDF generation)
- Django REST framework (for JWT token-based verification)

## Installation

1. Clone the repository to your local machine


2. Create and activate a virtual environment (optional but recommended):


3. Install the required dependencies:


4. Perform database migrations:


5. Create a superuser to access the Django admin interface:


6. Run the development server:


7. Access the web application in your browser at http://localhost:8000/

## Usage

1. Register or log in to the web application to access all features.
2. **Generate Certificate:**
- Click on "Generate Certificate" in the navigation menu.
- Enter the title and content for the certificate and click "Generate PDF."
- The generated certificate will be downloaded as a PDF file.

3. **Verify Certificate:**
- Click on "Verify Certificate" in the navigation menu.
- Enter the certificate code (case-insensitive) in the verification form and click "Verify."
- If the certificate is valid, the title and content of the certificate will be displayed. Otherwise, an error message will be shown.

4. **Customize Certificate:**
- After generating a certificate, you can customize it by clicking "Customize" on the home page or the "Customize" button on the generated certificate's detail page.
- Edit the title and content of the certificate as desired and click "Save Changes" to update the certificate.

## Bonus Feature: JWT Token-Based Verification

This web application uses JWT (JSON Web Token) for certificate verification. When a certificate is generated, a verification token is created and associated with the certificate. This token is used for secure certificate verification.

## Note

- This is a simplified implementation of a certificate management web application. In a production environment, additional security measures and user authentication should be implemented.
- The provided code is for educational purposes and may not be suitable for production use without further refinements and security considerations.

## Acknowledgments

- The project was inspired by the requirements provided in the assignment.
- Thank you to the Django community and developers for the wonderful framework.

## License

This project is licensed under the [MIT License](LICENSE).
