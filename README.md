AI Chatbot using FastAPI and NLP

An intent-based chatbot built using Python, FastAPI, NLTK, and Machine Learning.

Features
- Intent classification
- Rule-based responses
- REST API using FastAPI
- Swagger UI testing

Technologies Used
- Python
- FastAPI
- scikit-learn
- NLTK

Steps to Run
1. Clone Repository

git clone <your-github-link>
cd chatbot_project

2. Create Virtual Environment
python -m venv venv

3. Activate Environment (CMD)
venv\Scripts\activate.bat

4. Install Requirements
pip install -r requirements.txt

5. Train Model
cd model
python train.py

6. Run FastAPI Server

cd ../app
uvicorn main:app --reload

7. Open Swagger UI
Open in browser:
http://127.0.0.1:8000/docs
