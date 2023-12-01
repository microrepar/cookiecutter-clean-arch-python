import streamlit as st

from streamlit_js_eval import (copy_to_clipboard, create_share_link,
                                       get_geolocation, streamlit_js_eval)

from src.adapters import Controller


def user_crud_page():

    if st.checkbox("Check my location"):
        loc = get_geolocation()
        st.write(f"Your coordinates are {loc}")


    #############################################################
    ### ALL USERS PLACEHOLDER###
    #############################################################
    st.markdown(f'## ALL REGISTRED USERS')
    placeholder_get_all_users = st.empty()
    #############################################################


    #############################################################
    ### REGISTRY USER ###
    #############################################################
    st.markdown('## REGISTRY USER')

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
    ### UPDATE USER ###
    #############################################################
    st.markdown('## UPDATE USER')

    controller = Controller()
    request    = {'resource': '/user/update_detail',
                'user_id_': 1,
                'user_name': 'codigo100cera',
                'user_email': 'contato@codigo100cera.com.br',
                'user_age': 36,
                'user_username': 'username_test',
                'user_password': 'password_test',
                }

    st.write(request)

    if st.button('Update', type='primary'):
        resp       = controller(request=request)

        st.write(resp)
    #############################################################


    #############################################################
    ### REMOVE USER ###
    #############################################################
    st.markdown('## REMOVE USER')

    controller = Controller()
    request    = {'resource': '/user/remove',
                'user_username': 'username_test'
                }

    st.write(request)

    if st.button('Remove', type='primary'):
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