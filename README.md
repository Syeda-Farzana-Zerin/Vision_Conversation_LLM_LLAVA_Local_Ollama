# 🖼️ Image Q&A with LLaVA (Local Ollama + Streamlit)

A simple, fully local web application that lets you **upload an image**, display it instantly, and then **ask questions about it using natural language**.  
Powered by **Ollama** running the **LLaVA vision-language model** locally — no cloud, no API keys, fully private.

This app provides:
- 🖼️ Image upload & display  
- 💬 Chat window with persistent history  
- 🤖 Visual question answering using LLaVA  
- 🔐 100% local inference (Ollama)  
- ⚡ Fast, lightweight and easy to run  

---

## 🚀 Features

### ✔ Upload an Image  
Drag & drop or browse any `.png`, `.jpg`, or `.jpeg`.

### ✔ Ask Questions About the Image  
The model can answer things like:
- “What objects are in this room?”
- “Describe the setting.”
- “Is this a kitchen or living room?”
- “What colors dominate the scene?”

### ✔ Full Chat Memory  
Your messages and the AI replies stay visible on the page.

### ✔ Local Vision LLM (LLaVA)  
Runs locally via **Ollama**, ensuring:
- No data leaves your device  
- Faster inference  
- Works offline  

## 🛠 Requirements

### 1. Install Python packages
pip install streamlit pillow

### 2. Install Ollama (if not installed)
Download for Windows, macOS, or Linux:
https://ollama.com/


### Pull the LLaVA model
ollama pull llava

## ▶️ Running the App
streamlit run VisionLLM_Image.py

