# 📬 Multi-Agent AI Classifier & Router

A modular multi-agent AI system that classifies documents (PDF, JSON, Email), determines their intent (e.g., Invoice, RFQ, Complaint), routes them to the appropriate agent for processing, and maintains shared context using Redis for traceability.

---

## 📁 Project Structure

```
multi_agent_system/
├── agents/
│ ├── classifier_agent.py
│ ├── json_agent.py
│ └── email_agent.py
├── memory/
│ └── memory_client.py
├── utils/
│ ├── format_detector.py
│ └── intent_classifier.py
├── schemas/
│ └── target_schema.py
├── main.py
├── streamlit_app.py
└── README.md

```


## 🧠 Agents

| Agent            | Description                                              |
|------------------|----------------------------------------------------------|
| `classifier_agent.py` | Detects format and intent, routes input              |
| `json_agent.py`       | Processes structured JSON, validates fields          |
| `email_agent.py`      | Uses Gemini LLM to extract sender, summary, urgency  |

---

## 🗃️ Shared Memory (Redis)

The system uses a Redis-based memory module to store:

- Source type and timestamp
- Sender or thread ID
- Extracted fields (e.g., urgency, items)
- Routing and processing results

Accessible across all agents for context persistence and traceability.

---

## ✅ Features

- Input format detection (Email / JSON / PDF)
- Intent classification (RFQ, Invoice, Complaint, Regulation)
- Modular agent-based processing
- LLM (Gemini) integration for summarizing and urgency detection
- Redis shared memory
- Streamlit UI for manual testing

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/namanomar/multi-agent
cd multi-agent-ai-router
```
### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Create a .env File
### 4. Run application
```
streamlit run main.py
```