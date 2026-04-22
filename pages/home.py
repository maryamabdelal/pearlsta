import streamlit as st 


st.title('Welcome to Pearlista', text_alignment='center')
st.subheader('We make you more elegant' , text_alignment='center')
st.image('images/pearlsta.jpeg', width=700)

st.divider()

left, right = st.columns([1, 1], border=True)
with left:
    st.header("Not Registered Yet?")
    st.write("Join us today and experience the elegance of Pearlista! Sign up now to access exclusive offers, personalized recommendations, and a seamless shopping experience tailored just for you.")
    if left.button("Go To Sign Up", icon="📝", use_container_width=True, width="stretch"):
        left.markdown("You clicked the sign up button.")
        st.switch_page("Pages/SignUp.py")

with right:
    st.header('Contact us')
    st.write('Have questions or need more information? We are here to help! Reach out to us through the following channels:')
    if right.button("Go To Contact Us", icon="📝", use_container_width=True, width="stretch"):
        right.markdown("You clicked the contact us button.")
        st.switch_page("Pages/ContactUs.py")
