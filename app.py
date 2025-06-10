import streamlit as st
from scheduler import generate_schedule

st.set_page_config(page_title="AI Study Scheduler", layout="centered")

st.title("📚 AI-Powered Study Scheduler")
st.write("Smartly plan your study hours based on time and subject priorities!")
subjects = st.text_area("Enter your subjects (one per line)").split("\n")
total_hours = st.slider("How many hours can you study today?", 1, 16, 4)
important_subjects = st.multiselect("Select most important subjects", subjects)
if st.button("Generate Study Plan"):
    if not subjects or subjects == [""]:
        st.error("Please enter at least one subject.")
    else:
        schedule = generate_schedule(subjects, total_hours, important_subjects)
        st.success("📅 Here's your study plan for today:")
        for subject, hours in schedule.items():
            st.write(f"*{subject}* → {hours:.2f} hours")
