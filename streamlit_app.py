import streamlit as st

st.set_page_config(layout="wide")
st.title('WEB INVENTORY LOOKUP TOOL')
st.write('When you’re wondering why a SKU isn’t showing up online, this tool has your back!')

# Sidebar
with st.sidebar:
	st.title('INPUTS')
    st.text_input('Enter some text')


