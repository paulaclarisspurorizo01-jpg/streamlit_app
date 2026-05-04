import streamlit as st



st.title("📬 Contact Me")
st.write("You can reach out anytime using the form below.")

st.divider()

st.subheader("📌 My Contact Details")

col1, col2 = st.columns(2)

with col1:
    st.info("📧 Email: paulaclarisspurorizo01@email.com")

with col2:
    st.info("🎓 Role: Computer Science Student")

st.divider()


st.subheader("✉️ Send a Message")

with st.form("contact_form"):

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    submitted = st.form_submit_button("Send Message")

    if submitted:
        if name and email and message:
            st.success(f"Thanks {name}! Your message has been sent successfully.")
        else:
            st.warning("Please complete all fields before submitting.")

st.divider()
