# 🛡️ MPLADGuard-AI

<p align="center">
  <img src="assets/mpladguard-icon.png" width="150">
</p>

<p align="center">
  <b>AI-Powered Monitoring, Anomaly Detection & Risk Intelligence Platform for MPLADS</b>
</p>

<p align="center">
# 🛡️ MPLADGuard AI

### Backend Implementation & Project Monitoring Platform for MPLADS

**MPLADGuard AI** is a project monitoring and risk-analysis platform designed to improve transparency, efficiency, and oversight in the implementation of the **Members of Parliament Local Area Development Scheme (MPLADS)**.

The platform is intended to analyze project, financial, execution, inspection, and progress-related information and identify projects that may require closer monitoring or human verification.

> **Important:** A high-risk score does not prove fraud. It indicates that a project contains indicators that may require further investigation.

---

## 👨‍💻 My Contribution

This fork contains my **backend implementation** developed during the SIH 2026 project.

My primary contribution was focused on designing and implementing the backend/API layer that connects project data with the application's frontend and risk-analysis workflow.

### Backend Work

* Designed the **FastAPI backend structure**
* Developed REST API endpoints for project-related operations
* Implemented request/response validation using **Pydantic**
* Built backend data-processing services
* Implemented project statistics and analytical endpoints
* Developed the initial **risk-scoring logic**
* Prepared the backend architecture for ML/anomaly-detection integration
* Created an ML integration interface/stub for future model integration
* Worked on backend ↔ frontend API integration
* Structured the backend for future database and government-data integration

### Repository Context

This repository is my personal fork of the team's MPLADGuard AI project.

The `feature/backend-api` branch contains the backend implementation I developed.

The original team repository contains the team's final integrated implementation.

---

# 🚨 Problem

MPLADS involves development projects across different regions, implementing agencies, contractors, and stakeholders.

Large-scale manual monitoring can make it difficult to quickly identify projects that may require additional attention.

Potential monitoring indicators include:

* Unusual project costs
* Significant project delays
* Fund-utilization irregularities
* Financial vs. physical progress mismatch
* Insufficient inspections
* Unusual execution patterns
* Procurement-related anomalies
* Inconsistent project information

MPLADGuard AI aims to make this monitoring process more **data-driven, explainable, and efficient**.

---

# 💡 Solution

The platform combines project monitoring, data processing, analytics, and risk assessment into a centralized system.

### Core workflow

```text
Project Data
     ↓
Data Processing
     ↓
Feature Calculation
     ↓
Risk Analysis
     ↓
Risk Score
     ↓
Explainable Indicators
     ↓
Dashboard
     ↓
Human Verification
```

The system is designed as a **decision-support platform**, rather than an automated fraud-detection authority.

---

# ⚙️ Backend Architecture

The backend is built around a REST API architecture using **FastAPI**.

```text
                 React + Vite
                     │
                     │ REST API
                     ▼
              ┌──────────────┐
              │    FastAPI   │
              │    Backend   │
              └──────┬───────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Project     Analytics   Risk Engine
       Data          │           │
          │          │           │
          └──────────┼───────────┘
                     ▼
              API Responses
                     │
                     ▼
                 Dashboard
```

The backend is structured so that additional components such as databases, ML models, document-processing systems, and government datasets can be integrated later.

---

# 🚀 Current Backend Features

## 1. Project Data APIs

The backend provides API functionality for working with project-level information.

Examples include:

* Project retrieval
* Project statistics
* Project filtering
* Project status information
* Project-level analysis

---

## 2. Risk Scoring Engine

A backend risk-scoring layer evaluates project indicators and produces a risk score that can be used to prioritize projects for closer monitoring.

Potential indicators include:

* Cost deviation
* Fund utilization
* Project delay
* Financial progress
* Physical progress
* Progress mismatch
* Inspection frequency
* Other project-level indicators

Example:

```text
Cost Deviation        → High
Project Delay         → High
Progress Mismatch     → Medium
Inspection Frequency  → Low

             ↓

        Risk Score
             ↓

       HIGH RISK
```

The score is intended to support **prioritization and human review**, not automatically determine wrongdoing.

---

# 📊 Monitoring & Analytics

The platform can provide project-level and aggregate information such as:

* Total projects
* Completed projects
* Ongoing projects
* Delayed projects
* Project expenditure
* Fund utilization
* Risk distribution
* Project statistics
* Location-based information

These APIs can be consumed by the frontend dashboard to create interactive monitoring and visualization components.

---

# 🤖 ML Integration

The current backend is structured to support future integration with machine-learning based anomaly detection.

A planned architecture is:

```text
Project Data
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
ML Model
     ↓
Anomaly Score
     ↓
Risk Engine
     ↓
Explainable Result
```

Possible future approaches include unsupervised anomaly-detection techniques such as **Isolation Forest**.

### Important

The current backend should not be interpreted as a production fraud-detection system.

The ML integration is designed as an extensible component for future development and experimentation.

---

# 🧮 Risk Indicators

The platform can derive analytical indicators from project data.

### Cost Deviation

```text
(actual_cost - estimated_cost) / estimated_cost
```

### Fund Utilization

```text
utilized_amount / released_amount
```

### Progress Mismatch

```text
financial_progress - physical_progress
```

### Delay Ratio

```text
actual_duration / planned_duration
```

These indicators can be combined by the risk engine to help identify projects requiring additional attention.

---

# 📁 Dataset

The prototype is designed to work with structured project data containing fields such as:

### Project Information

* Project ID
* Project Name
* Project Type
* Work Category
* State
* District
* Constituency
* Location
* Latitude
* Longitude

### Financial Information

* Estimated Cost
* Sanctioned Amount
* Released Amount
* Utilized Amount
* Actual Cost
* Number of Payments

### Timeline

* Sanction Date
* Work Order Date
* Planned Completion Date
* Actual Completion Date
* Delay Days

### Progress

* Physical Progress
* Financial Progress
* Work Status

### Inspection

* Inspection Count
* Last Inspection Date
* Issues Reported
* Issues Resolved

### Contractor / Agency

* Implementing Agency
* Contractor ID
* Contractor Name
* Contract Value

---

# 🧪 Prototype Data

The current prototype uses **synthetic/sample data** for development and testing.

The long-term objective is to integrate verified government datasets, including relevant datasets available through **data.gov.in**, subject to availability, format, licensing, and API/data-access conditions.

This distinction is important because synthetic data is useful for validating the application's architecture and algorithms, but it should not be treated as official MPLADS data.

---

# 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* Pydantic

### Data Processing

* Pandas
* NumPy

### Machine Learning Integration

* Scikit-learn
* Joblib

### Frontend

* React
* Vite
* Tailwind CSS
* Recharts
* React Leaflet

### Database / Future Integration

* PostgreSQL
* Supabase

### Development

* Git
* GitHub
* REST APIs

---

# 📁 Project Structure

```text
mpladguard-ai/
│
├── backend/
│   ├── services/
│   ├── routes/
│   └── ...
│
├── frontend/
│
├── ml/
│
├── docs/
│
├── tests/
│
├── scripts/
│
├── assets/
│
├── .gitignore
│
└── README.md
```

> The exact structure may evolve as the project continues to develop.

---

# 🔄 Development Workflow

The project follows a Git-based collaborative workflow:

```text
Fork
  ↓
Feature Branch
  ↓
Development
  ↓
Commit
  ↓
Push
  ↓
Pull Request
  ↓
Review
  ↓
Merge
```

This repository preserves my backend development work separately from the final team implementation.

---

# 🎯 MVP

The broader MPLADGuard AI MVP focuses on:

* Project monitoring
* Financial analytics
* Risk scoring
* Anomaly-detection integration
* Explainable risk indicators
* Geospatial project monitoring
* Data-driven project prioritization

The backend contribution represented in this repository focuses primarily on the **API, data-processing, risk-analysis, and integration layer**.

---

# 🔮 Future Scope

Potential future improvements include:

* Integration with verified government datasets
* Database-backed project management
* Advanced anomaly-detection models
* Predictive project-delay detection
* Automated risk alerts
* SHAP-based model explainability
* Document verification
* OCR-based document processing
* Contractor network analysis
* Geospatial intelligence
* Satellite imagery analysis
* Computer vision for physical verification
* Mobile application for field inspectors
* Integration with government systems

---

# ⚠️ Responsible AI

MPLADGuard AI is intended to function as a **decision-support system**.

A high-risk score does **not** automatically mean that fraud, corruption, or wrongdoing has occurred.

The appropriate interpretation is:

> **Potential anomaly detected — requires human verification.**

rather than:

> **Fraud confirmed.**

Any real-world investigation or administrative decision should involve appropriate human review, audit procedures, and due process.

---

# 🏆 SIH 2026

**Problem Statement:** 26012

**Project:** MPLADGuard AI

**Objective:**
Use data analytics and AI-assisted techniques to improve monitoring, transparency, anomaly identification, and efficiency in MPLADS implementation.

This project was developed as part of our **Smart India Hackathon 2026** preparation and offline hackathon experience.

---

# 📌 Repository Note

This repository is a **personal fork** of the MPLADGuard AI team project.

It is maintained to showcase my individual backend development work and contribution to the project.

For the team's main project and final integrated implementation, refer to the original team repository.

---

## 🛡️ MPLADGuard AI

**AI-Assisted Monitoring for Transparent & Efficient Public Development**

**Backend implementation by Rohan Jagdale**

*Built as part of an SIH 2026 project.*

## 🛡️ MPLADGuard-AI

**AI-Assisted Monitoring for Transparent & Efficient Public Development**

Made for SIH 2026.
