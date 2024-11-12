import streamlit as st
import login 
import map

st.set_page_config(layout="wide")

if "show_login" not in st.session_state:
    st.session_state.show_login = True
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "users" not in st.session_state:
    st.session_state.users = {"coj49863":"rlagustn1"}
if "south" not in st.session_state:
    st.session_state.south = 0
if "north" not in st.session_state:
    st.session_state.north = 0
if "east" not in st.session_state:
    st.session_state.east = 0
if "west" not in st.session_state:
    st.session_state.west = 0


if(st.session_state.show_login ==True):
    login.show_page()
if(st.session_state.logged_in == True):
    map.show_page()