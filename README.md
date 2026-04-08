# Claude-Powered FinOps Agent

Traditional FinOps stops at reporting.

This project explores a different approach:
treating cloud cost as a **reasoning problem**.

---

## 🧠 What This System Does

This agent analyzes AWS Lambda cost anomalies in three layers:

### 1. Detection Layer
Identifies significant cost spikes based on variance thresholds.

### 2. Driver Analysis Layer
Breaks cost into real infrastructure drivers:
- Invocation count
- Execution duration
- Memory allocation

### 3. Claude Reasoning Layer
Uses AI to translate metrics into **engineering-level explanations**, including:
- Root cause
- Technical interpretation
- Recommended actions

---

## 🔍 Example Insight

A 112% Lambda cost increase was analyzed as:

- Invocation volume: +2% (flat)
- Execution duration: +108% (**primary driver**)
- Memory: unchanged

👉 Insight:
Same workload, but execution time doubled.

This indicates:
- downstream latency
- inefficient code paths
- or dependency degradation

---

## ⚡ Why This Matters

Engineers don’t optimize “cost”

They optimize:
👉 system behavior

This system bridges that gap by turning cost signals into **actionable engineering insight**.

---

## 🚀 What’s Next

- Jira-ready ticket generation
- Slack alert integration
- Multi-service expansion (EC2, RDS, DynamoDB)

---

## 👩🏽‍💻 Author

Dr. Christine  
Cloud FinOps Leader | RevealCostAI
