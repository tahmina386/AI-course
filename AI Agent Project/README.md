# AI Research Agent: ReAct with Structured Output

This project implements an autonomous AI Research Agent using the **LangChain** framework and the **Gemini 2.5 Flash** model. The agent follows the **ReAct (Reasoning and Acting)** pattern to strategically decide which external tools to use (Web Search, Wikipedia) to gather information and ensure the final output is delivered in a structured format.

---

##  Core Features

* **ReAct Agent:** The agent uses a sophisticated **Thought/Action/Observation** loop to plan complex research steps before reaching a final answer.
* **Multi-Tool Access:** Utilizes three tools:
    * `web_search` (DuckDuckGo)
    * `wikipedia_lookup`
    * Custom **`save_tool`** (saves final data locally).
* **Structured Output (Pydantic):** Guarantees the final findings adhere to a strict **`ResearchResponse` JSON schema**, ensuring clean, predictable data.
* **Self-Termination:** The `AgentExecutor` is configured to **stop** its loop immediately after the data is successfully saved by the `save_tool`, ensuring efficiency.

---

## How to Run the Agent

### 1. Prerequisites

Ensure you have **Python 3.9+** installed.

### 2. Setup and Navigation

1.  Open your **`AI Agent`** project folder in VS Code.
2.  Open the integrated terminal.

### 3. API Key Configuration

The agent requires a **Google API Key** for the Gemini model.

1.  Create a file named **`.env`** in the root of your project directory.
2.  Add your key to this file:

    ```env
    # .env
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"
    ```

### 4. Install Dependencies

Run the following command in the VS Code terminal to install all necessary libraries with their tested versions:

```bash
pip install langchain==0.1.20 langchain-core==0.1.52  
langchain-community==0.0.38 langchain-google-genai==0.0.8  
pydantic python-dotenv
```
### 5. Execution
Run the main Python script from your terminal:

```bash
python main.py
```  

The script will launch and prompt you for input:
```
--- Agent is Ready ---
What can i help you research?  
```
Type your research question (e.g., "History of the ReAct prompting framework") and press Enter.  

---

## Sample Screenshots  
1.  
<img src="Screenshot 2025-11-18 003453.png" width="750" height="950"/>  
<img src="Screenshot 2025-11-18 003541.png" width="750" height="950"/>  
2.  
<img src="Screenshot 2025-11-18 004212.png" width="750" height="950"/>  
<img src="Screenshot 2025-11-18 004232.png" width="750" height="950"/>  
