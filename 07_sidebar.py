Barimport streamlit as st
from PIL import Image

# sidebar
st.sidebar.title('Sidebar')
st.sidebar.header('input text')
user_id = st.sidebar.text_input('Inpu ID', value='streamlit', max_chars=15)
user_pw = st.sidebar.text_input('Input PW', value='abcd', type='password')

st.sidebar.header('select box')
sel_opt = ['Vemeer', 'Munch', 'Shin']
user_opt = st.sidebar.selectbox('favorite', sel_opt)
st.sidebar.write(user_opt)

# Main
st.title("Sidebar of Streamlit") ## write ()

image_files = ['Vermeer.png', 'Munch.png', 'ShinYoonbok.png']

sel_img_index = sel_opt.index(user_opt)
# 선택한 항목에 맞는 이미지 파일 지정
img_file = image_files[sel_img_index]
img_local = Image.open(img_file) # data path /
st.image(img_local, caption=user_opt) 

