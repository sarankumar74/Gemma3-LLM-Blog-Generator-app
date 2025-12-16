# ✍️ Gemma3 LLM Blog Generator App
🔍 *Local LLM • Blog Generation • Ollama • LangChain • Streamlit*

## 🚀 Tech Stack & Domains
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![LLM](https://img.shields.io/badge/LLM-Gemma3%201B-brightgreen)
![Ollama](https://img.shields.io/badge/Runtime-Ollama-black)
![LangChain](https://img.shields.io/badge/Framework-LangChain-purple)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red?logo=streamlit)
![Domain](https://img.shields.io/badge/Domain-NLP%20%26%20Content%20Generation-navy)

---

## 📘 Overview
This project is a **local LLM-based blog generator application** built using **Gemma3 (1B)** running via **Ollama**.

Users can generate blog content by providing a topic or brief input. The system allows control over **word count**, **target audience**, and **system prompt mode**, making the generated content more aligned with the intended readers.

All generation happens locally without relying on cloud APIs.

---

## 🎯 Problem Statement
Content creation often requires time, writing skill, and audience awareness. Existing tools mostly depend on cloud-based LLMs, which introduce cost, latency, and privacy concerns.

This project provides:
- Fully local blog generation  
- Audience-aware content creation  
- Custom system prompt control  

Without external API dependency.

---

## 💼 Use Cases
| Use Case | Description |
|--------|-------------|
| ✍️ Blog Writing | Generate structured blog posts from short inputs |
| 🎓 Education | Create student-friendly or research-focused content |
| 🧑‍🏫 Teaching | Produce explanations tailored for teachers |
| 🧪 Experimentation | Test prompt engineering with local LLMs |

---

## 🧠 Blog Generation Controls
Users can customize output using:

### Audience Type
- Researcher  
- Student  
- Teacher  
- Common people  

### Word Count
- User-defined length  

### System Prompt Mode
- Default assistant  
- Custom instruction prompts  

---

## 🗺️ Project Workflow

### 🧾 1 — User Input
- Blog topic or short content
- Select word count
- Choose audience type
- Choose system prompt mode

### 🤖 2 — Prompt Construction
- LangChain builds structured prompts
- System + user prompts combined

### 🧠 3 — Blog Generation
- Gemma3 (1B) runs locally via Ollama
- Generates blog content based on constraints

### 🌐 4 — UI Output
- Streamlit displays generated blog
- Instant regeneration with new settings

---



---

<summary>📸 Click to view Streamlit UI screenshots</summary>

#### Home Page  
![Home Page](https://github.com/user-attachments/assets/467a4508-bb6e-4cc8-a3bf-b7b912b19288)



#### Results Page  1
![Result Page](https://github.com/user-attachments/assets/a9e49020-8a5b-4e57-a024-a5cfb0ae2609)




#### Results Page  1
![Result Page](https://github.com/user-attachments/assets/86ec1e5b-b712-45bb-a199-343b0dcff8e4)


---


## 📁 Project Structure
```
Bank-Term-Deposit-Prediction/  
│
│ 
├── Local LLM Code /  
│   └── chatbot.py 
│  
├── app/  
│   └── app.py  
│  
├── requirements.txt  
└── README.md  

```
---

## 🛠️ Installation & Execution

Clone repository:
```
git clone https://github.com/sarankumar74/Gemma3-LLM-Blog-Generator-app.git
cd Gemma3-LLM-Blog-Generator-app
```

Install dependencies:
```
pip install -r requirements.txt
```

Run Streamlit app:
```
streamlit run app/app.py
```
