# Margin Visibility Portal (MVP)

## Overview

This project is a Proof of Concept (POC) for a Margin-Aware Deal Desk Copilot designed for staffing organizations.

The objective of the MVP is to provide sales representatives with real-time visibility into the margin impact of pricing decisions during negotiations. By making profitability visible at the point of decision, representatives can make more informed pricing decisions while maintaining sales velocity.

## How It Works

The application simulates integrations with existing business systems:

* CRM System (source of bill rates)
* ATS / Payroll System (source of labor costs)

A sales representative selects a deal and enters a proposed discount. The system retrieves the corresponding pricing and cost information, calculates the estimated gross margin, and immediately displays the result together with a simple risk classification.

### Margin Formula

```text
Margin % = (Price - Cost - Discount) / Price
```

## MVP Scope

This Proof of Concept focuses exclusively on validating a single business assumption:

> Providing real-time margin visibility during negotiations improves pricing discipline and protects profitability.

The MVP intentionally excludes:

* AI-generated recommendations
* Historical deal analysis
* Workflow automation
* Deal approvals
* CRM customizations
* Notifications and escalations

These capabilities are introduced in subsequent phases of the proposed solution.

## Running the Application

### Option 1: Run Locally

Install dependencies:

```bash
uv sync
````

Start the application:

```bash
uv run streamlit run app.py
```

The application will be available at:

http://localhost:8501


### Option 2: Run with Docker

Build the image:

```bash
docker build -t margin-visibility-portal .
```

Run the container:

```bash
docker run -p 8501:8501 margin-visibility-portal
```

The application will be available at:

```text
http://localhost:8501
```

## Example

| Field      | Value |
| ---------- | ----- |
| Bill Rate  | $100  |
| Labor Cost | $70   |
| Discount   | $10   |

Result:

```text
Margin = 20%
Risk = Medium
```

## Future Enhancements

### Phase 2

* AI Margin Intelligence Assistant
* Historical Deal Intelligence Repository
* Margin recommendations and explanations

### Phase 3

* Multi-agent architecture
* Automated processing of low-risk deals
* Human-in-the-loop approval workflows

## Disclaimer

This application is a simplified Proof of Concept created for a technical assessment and uses simulated business data for demonstration purposes.
