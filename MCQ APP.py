# Importing needed libraries
import streamlit as st
import openai

def questionsGeneration(topic, num_questions, openai_api_key): #Defining a function to be used to generate quiz's questions
    openai.api_key = openai_api_key #assign the object of openai with the API key

    questions = [] #Create a list to store the questions
    try: #Start catching error technique to debug

         prompt = f"Create {num_questions} multiple choice questions about {topic} with 4 answer choices." #Define the prompt that gpt will take.
         response = openai.completions.create(model="gpt-3.5-turbo",prompt=prompt,max_tokens=150,n = 1,temperature=0.7) #generate the defined prompt
            
         question, *answers = response.split('\n') #Make two lines, the first for the questions and the second for the answers
         questions.append[[question, answers]] #put the question and its answers to the questions list
           
    except Exception as e:
        print(f"Here is the API issue: {e}")
        return []

    return questions

def main(): #Main function
    st.title("Multiple-Choice Quiz Application") #Set the title of the interface

    topic = st.text_input("Enter the quiz topic:") #Variable assigned of the user input about the type of the quiz.
    num_questions = st.number_input("Enter the number of questions:", min_value=1, max_value=10, value=5) #Variable assigned of the user input about questions numbers.

    if st.button("Generate Quiz"): #When pressing the button
        with st.spinner('Generating questions...'): #print this statement as waiting message
            
            questions = questionsGeneration(topic, num_questions, 'TheGeneratedAPI') #variable to hold the function with the user's inputs and the API key.

        score = 0 #To track user's score
        for i, (question, answers, correct_answer) in enumerate(questions):
            st.write(f"Q{i+1}: {question}") #To write the question number and the question itself
            user_answer = st.radio(f"Options for Q{i+1}:", answers, key=f"question_{i}") #buttons to let the user able to choose an answer

            if user_answer == correct_answer:
                score += 1

        if st.button("Submit Quiz"): #When pressing this button
            st.write(f"Your score: {score}/{num_questions}") #Print the score
main() 