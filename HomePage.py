import streamlit as st
from PIL import Image



image = Image.open("assets/pic1.jpg")

st.title("💻 My Portfolio")
st.write("Simple portfolio built using Streamlit.")

st.divider()

st.header("About Me")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(image, use_container_width=True)

with col2:
    st.subheader("Paula Clariss P. Rizo")
    st.write("""
Hello! I am **Paula Clariss P. Rizo**, a Computer Science student.

I enjoy learning programming and creating simple projects.

🎓 School: DEBESMSCAT  
📚 Year Level: 3rd Year Student
""")

st.divider()

st.header("Skills")

st.write("C #")
st.progress(60)

st.write("Python")
st.progress(70)

st.write("C++")
st.progress(65)

st.divider()

st.header("Projects")


st.write("🎓 Student Record System - Small school project")
st.write("🧮 Calculator App - Simple mini project")
st.write("🌐 Portfolio Website - Personal web project")


st.divider()


