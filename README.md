# CommandCopilot

AI-powered assistant for IT support engineers that suggests commands and diagnostics.

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the app

```bash
uvicorn main:app --reload
```

### 3. Test it

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

Use the `/analyze` endpoint to test ticket input.

---

## 🔧 Coming Soon

- Azure AI Agent Service integration
- Real command suggestions based on ticket context
- Optional integration with Azure Functions