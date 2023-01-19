import streamlit as st

st.set_page_config(layout="wide")

# Sidebar
with st.sidebar:
    st.title('INPUTS')
    st.text_input('6-DIGIT SKU')
    st.selectbox('COUNTRY', ['US', 'CA'])

st.title('WEB INVENTORY LOOKUP TOOL')
st.write('When you’re wondering why a SKU isn’t showing up online, this tool has your back!')

col1, col2 = st.columns((1,1))

with col1:
    st.title('Column 1')

with col2:
    st.title('Column 2')


#Main Section

