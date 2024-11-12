import streamlit as st
import pydeck as pdk

def show_page():
    # 서울시 각 구의 중심 좌표 (위도, 경도)
    if st.button("테스트"):
        st.session_state.information +=1   
        st.rerun()
# 서울시 각 구의 중심 좌표와 정보
    seoul_districts = {
        "강남구": {"latitude": 37.5172, "longitude": 127.0473, "info": st.session_state.south},
        "강동구": {"latitude": 37.5301, "longitude": 127.1238, "info": st.session_state.east},
        "강북구": {"latitude": 37.6396, "longitude": 127.0257, "info": st.session_state.north},
        "강서구": {"latitude": 37.5509, "longitude": 126.8495, "info": st.session_state.west},

    }

    # Streamlit 애플리케이션 제목
    st.title("서울시 구별 실시간 강수량 표시")

    # 사용자로부터 구 선택 받기
    selected_district = st.selectbox("구를 선택하세요:", list(seoul_districts.keys()))

    # 선택된 구의 좌표와 정보 가져오기
    latitude = seoul_districts[selected_district]["latitude"]
    longitude = seoul_districts[selected_district]["longitude"]
    info = seoul_districts[selected_district]["info"]

    # 선택된 구의 정보 표시
    st.write(f"### {selected_district}의 위치 정보")
    st.write(f"위도: {latitude}, 경도: {longitude}")
    st.write(f"{selected_district}의 현재 강수량 {info}")

    # pydeck을 사용하여 지도 표시
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=latitude,
            longitude=longitude,
            zoom=12,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=[{"lat": latitude, "lon": longitude, "info": info}],
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
                pickable=True,
            ),
        ],
        tooltip={"text": "{info}"}
    ))
