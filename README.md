```markdown
<p align="center">
  <img src="assets/watermarked_img_15720235880708124788.png" width="160" alt="MPLADGuard-AI Icon">
</p>

<h1 align="center">🛡️ MPLADGuard-AI</h1>

<p align="center">
  <b>AI-Powered Monitoring, Anomaly Detection & Risk Intelligence Platform for MPLADS</b>
</p>

<p align="center">
  SIH 2026 • Problem Statement SIH26102
</p>

---

## 🎯 About

MPLADGuard-AI is an AI-powered platform designed to detect potential anomalies, fraud indicators, and inefficiencies in the implementation of the Members of Parliament Local Area Development Scheme (MPLADS).

The platform analyzes project, financial, execution, inspection, contractor, procurement, and document-related data to identify projects that require further investigation.

> **Note:** A high-risk score does not prove fraud. It indicates that the project requires further human verification.

---

## 🚨 Problem

MPLADS involves thousands of development projects implemented across different regions through multiple agencies and stakeholders.

Manual monitoring makes it difficult to quickly identify:

* Unusual project costs
* Financial irregularities
* Delayed projects
* Fund utilization anomalies
* Financial vs. physical progress mismatch
* Insufficient inspections
* Unusual contractor patterns
* Procurement anomalies
* Document inconsistencies

MPLADGuard-AI aims to make this monitoring process faster, smarter, and data-driven.

---

## 💡 Solution

MPLADGuard-AI combines:

* 📊 **Project & Financial Analytics**
* 🤖 **AI-Based Anomaly Detection**
* ⚠️ **Explainable Risk Scoring**
* 📄 **Document Verification**
* 🗺️ **Geospatial Monitoring**

### Basic Workflow


```

Project Data ➔ Data Processing ➔ Feature Engineering ➔ Machine Learning ➔ Anomaly Detection ➔ Risk Score ➔ Explainable Results ➔ Dashboard ➔ Human Investigation

```

---

## 🚀 Key Features

### 1. 📊 Monitoring Dashboard

Centralized dashboard showing:

* Total projects, sanctioned funds, and utilized funds
* Completed, ongoing, and delayed project metrics
* High-risk projects breakdown
* Financial analytics and risk distribution

### 2. 🤖 AI Anomaly Detection

The ML system analyzes project data and identifies unusual patterns using unsupervised anomaly detection models like **Isolation Forest**.

Important features evaluated:

* Estimated vs. Actual cost
* Sanctioned vs. Released vs. Utilized amount
* Planned vs. Actual duration (Delay metrics)
* Physical vs. Financial progress ratio
* Inspection counts, contractor history, and procurement data

#### Example Analysis

```text
Estimated Cost: ₹20 Lakh          Actual Cost: ₹32 Lakh
Planned Duration: 8 Months        Actual Duration: 17 Months
Physical Progress: 45%            Financial Progress: 88%
Inspection Count: 1

RESULT ➔ Risk Score: 87/100 — HIGH RISK

```

### 3. 🔍 Explainable Risk Analysis

The system provides detailed explanations behind every risk score generated:

* High cost deviation
* Large project delay
* Financial and physical progress mismatch
* Low inspection frequency
* Abnormal fund utilization

This makes the AI output intuitive and actionable for inspecting officials.

### 4. 📄 Document Verification

The platform cross-verifies financial figures across project documents:

* Work Orders & Administrative Sanctions
* Technical Sanctions & Bills
* Utilization Certificates & Completion Certificates
* Inspection Reports

```text
Document Amount: ₹28 Lakh  |  Database Amount: ₹22 Lakh
STATUS ➔ Potential Financial Discrepancy Flagged

```

### 5. 🗺️ Geospatial Monitoring

Projects are mapped visually using risk-coded indicators:

* 🟢 **Low Risk**
* 🟠 **Medium Risk**
* 🔴 **High Risk**

Each interactive point displays project metadata, completion status, and active risk flags.

---

## 🧠 Machine Learning Architecture

### ML Pipeline

```
Raw Project Data ➔ Data Cleaning ➔ Feature Engineering ➔ Feature Matrix ➔ Isolation Forest ➔ Anomaly Score ➔ Risk Engine ➔ Explainable Risk Score

```

### Key Mathematical Metrics

* **Cost Deviation:**

$$\text{Cost Deviation} = \frac{\text{actual\_cost} - \text{estimated\_cost}}{\text{estimated\_cost}}$$


* **Fund Utilization Ratio:**

$$\text{Fund Utilization} = \frac{\text{utilized\_amount}}{\text{released\_amount}}$$


* **Progress Mismatch:**

$$\text{Progress Mismatch} = \text{financial\_progress} - \text{physical\_progress}$$


* **Delay Ratio:**

$$\text{Delay Ratio} = \frac{\text{actual\_duration}}{\text{planned\_duration}}$$


* **Inspection Gap:**

$$\text{Inspection Gap} = \text{days\_since\_last\_inspection}$$


* **Cost Per Beneficiary:**

$$\text{Cost Per Beneficiary} = \frac{\text{actual\_cost}}{\text{estimated\_beneficiaries}}$$



---

## 📊 Dataset Structure

The platform processes multi-dimensional project data across categories:

| Category | Key Parameters |
| --- | --- |
| **Project Info** | Project ID, Name, Type, Work Category, Location (State/District/Constituency), GPS Coords |
| **Financials** | Estimated Cost, Sanctioned Amount, Released Amount, Utilized Amount, Payment Counts |
| **Timeline** | Sanction Date, Work Order Date, Planned & Actual Completion Dates, Delay Days |
| **Progress & Audits** | Physical Progress %, Financial Progress %, Inspection Count, Reported Issues |
| **Contractor & Bidding** | Implementing Agency, Contractor ID/Name, Tender ID, Bid Count, Price Variance |

---

## 🏗️ System Architecture

```
                       ┌─────────────────────────┐
                       │   React + Vite Frontend │
                       └────────────┬────────────┘
                                    │
                       ┌────────────▼────────────┐
                       │     FastAPI Backend     │
                       └────────────┬────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         │                          │                          │
┌────────▼────────┐        ┌────────▼────────┐        ┌────────▼────────┐
│    Database     │        │    ML Engine    │        │ Document Engine │
│   (Supabase)    │        │  (Scikit-Learn) │        │   (PDF / OCR)   │
└────────┬────────┘        └────────┬────────┘        └────────┬────────┘
         │                          │                          │
         └──────────────────────────┼──────────────────────────┘
                                    │
                       ┌────────────▼────────────┐
                       │       Risk Engine       │
                       └────────────┬────────────┘
                                    │
                       ┌────────────▼────────────┐
                       │   Executive Dashboard   │
                       └─────────────────────────┘

```

---

## 🛠️ Technology Stack

* **Frontend:** React, Vite, Tailwind CSS, Recharts, React Leaflet
* **Backend:** Python, FastAPI, Pydantic
* **Machine Learning:** Python, Pandas, NumPy, Scikit-learn, Joblib
* **Database & Storage:** PostgreSQL, Supabase
* **Utilities:** Git, GitHub, OpenStreetMap, Tesseract OCR / PDFPlumber

---

## 📁 Project Structure

```text
mpladguard-ai/
├── frontend/             # React application source code
├── backend/              # FastAPI application endpoints
├── ml/                   # Machine learning models & training scripts
├── docs/                 # Documentation and API specs
├── tests/                # Automated test suites
├── scripts/              # Utility & deployment scripts
├── assets/               # Logos, diagrams, and icon media
│   └── watermarked_img_15720235880708124788.png
├── .gitignore
└── README.md

```

---

## 👥 Team Collaboration Workflow

We utilize a structured Git flow strategy:

```
Fork ➔ Feature Branch ➔ Pull Request ➔ Code Review ➔ Merge to Main

```

The `main` branch remains protected and stable. Every feature development occurs on isolated branches to ensure continuous delivery.

---

## 🎯 MVP Roadmap

* [x] Core Project & Financial Dashboard Setup
* [x] AI Anomaly Detection Engine (Isolation Forest)
* [ ] Explainable Risk Factor Generator
* [ ] Basic Document OCR Cross-Verification
* [ ] Geospatial Constituency Heatmap

---

## 🔮 Future Scope

* Satellite imagery cross-verification using Computer Vision
* Mobile application for on-site field inspector verification
* Real-time integration with national procurement databases
* SHAP (SHapley Additive exPlanations) for enhanced AI transparency
* Direct integration with MoSPI eSAKSHI portals

---

## ⚠️ Responsible AI Principles

MPLADGuard-AI functions strictly as an automated **decision-support system**.

A high-risk project flag does **not** equal confirmed fraud. The system reports *"Potential anomaly detected — requires human verification"* to assist government auditors and protect due process.

---

## 🏆 SIH 2026

* **Problem Statement:** SIH26102
* **Ministry:** Ministry of Statistics and Programme Implementation (MoSPI)
* **Project Name:** MPLADGuard-AI
* **Objective:** Leverage AI and advanced analytics to optimize monitoring, anomaly detection, transparency, and efficiency in MPLADS delivery.

```

```
