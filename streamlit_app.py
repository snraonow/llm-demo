# import gradio as gr

# def greet(name):
#     return "Hello " + name + "!!"

# iface = gr.Interface(fn=greet, inputs="text", outputs="text")
# iface.launch()

import streamlit as st

questions = [
  {
    "question": "What was NVDA's revenue in February 2023?",
    "choices": ["$10 billion", "$11 billion", "$12 billion", "$13 billion"],
    "answer": "$12 billion"
  },
  {
    "question": "What was NVDA's net income in May 2023?",
    "choices": ["$2.5 billion", "$2.6 billion", "$2.7 billion", "$2.8 billion"],
    "answer": "$2.6 billion"
  },
  {
    "question": "What was NVDA's operating income in November 2023?",
    "choices": ["$3.5 billion", "$3.6 billion", "$3.7 billion", "$3.8 billion"],
    "answer": "$3.7 billion"
  },
  {
    "question": "What was NVDA's gross margin in August 2023?",
    "choices": ["61%", "62%", "63%", "64%"],
    "answer": "62%"
  },
  {
    "question": "What was NVDA's research and development expenses in February 2023?",
    "choices": ["$1.3 billion", "$1.4 billion", "$1.5 billion", "$1.6 billion"],
    "answer": "$1.5 billion"
  },
  {
    "question": "What was NVDA's diluted earnings per share in May 2023?",
    "choices": ["$2.40", "$2.50", "$2.60", "$2.70"],
    "answer": "$2.60"
  },
  {
    "question": "What was NVDA's cash and cash equivalents in November 2023?",
    "choices": ["$16 billion", "$17 billion", "$18 billion", "$19 billion"],
    "answer": "$18 billion"
  },
  {
    "question": "What was NVDA's total assets in August 2023?",
    "choices": ["$55 billion", "$56 billion", "$57 billion", "$58 billion"],
    "answer": "$57 billion"
  },
  {
    "question": "What was NVDA's operating expenses in February 2023?",
    "choices": ["$2.2 billion", "$2.3 billion", "$2.4 billion", "$2.5 billion"],
    "answer": "$2.4 billion"
  },
  {
    "question": "What was NVDA's operating cash flow in May 2023?",
    "choices": ["$3.8 billion", "$3.9 billion", "$4 billion", "$4.1 billion"],
    "answer": "$4 billion"
  }
]

streamQuestions = []
index = 0
for q in questions:
    streamQ = st.radio(label = q["question"] , options= q["choices"] , index = None , key = index )
    streamQuestions.append(streamQ)
    index = index + 1

index = 0
correctAnswer = 0
for streamQs in streamQuestions :
    if(streamQs == questions[index]["answer"] ):
        correctAnswer = correctAnswer + 1
    index = index + 1

st.write('Number of Correct answer :' , correctAnswer )

# genre = st.radio(
#     "What's your favorite movie genre",
#     [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
#     captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

# if genre == ':rainbow[Comedy]':
#     st.write('You selected comedy.')
# else:
#     st.write("You didn\'t select comedy.")
