# faq_chatbot.py

import streamlit as st

# Predefined FAQ answers with keywords (including punctuation if needed)
faq_answers = {
    "programs": "Iron Lady offers programs like:\n- Leadership Essentials\n- Master of Business Warfare\n- 100 Board Members Program\n- 1 Crore Club",
    
    "duration": "Program durations:\n- Leadership Essentials: 6 weeks\n- Master of Business Warfare: 12 weeks\n- 100 Board Members Program: 3 months\n- 1 Crore Club: 6 months",
    
    "online offline": "Program format:\n- Most programs are offline at KIADB plot#8, Sadaramangala Rd, Bengaluru\n- Some sessions may have online components",
    
    "certificate": "Yes, certificates are provided upon successful completion of the programs",
    
    "mentor coach mentors/coaches": "Mentors and coaches:\n- Industry leaders\n- Experts with over 25 years of experience in leadership and business strategy",
    
    "about programs": "Iron Lady leads transformative leadership programmes for women:\n- Uses the Art of War\n- Business War Tactics\n- Strength-Based Excellence model\n- Designed to empower women in today's business world"
}

# Streamlit UI
st.title("🤖 Iron Lady FAQ Chatbot")
st.write("Ask a question about Iron Lady's programs:")

# User input
user_question = st.text_input("Your question:")

if user_question:
    # Convert to lowercase for comparison but KEEP punctuation
    question_text = user_question.lower().strip()

    # Match keywords
    found = False
    for key, answer in faq_answers.items():
        keywords = key.split()
        if any(word in question_text for word in keywords):
            st.write(f"Answer:\n{answer}")
            found = True
            break
    
    if not found:
        st.write("Answer:\nSorry, I don’t have an answer for this question yet.")
