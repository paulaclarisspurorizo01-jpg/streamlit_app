import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Paula Clariss P. Rizo",
    page_icon="👨‍💻",
    layout="wide"
)

image = Image.open("assets/pic1.jpg")


st.title("👨‍💻 My Personal Portfolio")
st.write("Welcome to my simple portfolio created using Streamlit.")

st.divider()

col1, col2 = st.columns([1,2])

with col1:
    st.image(image, use_container_width=True)

with col2:
    st.subheader("Hi! I'm Paula Clariss P. Rizo 👋")

    st.write("""
I am a Computer Science student who enjoys learning programming 
and building simple applications.

I like learning how to code and create small projects.
""")

    st.write("""
📅 Born on: November 01, 2004  
📍 Address: Guincaiptan, Mandaon, Masbate  
🎂 Age: 21
""")

    if st.button("Say Hello"):
        st.success("Thanks for visiting my portfolio!")

st.divider()

st.subheader("Skills")

st.write("Python")
st.progress(90)

st.write("HTML")
st.progress(80)

st.write("CSS")
st.progress(75)

st.write("Streamlit")
st.progress(85)

st.divider()

st.subheader("Education")

st.write("""
College of Computing and Information Technology at
DEBESMSCAT

• Programming Fundamentals  
• Web Development  
• Software Design  
• Problem Solving
""")

st.divider()

st.subheader("My Favorite Skill")

skill = st.selectbox(
    "Choose a skill:",
    ["Python", "HTML", "CSS", "Streamlit"]
)

st.write(f"My selected skill is **{skill}**.")
