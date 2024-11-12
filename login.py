import streamlit as st
import map

def login(username, password):
    if username in st.session_state.users and st.session_state.users[username] == password:
        st.session_state.logged_in = True
        st.rerun()
    else:
        st.error("사용자명 또는 비밀번호가 올바르지 않습니다.")

# 세션 상태 초기화
def show_page():
    
    if st.session_state.logged_in:
        # 로그인 성공 후 페이지 전환 메뉴 표시
        st.session_state.show_login = False
        
    else:
        # 로그인 UI
        col1, col2 = st.columns([1, 1])

        with col1:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            st.markdown(
                """
            <div class="french-font" style="text-align: center;">
                    <img src="https://www.komipo.co.kr/main_new4/contents/images/sub/sangcomi_sub_character06.jpg" 
                    alt="서비스 이미지" style="width:100%; max-width:500px; margin: auto;">
                    <p>안전한 미래를 위해!</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            st.header("로그인")
            st.session_state.username = st.text_input("ID")
            st.session_state.password = st.text_input("Password", type="password")

            col3, col4 = st.columns([11, 3])
            with col3: 
                st.checkbox("ID remember")
            with col4:
                st.button("Forget your ID?")
            # 로그인 버튼
            if st.button("로그인"):
                login(st.session_state.username, st.session_state.password)

