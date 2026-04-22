import streamlit as st


home_page = st.Page(
    page="pages/home.py",
    icon='🏡' ,
    title='Home page' ,
  
    default=True
)
signin_page = st.Page( 
    page="pages/signin.py", 
    title='signin page' , 
    icon='👥' 
)
signup_page = st.Page( 
    page="pages/signup.py", 
    title='signup page' , 
    icon='🔐' 
)
contact_us = st.Page( 
    page="pages/contact_us.py", 
    title='Contact Us' , 
    icon='☎️' 
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
