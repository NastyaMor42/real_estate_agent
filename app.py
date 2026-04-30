import streamlit as st
from memory import get_memory, update_memory

USER_ID = "nastya"

st.title("🏡 התחלת סוכן נדל״ן")

memory = get_memory(USER_ID)

# אם יש כבר מידע - מציגים אותו
if memory:
    st.write("מה שאני כבר יודע עלייך:")
    st.write(memory)

st.divider()

st.write("בואי נעדכן חיפוש:")

city = st.text_input("עיר:", value=memory.get("city", ""))
price = st.number_input("מחיר מקסימלי:", value=memory.get("max_price", 0), step=500)

if st.button("עדכן העדפות"):
    update_memory(USER_ID, {
        "city": city,
        "max_price": price
    })
    st.success("נשמר!")

st.divider()

st.write("הזיכרון הנוכחי:")
st.write(get_memory(USER_ID))
