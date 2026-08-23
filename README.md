# RAG-system
A robust Retrieval-Augmented Generation (RAG) system built with **FastAPI** and **LangChain**, designed for efficient document processing and intelligent querying.

## Requirements

To run this project, you will need:
* **Python 3.10.x or higher** (Tested and developed on version **3.10.11**)
* **Git** installed on your machine

---

### How to Install Python

If you don't have Python installed yet, follow these steps:

1. **Download Python:**
   Go to the official website [python.org](https://www.python.org/downloads/) and download **Python 3.10.11** (or any 3.10.x version).

2. **Run the Installer:**
   * **Crucial Step:** During installation, make sure to check the box that says **"Add Python to PATH"** at the bottom of the window.
   * Click **Install Now**.

3. **Verify Installation:**
   Open your terminal (Command Prompt, PowerShell, or VS Code Terminal) and type:
   ```bash
   python --version
   ```

## Getting Started

### 1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd RAG-system
   ```

### 2. Create a Virtual Environment (venv)
    python -m venv venv
    
### 3. Activate the Virtual Environment:

    .\venv\Scripts\activate
    
### 4. Navigate to the source folder:

    cd src

### 5. Install Dependencies
    
    pip install -r requirements.txt
    
### 6. Setup the environment variables
    
    Copy-Item .env.example .env
    
Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

### 7. Run the FASTAPI server 

```bash
uvicorn main:app --reload --host 0.0.0.0
```
Open your browser or API client (like Postman) and go to:

Local URL: http://127.0.0.1:8000

Interactive Docs (Swagger): http://127.0.0.1:8000/docs
