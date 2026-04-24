#  AI Workflow Automation Engine (Agentic Task Executor)

An intelligent multi-agent system that converts natural language goals into executable workflows using **Gemini AI**, dynamic tool execution, and a React-based dashboard.

---

##  Features

*  Natural Language Goal Understanding (Gemini)
*  Multi-Step Task Planning
*  Dynamic Tool Execution (APIs, custom tools)
*  AI-Based Evaluation of Results
*  Context-Aware Workflow (step-to-step data flow)
*  Execution Logs Dashboard (React UI)
*  Memory + History Tracking

---

##  Architecture

```
User Goal
   ↓
Planner Agent (Gemini)
   ↓
Executor Agent (Tools + Context)
   ↓
Evaluator Agent (Gemini)
   ↓
Memory + History
   ↓
Execution Logs (UI)
```

---

## 📁 Project Structure

```
ai-workflow-engine/
│
├── backend/
│   ├── src/
│   │   ├── agents/
│   │   ├── memory/
│   │   ├── tools/
│   │   ├── utils/
│   │
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 1. Clone the Repository

```
git clone https://github.com/MAvinash24/ai-workflow-engine.git
cd ai-workflow-engine-main
cd ai-workflow-engine
```

---

### 🔹 2. Backend Setup (Python)

```
cd backend
pip3 install -r requirements.txt
```

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

Run backend:

```
python -m uvicorn main:app --reload
```

Backend will run at:
 http://127.0.0.1:xxxx

---

### 🔹 3. Frontend Setup (React + Vite)

```
cd frontend
npm install
npm run dev
```

Frontend will run at:
 http://localhost:xxxx

---

##  Usage

1. Open the frontend in your browser
2. Enter a goal like:

```
Fetch data, summarize it, and notify
```

3. View step-by-step execution logs in real time

---

## 💡 Example Workflow

### Input:

```
Fetch posts, summarize them, and store the result
```

### Output:

* Fetch data from API
* Summarize using Gemini
* Store processed data
* Evaluate each step

---

## 🛠️ Tech Stack

* **Backend:** FastAPI, Python
* **Frontend:** React (Vite)
* **AI Model:** Google Gemini
* **Tools:** Requests, Custom Tool Layer
* **State Management:** In-memory context + history

---

##  Description

> Built a multi-agent AI workflow automation engine capable of planning, executing, and evaluating multi-step tasks using Gemini, dynamic tool invocation, and context-aware reasoning with a React-based monitoring dashboard.

---

## 🔥 Future Improvements

* Drag-and-drop workflow builder (like n8n)
* MongoDB for persistent memory
* Authentication (JWT)
* Live streaming execution logs
* Tool registry (LangChain-style)

---

## ⚠️ Notes

* Ensure backend is running before using frontend
* Add CORS middleware in FastAPI if needed
* Use valid Gemini API key

---

##  Author

Avinash

---
