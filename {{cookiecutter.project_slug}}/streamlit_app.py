"""Application's entry point
Project name: {{cookiecutter.project_name}}
Author: {{cookiecutter.author}}
Description: {{cookiecutter.description}}
"""

import streamlit as st

from src.adapters import Controller

#############################################################
### GET ALL USERS PLACEHOLDER###
#############################################################
st.markdown(f'## Get all users')
placeholder_get_all_users = st.empty()
#############################################################


#############################################################
### REGISTRY USER ###
#############################################################
st.markdown('## Registry user')

controller = Controller()
request    = {'resource': '/user/registry',
              'user_name': 'test',
              'user_age': 36,
              'user_username': 'username_test',
              'user_password': 'password_test',
              }

st.write(request)

if st.button('Add', type='primary'):
    resp       = controller(request=request)

    st.write(resp)
#############################################################


#############################################################
### GET ALL USERS ###
#############################################################
controller = Controller()
request    = {'resource': '/user'}
resp       = controller(request=request)
#############################################################

placeholder_get_all_users.write(resp)
#############################################################
