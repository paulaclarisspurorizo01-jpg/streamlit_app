import streamlit as st


st.title("🚀 My Work Portfolio")
st.write("A simple showcase of my programming projects.")

st.divider()


st.subheader("📁 My Projects")

projects = {
    "Student Record System": "A simple system for managing student information.",
    "Calculator App": "A basic app for performing arithmetic operations.",
    "Personal Web Portfolio": "A website that displays my skills and works."
}

col1, col2 = st.columns([1, 2])

with col1:
    selected_project = st.selectbox("Select a project", list(projects.keys()))

with col2:
    st.success(projects[selected_project])

st.divider()

st.subheader("📊 Portfolio Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Projects", "3")
col2.metric("Main Language", "Python")
col3.metric("Framework", "Streamlit")

st.divider()


st.subheader("💖 Support")

if st.button("Like this Portfolio"):
    st.success("Thank you for your support! ❤️ - Martin R. Monterola")

st.divider()

st.caption("© 2026 Work Portfolio | Built with Streamlit")
