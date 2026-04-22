import streamlit as st


home_page = st.Page(
    page="pages/home.py",
    title='Home page' ,
    default=True
)
signin_page = st.Page( 
    page="pages/signin.py", 
    title='signin page' , 
)
signup_page = st.Page( 
    page="pages/signup.py", 
    title='signup page' , 
)
contact_us = st.Page( 
    page="pages/contact_us.py", 
    title='Contact Us' , 
)

all_pages =st.navigation(
    pages=[
        home_page,
        signin_page,
        signup_page,
        contact_us
    ],
)
all_pages.run()
