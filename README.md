Here is your exact, full-length original `README.md` content restored with every single section, detail, sub-bullet, and math breakdown intact—formatted cleanly with your preferred left-aligned header style.

```markdown
# MPLADGuard-AI 🛡️

> AI-Powered Monitoring, Anomaly Detection & Risk Intelligence Platform for MPLADS

<p align="left">
  <img src="assets/mpladguard-icon.png" width="150" alt="MPLADGuard-AI Icon">
</p>

SIH 2026 • Problem Statement 26012

---

## 🎯 About

MPLADGuard-AI is an AI-powered platform designed to detect potential anomalies, fraud indicators, and inefficiencies in the implementation of the Members of Parliament Local Area Development Scheme (MPLADS).

The platform analyzes project, financial, execution, inspection, contractor, procurement, and document-related data to identify projects that may require further investigation.

> A high-risk score does not prove fraud. It indicates that the project requires further human verification.

---

## 🚨 Problem

MPLADS involves thousands of development projects implemented across different regions through multiple agencies and stakeholders.

Manual monitoring makes it difficult to quickly identify:

- Unusual project costs
- Financial irregularities
- Delayed projects
- Fund utilization anomalies
- Financial vs physical progress mismatch
- Insufficient inspections
- Unusual contractor patterns
- Procurement anomalies
- Document inconsistencies

MPLADGuard-AI aims to make this monitoring process faster, smarter, and data-driven.

---

## 💡 Solution

MPLADGuard-AI combines:

- 📊 Project & Financial Analytics
- 🤖 AI-Based Anomaly Detection
- ⚠️ Explainable Risk Scoring
- 📄 Document Verification
- 🗺️ Geospatial Monitoring

### Basic Workflow

Project Data
↓
Data Processing
↓
Feature Engineering
↓
Machine Learning
↓
Anomaly Detection
↓
Risk Score
↓
Explainable Results
↓
Dashboard
↓
Human Investigation

---

# 🚀 Key Features

## 1. 📊 Monitoring Dashboard

Centralized dashboard showing:

- Total projects
- Total sanctioned funds
- Total utilized funds
- Completed projects
- Ongoing projects
- Delayed projects
- High-risk projects
- Financial analytics
- Risk distribution
- Project statistics

---

## 2. 🤖 AI Anomaly Detection

The ML system analyzes project data and identifies unusual patterns.

Important features include:

- Estimated cost
- Sanctioned amount
- Released amount
- Utilized amount
- Actual expenditure
- Planned duration
- Actual duration
- Delay
- Physical progress
- Financial progress
- Inspection count
- Contractor information
- Procurement information

The initial prototype uses an unsupervised anomaly detection approach such as **Isolation Forest**.

### Example

Estimated Cost: ₹20 Lakh  
Actual Cost: ₹32 Lakh

Planned Duration: 8 Months  
Actual Duration: 17 Months

Physical Progress: 45%  
Financial Progress: 88%

Inspection Count: 1

↓

**Risk Score: 87/100 — HIGH RISK**

---

## 3. 🔍 Explainable Risk Analysis

The system does not only provide a risk score.

It also explains the major factors responsible for the score.

Example:

- High cost deviation
- Large project delay
- Financial and physical progress mismatch
- Low inspection frequency
- Abnormal fund utilization

This makes the AI output easier for officials to understand.

---

## 4. 📄 Document Verification

The platform can analyze project documents such as:

- Work Orders
- Administrative Sanctions
- Technical Sanctions
- Bills
- Utilization Certificates
- Completion Certificates
- Inspection Reports

Example:

Document Amount: ₹28 Lakh  
Database Amount: ₹22 Lakh

→ Potential Financial Discrepancy

The system flags the discrepancy for human verification.

---

## 5. 🗺️ Geospatial Monitoring

Projects can be displayed on an interactive map.

🟢 Low Risk  
🟠 Medium Risk  
🔴 High Risk

Each project can display:

- Project name
- Project type
- Location
- Cost
- Completion status
- Risk score
- Risk indicators

---

# 🧠 Machine Learning

### ML Pipeline

Raw Project Data
↓
Data Cleaning
↓
Feature Engineering
↓
Feature Matrix
↓
Isolation Forest
↓
Anomaly Score
↓
Risk Engine
↓
Explainable Risk Score

### Important Derived Features

Cost Deviation:

(actual_cost - estimated_cost) / estimated_cost

Fund Utilization:

utilized_amount / released_amount

Progress Mismatch:

financial_progress - physical_progress

Delay Ratio:

actual_duration / planned_duration

Inspection Gap:

days_since_last_inspection

Cost Per Beneficiary:

actual_cost / estimated_beneficiaries

---

# 📊 Dataset

The dataset can contain:

### Project Information

- Project ID
- Project Name
- Project Type
- Work Category
- State
- District
- Constituency
- Location
- Latitude
- Longitude

### Financial Information

- Estimated Cost
- Sanctioned Amount
- Released Amount
- Utilized Amount
- Actual Cost
- Number of Payments

### Timeline

- Sanction Date
- Work Order Date
- Planned Completion Date
- Actual Completion Date
- Delay Days

### Progress

- Physical Progress
- Financial Progress
- Work Status

### Inspection

- Inspection Count
- Last Inspection Date
- Issues Reported
- Issues Resolved

### Contractor

- Implementing Agency
- Contractor ID
- Contractor Name
- Contract Value

### Procurement

- Tender ID
- Bid Count
- Winning Bid
- Second Lowest Bid
- Procurement Method

### Impact

- Estimated Beneficiaries
- Population Served

---

# 🔄 Dataset Growth

New verified project data can continuously be added.

10 Projects
↓
20 Projects
↓
30 Projects
↓
50 Projects
↓
100+ Projects

When retraining the model, the accumulated dataset should be used.

For example:

Round 1 → Projects 1–10  
Round 2 → Projects 1–20  
Round 3 → Projects 1–30  
...  
Round 10 → Projects 1–100

Different project categories such as bridges, roads, schools, and water infrastructure can use category-specific features because their normal cost and execution patterns are different.

---

# 🏗️ Architecture

Frontend
React + Vite
↓
FastAPI Backend
↓
┌───────────────┬───────────────┬───────────────┐
│               │               │               │
Database       ML Engine       Document Engine
│               │               │               │
Supabase       Scikit-learn    PDF/OCR
│               │               │               │
└───────────────┴───────────────┴───────────────┘
↓
Risk Engine
↓
Dashboard

---

# 🛠️ Technology Stack

Frontend:
- React
- Vite
- Tailwind CSS
- Recharts
- React Leaflet

Backend:
- Python
- FastAPI
- Pydantic

Machine Learning:
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

Database:
- PostgreSQL
- Supabase

Other:
- Git
- GitHub
- OpenStreetMap
- PDF/OCR tools

---

# 📁 Project Structure

mpladguard-ai/

├── frontend/
├── backend/
├── ml/
├── docs/
├── tests/
├── scripts/
├── assets/
│   └── mpladguard-icon.png
├── .gitignore
└── README.md

---

# 👥 Team Collaboration

We follow:

Fork → Branch → Pull Request → Review → Merge

The main branch remains stable.

Each team member works on their own fork or feature branch and submits a Pull Request before changes are merged into the main repository.

---

# 🎯 MVP

Our initial MVP focuses on:

- [ ] Project & Financial Dashboard
- [ ] AI Anomaly Detection
- [ ] Explainable Risk Analysis
- [ ] Document Verification
- [ ] Geospatial Monitoring

---

# 🔮 Future Scope

- Satellite imagery analysis
- Computer vision for physical verification
- Mobile application for field inspectors
- Real-time CCTV integration
- Advanced contractor network analysis
- Predictive project-delay detection
- Automated alerts
- SHAP-based explainability
- Continuous model retraining
- Government system integrations

---

# ⚠️ Responsible AI

MPLADGuard-AI is a decision-support system.

A high-risk project does NOT automatically mean that fraud has occurred.

The system should report:

"Potential anomaly detected — requires investigation."

rather than:

"Fraud confirmed."

Final decisions must be made through appropriate human verification, audit, and due process.

---

# 🏆 SIH 2026

**Problem Statement:** 26012

**Project:** MPLADGuard-AI

**Objective:** Use AI and data analytics to improve monitoring, anomaly detection, transparency, and efficiency in MPLADS implementation.

---

## 🛡️ MPLADGuard-AI

**AI-Assisted Monitoring for Transparent & Efficient Public Development**

Made for SIH 2026.

```
