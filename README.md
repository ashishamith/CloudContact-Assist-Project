# ✦ CloudContact Assist
### Intelligent Customer Support & Ticket Management Platform

A smart customer support platform that streamlines ticket submission, automated categorization, priority assignment, team routing, and ticket monitoring through an interactive admin dashboard.

**Built with Python · Streamlit · Google Sheets · Plotly**

---

## 🚀 Overview

CloudContact Assist is a customer support management application designed to simplify ticket handling and improve support operations.

Customers can submit support requests through a dedicated portal. The system analyzes the issue, categorizes the request, assigns a priority, and routes it to the appropriate support team.

Administrators can monitor incoming requests, analyze ticket distribution, filter records, and update ticket statuses through a centralized dashboard.

## ✨ Key Features

### 🎧 Customer Support Portal
- Submit support requests using a simple web form.
- Capture customer email, issue subject, and description.
- Automatically process submitted support tickets.
- Generate ticket details after successful submission.

### 🧠 Intelligent Ticket Routing
- Automatically categorize customer queries.
- Assign tickets to relevant support teams.
- Determine ticket priority based on routing rules.
- Streamline ticket allocation through Python-based logic.

### 📊 Admin Analytics Dashboard
- Monitor total ticket volume.
- Track open, in-progress, and high-priority tickets.
- Visualize ticket distribution by category.
- Analyze ticket priorities and workflow status.
- Monitor tickets assigned to different teams.

### 🛡️ Ticket Management
- Secure administrator login.
- Search and filter support tickets.
- Update ticket statuses.
- Export filtered ticket records as CSV.
- Store ticket records in Google Sheets.

### 🎨 User Interface
- Modern dark-themed interface.
- Gradient-based visual design.
- Interactive dashboard components.
- Responsive layout for different screen sizes.

---

## 🏗️ System Architecture

```text
             CUSTOMER
                 |
                 v
        CUSTOMER SUPPORT FORM
                 |
                 v
          PYTHON APPLICATION
                 |
                 v
        TICKET ROUTING ENGINE
                 |
        +--------+--------+
        |        |        |
        v        v        v
     CATEGORY PRIORITY  TEAM
        |        |        |
        +--------+--------+
                 |
                 v
          GOOGLE SHEETS
                 |
                 v
         ADMIN DASHBOARD
                 |
        +--------+--------+
        |        |        |
        v        v        v
     ANALYTICS FILTERS  STATUS
                         UPDATES
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and ticket processing |
| Streamlit | Web application and dashboard |
| Pandas | Data processing and analysis |
| Plotly | Interactive analytics and charts |
| Google Sheets API | Ticket storage and management |
| Python-dotenv | Environment variable management |
| Git & GitHub | Version control and project hosting |

---

## 📁 Project Structure

```text
CloudContact-Assist/
│
├── app.py
│
├── services/
│   ├── __init__.py
│   ├── ticket_router.py
│   └── google_sheets.py
│
├── credentials/
│   └── service_account.json
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/CloudContact-Assist.git
```

### 2. Navigate to the project directory

```bash
cd CloudContact-Assist
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file:

```env
ADMIN_USERNAME=your_username
ADMIN_PASSWORD=your_password
```

### 6. Configure Google Sheets

1. Create a Google Cloud project.
2. Enable the Google Sheets API.
3. Create a service account.
4. Download its JSON credentials.
5. Place the credentials file inside the `credentials/` directory.
6. Share your Google spreadsheet with the service account email.
7. Configure the spreadsheet name expected by your application.

### 7. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

---

## ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

1. Push your project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select `app.py` as the application entry point.
5. Configure environment variables and Google service account credentials using Streamlit Secrets.
6. Deploy the application.

**Security note:** Never commit `.env`, service account JSON files, private keys, or passwords to GitHub.

---

## 🔐 Security Considerations

- Keep administrator credentials outside source code.
- Store Google service account credentials securely.
- Exclude sensitive files using `.gitignore`.
- Restrict spreadsheet access to authorized service accounts.
- Use HTTPS when deploying the application.

---

## 🎯 Project Objectives

- Automate repetitive customer support ticket classification.
- Improve ticket ownership through rule-based team assignment.
- Prioritize customer issues for better workflow management.
- Centralize ticket records and administrative monitoring.
- Provide actionable insights through interactive analytics.

---

## 🔮 Future Enhancements

- AI-powered ticket classification using NLP.
- Automated customer email notifications.
- SLA monitoring and escalation workflows.
- Role-based administrator access.
- Advanced ticket performance analytics.
- Integration with CRM and cloud contact center platforms.

---

## 👨‍💻 Author

**Ashish Amith R**

BE – Artificial Intelligence & Machine Learning

Interested in building practical solutions using Python, AI/ML, data analytics, and workflow automation.

---

### ⭐ Support

If you find this project interesting, consider giving the repository a star!

**CloudContact Assist — Smarter Routing. Better Support. Clearer Operations.**