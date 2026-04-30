import streamlit as st
from memory import get_memory, update_memory

USER_ID = "nastya"

st.title("בדיקת MEMORY")

city = st.text_input("עיר:")
price = st.number_input("מחיר מקסימלי:", step=500)

if st.button("שמור"):
    update_memory(USER_ID, {
        "city": city,
        "max_price": price
    })

st.write("הזיכרון שלך:")
st.write(get_memory(USER_ID))
