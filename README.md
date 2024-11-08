# Panda Prototype - Email Customer Feature Proposal

A web application prototype designed for Go Sales Ireland to simplify the payment process for customers. Sales representatives can send payment links directly to customers' emails, allowing them to complete payments online at their convenience. This project includes features like web scraping, browser automation, and email notifications, making it a versatile tool for streamlining customer interactions.

## Features

1. **Customer Signup Link**: 
   - Sales reps enter customer details (first name, last name, email, etc.) into a web form.
   - Upon form submission, an email with a signup link is sent to the customer.
   
2. **Pre-Filled Payment Page**:
   - The payment page is pre-populated with non-editable fields ("Agent Name," "Area," and "Plan") to ensure a smooth payment process.
   - This feature reduces errors and improves user experience by minimizing the steps customers need to take.

## Technology Stack

- **Backend**: Python (Flask Framework)
   - **Flask** serves as a lightweight web framework to handle HTTP requests and route them to the appropriate functions.
   - **Selenium** is used for browser automation, allowing automated interactions with the web page (e.g., form submissions).
   - **Pandas** is utilized for data handling, enabling efficient data manipulation, especially for reading and writing structured data.

- **Frontend**: HTML, CSS, JavaScript
   - A clean and simple UI built with HTML and CSS for the form and user interaction.
   - JavaScript is used for form validation and dynamic content handling.

- **Automation**:
   - **Selenium WebDriver**: Automates browser tasks to simulate user actions. This allows sales reps to test the process in real-time.
   - **Threading**: Used to manage multiple tasks concurrently, such as sending emails and updating databases without causing delays in user interaction.
   
- **Email Notifications**:
   - **SMTP** is used to send automated emails. The email includes a payment link that redirects customers to a secure page where they can complete their payment.
   - **Email Templates** are created with HTML for better user engagement.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Darshan22112000/Panda-Prototype.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Panda-Prototype
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python final_prototype.py
   ```

5. Open your browser and go to:
   ```plaintext
   http://localhost:5000
   ```

## Usage Guide

1. **Form Submission**: The sales representative fills out the form with customer details, selects the plan, and submits it.
2. **Email Notification**: The customer receives an email with the payment link.
3. **Payment Page**: The customer clicks the link, fills out the remaining fields, and completes the payment.

## Future Enhancements

1. **Code Optimization**:
   - Refactor code to improve readability and efficiency, especially in data handling and routing.

2. **Database Integration**:
   - Use a database like **PostgreSQL** or **MySQL** to store customer data, payment statuses, and transaction histories securely.

3. **Deployment**:
   - Deploy the app on cloud platforms such as **Google Cloud** or **AWS**.
   - Integrate **CI/CD pipelines** for automated testing and deployment.
   - Set up a **production environment** with SSL for secure communication.

4. **API Integration**:
   - Integrate third-party APIs for additional functionality, such as real-time payment status updates.
   - Use RESTful API design principles for future scalability and interoperability.

5. **Security Enhancements**:
   - **Data Encryption**: Ensure sensitive data, such as customer details, is encrypted during transmission.
   - **OAuth**: Implement authentication for added security, especially if this app expands to other services.
   - **GDPR Compliance**: Ensure data privacy policies are followed.

## Benefits

- **Go Sales Ireland**: Enhances customer engagement, optimizes resource allocation, and provides actionable data insights.
- **Panda**: Expands customer reach, increases sales opportunities, and provides data for strategic decision-making.

---
