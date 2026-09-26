## GRAPHICAL INTTERFACE ####
import streamlit as st
import os
from diet import bmi_calculator, bmr_calculator, calorie_target, tdee_calculator
from dotenv import load_dotenv
from openai import OpenAI
from rag import load_rag

### LLM

### Accessing the API Key from the Token
load_dotenv()
HF_token = os.getenv("HF_TOKEN")

client = OpenAI(
    base_url = "https://router.huggingface.co/v1",
    api_key = HF_token
    )



# st.page_setup(
#     page_title = "Your AI Health Assistant!", 
#     page_icon = "👍", 
#     layout = "wide"
#     )

st.set_page_config(
    page_title="Your AI Health Assistant!",
    page_icon="👍",
    layout="wide"
)
st.title("👍Your AI Health Assistant!")
st.header("Didn't you become a little fat than yesterday? Check!")

st.write("Personal Heatlh Assistance and Diet Recommendation System")

st.sidebar.header("Your Information")

gender = st.sidebar.selectbox("Select your Gender", ["male", "female"])
age = st.sidebar.number_input("Enter your Age", 1, 100)
weight = st.sidebar.number_input("Enter your Weight (in kg)", 1, 200)
height = st.sidebar.number_input("Enter your Height (in cm)", 100, 250)
activity = st.sidebar.selectbox("Select your Activity Level", 
                                ["Sedentary", 
                                 "Lightly_Active", 
                                 "Moderately_Active", 
                                 "Very_Active", 
                                 "Extra_Active"])
aim = st.sidebar.selectbox("Select your Aim", ["weight maintain", "weight loss", "weight gain"])
diet_type = st.sidebar.selectbox("Select your Diet Type:", ["Vegetarian", "Non-Vegetarian", "Vegan"])
allergies = st.sidebar.selectbox("Slect your Allergies:", ["Allergic", "None"])

bmi = bmi_calculator(weight, height)
bmr = bmr_calculator(weight, height, age, gender)
tdee = tdee_calculator(bmr, activity)
calorie = calorie_target(tdee, aim)


col1, col2, col3, col4 = st.columns(4)

col1.metric("Your BMI", bmi)
col2.metric("Your BMR",f"{bmr} kcal")
col3.metric("Your TDEE", f"{tdee} kcal")
col4.metric("Your Calorie Target", f"{calorie} kcal")


tab1, tab2 = st.tabs(["Diet Recommendation", "Health Assistance"])

if st.button("Get Recommendations"):
    if client:
        with st.spinner("Creating Diet..."):
            try:
                db = load_rag()
                search_query = f"""
                Diet Type {diet_type}, 
                Healthy Food, 
                Protein, 
                Allergies {allergies}
                """
                # search_query = f"Recommend me a diet plan for {aim} with {calorie} calories."

                docs = db.similarity_search(search_query, 3)
                context = "\n\n".join([doc.page_content for doc in docs])
                prompt = f"""
# **Diet Recommendation Prompt:**

You are a helpful AI nutrition assistant.



Use the following nutrition knowledge

to create a simple one-day diet plan.



NUTRITION KNOWLEDGE:



{context}





USER INFORMATION:



Age: {age}



Gender: {gender}



Height: {height} cm



Weight: {weight} kg



Activity Level: {activity}



aim: {aim}



Diet Type: {diet_type}



Food Allergy: {allergies}



Estimated BMI: {bmi}



Estimated BMR: {bmr} kcal/day



Estimated TDEE: {tdee} kcal/day



Estimated Daily Calorie Target:

{calorie} kcal/day





Create the following:



1\. Breakfast

2\. Morning Snack

3\. Lunch

4\. Evening Snack

5\. Dinner





For every meal provide:



\- Food

\- Portion

\- Approximate calories

\- Approximate protein





IMPORTANT RULES:



\- Respect the user's diet type.

\- Do not recommend foods containing

&#x20; the stated allergy.

\- Use the provided nutrition knowledge

&#x20; when possible.

\- Keep the plan simple and practical.

\- Do not diagnose diseases.

\- Do not prescribe medicines.

\- Do not claim to cure diseases.

\- This is general wellness information,

&#x20; not medical advice.
"""
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                answer = response.choices[0].message.content
                st.markdown(answer)
            except:
                st.error("Error: Unable to generate recommendations. Please try again later.")

if tab2:
    question = st.text_area("Ask about Health", 
                 placeholder = "Eg: Good source of vegetarian protein")
    if st.button ("Ask AI"):
        db = load_rag()
        docs = db.similarity_search(question, 3)
        context = "\n\n".join([doc.page_content for doc in docs])
        prompt = f"""
# **Chatbot Prompt:**
You are an AI health and nutrition assistant.

Use the following knowledge to answer the user's question.

NUTRITION KNOWLEDGE: {context}

USER QUESTION:

{question}





INSTRUCTIONS:



\- Answer clearly.

\- Keep the explanation beginner-friendly.

\- Use the provided knowledge when possible.

\- Do not invent medical facts.

\- Do not diagnose diseases.

\- Do not prescribe medicines.

\- Do not claim to cure diseases.

\- If the question concerns a serious

&#x20; medical problem, recommend consulting

&#x20; a qualified healthcare professional.



This application provides general health

and nutrition information for educational

and wellness purposes.

"""             
        response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                        messages=[
                                    {"role": "user", "content": prompt}
                                ]
                            )
        answer = response.choices[0].message.content
        st.markdown(answer)