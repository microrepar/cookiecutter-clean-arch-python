"""Application's entry point
Project name: {{cookiecutter.project_name}}
Author: {{cookiecutter.author}}
Description: {{cookiecutter.description}}
"""
import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages

from src.external.app_pages.auth_manager.authentication import streamlit_auth
from src.external.app_pages.user_crud import user_crud_page

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

placeholder_msg = st.empty()

# ------------------------- Authentication -------------------------
name, authentication_status, username, authenticator, credentials = streamlit_auth(placeholder_msg)

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password to access application")

if authentication_status:
    # ---- SIDEBAR ----
    authenticator.logout(f"Logout | {st.session_state.username}", "sidebar")
    st.sidebar.divider()

    if username == 'admin':
        show_pages(
            [   Page("streamlit_app.py", "USER CRUD", "🗂️"),
                Page("src/external/app_pages/auth_manager/auth_manager_page.py", "Authentication Manager", "🔑"),
            ]
        )
    else:
        show_pages(
            [
                Page("streamlit_app.py", "USER CRUD", "🗂️"),
                Page("src/external/app_pages/auth_manager/auth_manager_page.py", "Authentication Manager", "🔑"),
            ]
        )
    
    add_page_title()
    user_crud_page()

else:
    show_pages([Page("streamlit_app.py", "USER CRUD", "🗂️"),])