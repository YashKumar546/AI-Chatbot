# 🤖 AI Chatbot using Flask & Machine Learning

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn)
![NLTK](https://img.shields.io/badge/NLTK-Natural%20Language%20Processing-green?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5)
![CSS](https://img.shields.io/badge/CSS3-Styling-1572B6?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-Interactive-F7DF1E?style=for-the-badge&logo=javascript)

---

## 📖 Overview

This project is an AI-powered chatbot built using **Python**, **Flask**, **Natural Language Processing (NLP)**, and **Machine Learning**.

The chatbot classifies user messages into predefined intents using **TF-IDF Vectorization** and a **Logistic Regression** model, then generates an appropriate response through an interactive web interface.

The project demonstrates the complete machine learning workflow, from dataset preparation and model training to deployment with Flask.

---

## ✨ Features

- 🤖 AI-powered intent classification
- 🧠 NLP preprocessing using NLTK
- 📊 TF-IDF Vectorization
- 📈 Logistic Regression classifier
- 🌐 Interactive Flask web application
- 💬 Real-time chatbot responses
- 📂 Modular project structure
- 📓 Jupyter Notebook for model training
- 🚀 Easy to extend with new intents

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- NLTK
- Pandas
- NumPy
- HTML
- CSS
- JavaScript

---

# 🧠 Machine Learning Workflow

```
User Input
     │
     ▼
Text Preprocessing
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Logistic Regression Model
     │
     ▼
Predicted Intent
     │
     ▼
Chatbot Response
```

---

# 📂 Project Structure

```text
AI-Chatbot/
│
├── model/
│   ├── chatbot_model.pkl
│   ├── label_encoder.pkl
│   └── vectorizer.pkl
│
├── notebook/
│   └── Chatbot_Training.ipynb
│
├── screenshots/
│   ├── home.png
│   └── chat-demo.png
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── chatbot.py
├── intents.json
├── train.py
├── test_chatbot.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Chatbot.git
cd AI-Chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python train.py
```

### Run the Flask Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 💬 Sample Queries

```
Hi

What is Python?

Explain AI

Tell me a joke

Thanks

Goodbye
```

---

# 📸 Screenshots

## Home Page

![Home Page](screenshots/screenshots/home.png)

---

## Chat Demo

![Chat Demo](screenshots/screenshots/chat-demo.png)

# 📈 Future Improvements

- Voice-based interaction
- Deep Learning (LSTM/BERT)
- Database integration
- User authentication
- Chat history
- Multi-language support
- Dark/Light theme toggle
- Integration with external APIs

---

# 👨‍💻 Author

**Yash Kumar**

B.Tech Computer Science Engineering

Passionate about Artificial Intelligence, Machine Learning, Python, and Full-Stack Development.

---

## ⭐ If you found this project useful, consider giving it a Star!
