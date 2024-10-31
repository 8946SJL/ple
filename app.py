import streamlit as st
import time

# 스플래시 화면
st.title("라온하제")
st.markdown("<h1 style='text-align: center; color: blue;'>로딩 중...</h1>", unsafe_allow_html=True)

# 스플래시 화면이 잠시 보이도록 대기
time.sleep(2)  # 2초 대기 후 홈 화면으로 이동

# 홈 화면
st.write("Hello, World!")
