import streamlit as st
st.title('김예은의 첫번쨰 앱')
st.subheader('오늘 저녁 뭐 먹지')
st.write('떡볶이 먹고시포')
st.write('https://naver.com')
st.link_button("네이버 바로가기", 'https://naver.com')

name= st.text_input('이름을 입력해주세요.')
if st.button('환영인사'):
    st.write(name+'님 안녕하세요!')
    st.balloons()
    st.image("https://www.news1.kr/_next/image?url=https%3A%2F%2Fi3n.news1.kr%2Fsystem%2Fphotos%2F2017%2F2%2F28%2F2407472%2Farticle.jpg&w=1920&q=75")

st.success('성공!')
st.warning('경고!')
st.error('오류!')
st.info('안내문')
