# AI Health Assistant & Diet Recommendation System

A Streamlit-based AI health and nutrition assistant that calculates BMI, BMR, TDEE, and estimated daily calorie requirements, and uses those results to generate simple one-day diet recommendations.

The project also includes a nutrition chatbot that uses Retrieval-Augmented Generation (RAG) to provide answers based on a nutrition knowledge source.

> **Disclaimer:** This project is intended for educational and general wellness purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

## Overview

The application combines basic nutrition calculations, a nutrition knowledge base, RAG, and an AI language model to provide personalized wellness-oriented responses.

The user provides information such as:

- Age
- Gender
- Height
- Weight
- Activity level
- Goal
- Diet type
- Food allergies

The application then calculates:

- BMI (Body Mass Index)
- BMR (Basal Metabolic Rate)
- TDEE (Total Daily Energy Expenditure)
- Estimated daily calorie requirements

These values are used along with the user's preferences and restrictions to generate a simple one-day meal plan.

## Features

### Health & Nutrition Chatbot

Users can ask general questions about nutrition and healthy eating.

Examples:

- What are good sources of protein?
- What foods are high in fiber?
- Why is hydration important?
- What are some healthy snack options?
- How can I increase my daily protein intake?

The chatbot uses relevant information retrieved from the project's nutrition knowledge base when generating its response.

### Personalized Diet Recommendations

The application generates a one-day meal plan based on the user's information and preferences.

The plan includes:

1. Breakfast
2. Morning snack
3. Lunch
4. Evening snack
5. Dinner

Each meal includes approximate:

- Food items
- Portions
- Calories
- Protein

The recommendation can take into account the user's goal, diet type, and food allergies.

### Nutrition Calculations

The application calculates several commonly used nutrition metrics.

**BMI**


BMI = weight (kg) / height² (m²)

BMR

The application uses the Mifflin-St Jeor equation to estimate basal metabolic rate.

For males:

BMR = 10 × weight + 6.25 × height - 5 × age + 5

For females:

BMR = 10 × weight + 6.25 × height - 5 × age - 161

TDEE

TDEE = BMR × Activity Factor

These calculations are estimates and should not be treated as precise measurements of an individual's nutritional requirements.


## RAG Pipeline

The project uses Retrieval-Augmented Generation (RAG) to provide the AI model with relevant nutrition information.

The general flow is:

Nutrition PDF
     ↓
Document Processing
     ↓
FAISS Vector Database
     ↓
Relevant Context Retrieval
     ↓
Prompt Construction
     ↓
AI Model
     ↓
Response

The nutrition knowledge source is stored in the data/ directory, while the FAISS vector database is generated locally from that source.

The vector database is intentionally not included in the repository because it can be recreated using the database creation script.


## Project Structure
ai_health_assistant_project/
│
├── app.py
├── diet.py
├── rag.py
├── create_database.py
├── llm_test.py
├── prompt.md
├── readme.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── nutrition.pdf
│
└── vector_db/
    ├── index.faiss
    └── index.pkl

The env/, .env, apis.txt, __pycache__/, and generated vector_db/ files are excluded from version control.

## Technology Stack


Python
Streamlit
FAISS
RAG (Retrieval-Augmented Generation)
Large Language Model API
Hugging Face
python-dotenv
Nutrition knowledge base in PDF format