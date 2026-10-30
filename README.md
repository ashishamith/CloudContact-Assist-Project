# ✦ CloudContact Assist

### Intelligent Customer Support & Ticket Management Platform

<p align="center">
  <b>Smart Ticket Routing • Automated Prioritization • Interactive Analytics</b>
</p>

<p align="center">
  Built with Python | Streamlit | Google Sheets API | Plotly
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Database-Google%20Sheets-34A853?logo=googlesheets&logoColor=white" />
  <img src="https://img.shields.io/badge/Visualization-Plotly-3F4F75?logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

---

## 🚀 Overview

**CloudContact Assist** is an intelligent customer support and ticket management platform designed to streamline customer service operations through automated ticket categorization, priority assignment, team routing, and centralized ticket monitoring.

The application provides customers with an interactive support portal to submit service requests. A Python-based routing engine processes incoming queries, identifies the relevant support category, assigns priority levels, and directs tickets to the appropriate support team.

Administrators can monitor ticket activity, analyze operational performance, manage ticket statuses, and access interactive visualizations through a centralized dashboard.

## 🖥️ Application Preview

### 01. Home Page

![CloudContact Assist Home Page](screenshots/home.png)

### 02. Customer Support Portal

![Customer Support Portal](screenshots/support-portal.png)

### 03. Admin Dashboard

![Admin Dashboard](screenshots/admin-dashboard.png)

### 04. Analytics Dashboard

![Analytics Dashboard](screenshots/analytics.png)

---

## ✨ Key Features

### 🎧 Customer Support Portal
- Interactive customer support request form.
- Customer email, subject, and issue description collection.
- Automated ticket creation.
- Unique ticket ID generation.
- Ticket submission confirmation.

### 🧠 Intelligent Ticket Routing
- Rule-based customer query categorization.
- Automatic support team assignment.
- Priority classification: High, Medium, and Low.
- Structured ticket processing using Python.
- Consistent ticket routing based on predefined rules.

### 📊 Admin Analytics Dashboard
- Total ticket volume monitoring.
- Open and in-progress ticket tracking.
- High-priority ticket monitoring.
- Category-wise ticket distribution.
- Priority-wise ticket analysis.
- Workflow status visualization.
- Support team performance overview.

### 🛡️ Ticket Management
- Administrator authentication.
- Centralized ticket monitoring.
- Ticket filtering by team, status, and priority.
- Ticket status updates.
- Google Sheets integration for ticket storage.
- CSV export of filtered ticket records.

### 🎨 User Interface
- Modern dark-themed interface.
- Gradient-based visual design.
- Interactive dashboard components.
- Responsive application layout.
- Visually organized analytics sections.

---

## 🏗️ System Architecture

```text
                    CUSTOMER
                       |
                       v
             CUSTOMER SUPPORT PORTAL
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
          CATEGORY  PRIORITY   TEAM
              |        |        |
              +--------+--------+
                       |
                       v
                GOOGLE SHEETS
                       |
                       v
                ADMIN DASHBOARD
                       |
          +------------+------------+
          |            |            |
          v            v            v
       ANALYTICS     FILTERS     STATUS
                                  UPDATES
```

---

## 🔄 Application Workflow

1. Customer submits a support request.
2. The application validates the submitted information.
3. The routing engine analyzes the subject and message.
4. The system assigns a support category.
5. The system determines the ticket priority.
6. The ticket is assigned to the relevant support team.
7. Ticket information is stored in Google Sheets.
8. Administrators monitor and manage tickets through the dashboard.
9. Ticket status changes are synchronized with Google Sheets.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and ticket processing |
| Streamlit | Interactive web application |
| Pandas | Data processing and manipulation |
| Plotly | Interactive charts and visualizations |
| Google Sheets API | Ticket storage and retrieval |
| gspread | Google Sheets integration |
| Google Auth | Service account authentication |
| python-dotenv | Local environment configuration |
| Git | Version control |
| GitHub | Source code management |

---

## 📁 Project Structure

```text
CloudContact-Assist/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── config/
│   └── settings.py
│
├── services/
│   ├── __init__.py
│   ├── google_sheets.py
│   └── ticket_router.py
│
├── credentials/
│   └── service_account.json
│
└── screenshots/
    ├── home.png
    ├── support-portal.png
    ├── admin-dashboard.png
    └── analytics.png
```

> **Security:** The credentials folder is for local development only and must be excluded from GitHub using `.gitignore`.

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10 or above
- Git
- Google account
- Google Cloud project
- Google Sheets API access

### 1. Clone the Repository

```bash
git clone https://github.com/ashishamith/CloudContact-Assist-Project.git
```

### 2. Navigate to the Project Directory

```bash
cd CloudContact-Assist-Project
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Google Sheets API

1. Open Google Cloud Console.
2. Create or select a Google Cloud project.
3. Enable Google Sheets API and Google Drive API.
4. Create a service account.
5. Generate a service account JSON key.
6. Store the JSON file locally in the `credentials/` directory.
7. Create a Google spreadsheet named `CloudContact Assist`.
8. Share the spreadsheet with the service account email and grant Editor access.

### 6. Configure Administrator Credentials

Create a `.env` file in the project root:

```env
ADMIN_USERNAME=your_username
ADMIN_PASSWORD=your_strong_password
```

### 7. Run the Application

```bash
streamlit run app.py
```

Open the local application URL displayed in your terminal.

---

## 🔐 Security & Configuration

- Keep Google service account credentials outside source code.
- Exclude private keys and `.env` files from GitHub.
- Use secure administrator credentials.
- Restrict Google Sheets access to authorized service accounts.
- Never expose service account private keys in public repositories.

Example `.gitignore`:

```gitignore
.env
.streamlit/secrets.toml
credentials/
__pycache__/
*.pyc
.venv/
venv/
```

---

## 🔮 Future Enhancements

- AI-powered ticket classification using Natural Language Processing.
- Automated customer email notifications.
- SLA monitoring and ticket escalation.
- Role-based administrator access.
- Advanced operational analytics.
- CRM integration.
- Cloud contact center platform integration.
- AI-assisted customer response recommendations.

---

## 🎯 Project Objectives

- Reduce manual effort in customer support ticket classification.
- Improve ticket allocation through automated team routing.
- Organize support requests according to priority.
- Centralize ticket information and administrative monitoring.
- Provide operational insights through interactive analytics.

---

## 👨‍💻 Author

**Ashish Amith R**

BE – Artificial Intelligence & Machine Learning

**Technical Interests:** Python | Data Analytics | AI/ML | Automation | Dashboard Development

---

## ⭐ Support the Project

If you find this project useful or interesting, consider giving the repository a ⭐ star.

<p align="center">
  <b>CloudContact Assist</b><br/>
  Smarter Routing. Better Support. Clearer Operations.
</p>
