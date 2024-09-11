import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import pyshorteners

# 페이지 설정
st.title("URL 단축기")

# 사용자로부터 URL 입력 받기
url = st.text_input("단축할 URL을 입력하세요:")

# URL 단축 함수
def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

# 버튼을 클릭하면 URL을 단축
if st.button("단축하기"):
    if url:
        try:
            short_url = shorten_url(url)
            st.success(f"단축된 URL: {short_url}")
        except Exception as e:
            st.error(f"URL 단축에 실패했습니다: {str(e)}")
    else:
        st.warning("URL을 입력하세요.")
