# AI Chatbot Testing & Automation Framework

## Project Overview

This project is an AI chatbot testing automation framework built using Playwright, PyTest, Flask, and API testing.

The framework automates chatbot UI workflows, validates responses, performs negative testing, and tests backend APIs.

---

## Features

- UI Automation Testing
- API Automation Testing
- Negative Testing
- HTML Reporting
- Logging System
- Screenshot Capture
- Prompt Validation
- Response Validation
- Flask-based Local Chatbot Application

---

## Tech Stack

- Python
- Playwright
- PyTest
- Flask
- Requests
- HTML Reports

---

## Folder Structure

```bash
AI-Chatbot-Testing-Framework/
│
├── chatbot_app.py
├── tests/
│   ├── ui_tests/
│   └── api_tests/
│
├── pages/
├── utils/
├── screenshots/
├── reports/
├── logs/
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/mahi1512-beep/AI-Chatbot-Testing-Framework.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Chatbot Application

```bash
python chatbot_app.py
```

### Run UI Tests

```bash
pytest tests/ui_tests -v -s
```

### Run API Tests

```bash
pytest tests/api_tests -v -s
```

---

## Test Scenarios Covered

- Prompt Testing
- Response Validation
- Negative Testing
- API Validation
- Screenshot Handling
- Logging Validation

---

## Future Enhancements

- Jenkins CI/CD Integration
- Docker Support
- Cross-Browser Testing
- Parallel Test Execution

---

## Author

Mahendra Singh
