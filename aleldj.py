import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(
    page_title="2025 미디어 이용행태 인사이트 대시보드",
    page_icon="📊",
    layout="wide"
)

# 2. 데이터 가공 및 탑재 (스마트폰 및 PC 2025년 12월 데이터)
@st.cache_data
def load_data():
    categories = ["교육", "드라마&영화", "보도", "스포츠", "어린이(유아)", "오락", "정보"]
    
    # 연령대별 스마트폰 총 시청시간 합계 (남+여 합산)
    smartphone_data = {
        "10대 (13-19세)": [7.6, 7287.4, 3589.3, 956.9, 391.7, 36396.2, 2912.2],
        "20대 (20-29세)": [16.3, 19120.2, 12173.5, 2338.7, 530.3, 97397.9, 8499.9],
        "30대 (30-39세)": [3.2, 46187.2, 37732.9, 5681.5, 1614.5, 135916.9, 14437.2],
        "40대 (40-49세)": [121.7, 78407.4, 63908.6, 6813.3, 975.7, 166676.0, 13900.0],
        "50대 (50-59세)": [154.9, 100976.7, 136557.5, 8165.9, 1491.5, 174661.3, 20545.4],
        "60대 이상": [296.4, 41290.5, 164758.7, 5692.8, 1098.4, 134098.1, 20573.4]
    }
    
    # 기기별 비교 데이터
    device_data = {
        "스마트폰": [600.2, 293269.4, 418720.7, 29649.0, 6102.1, 745146.6, 80868.1],
        "PC": [729.6, 12743.6, 20558.3, 13293.2, 1443.6, 50911.8, 8927.8]
    }
    
    return pd.DataFrame(smartphone_data, index=categories), pd.DataFrame(device_data, index=categories)

df_age, df_device = load_data()

# 3. 헤더 및 대시보드 소개
st.markdown("""
<div style="background-color:#1E1E2F; padding:20px; border-radius:12px; margin-bottom:25px;">
    <h1 style="color:white; text-align:center; margin:0;">📊 2025 미디어 이용행태 데이터 분석 대시보드</h1>
    <p style="color:#A0A0B0; text-align:center; font-size:1.1rem; margin-top:10px; margin-bottom:0;">
        단순한 '스마트폰 중독' 프레임을 넘어, 미디어 소비 데이터가 보여주는 <b>진짜 사회 변화</b>를 분석합니다.
    </p>
</div>
""", unsafe_allow_html=True)

# 4. [메인 인사이트] 주목할 만한 발견 (뻔하지 않은 이야기)
st.markdown("### 🚨 이번 데이터에서 찾은 '의외의' 핵심 발견")
col_ins1, col_ins2, col_ins3 = st.columns(3)

with col_ins1:
    st.markdown("""
    <div style="background-color:#EBF5FF; padding:20px; border-radius:10px; border-left: 6px solid #007BFF; height:200px;">
        <h4 style="color:#004085; margin:0;">1️⃣ 뉴스는 노년층의 전유물?</h4>
        <p style="color:#004085; font-size:0.95rem; margin-top:10px;">
            <b>보도(뉴스)</b> 장르 시청 시간은 60대 이상이 10대보다 <b>약 45배</b> 많습니다. 세대 간 세상 소식을 접하는 통로(유튜브 숏폼 vs 전통 뉴스)가 완전히 갈라졌음을 뜻합니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_ins2:
    st.markdown("""
    <div style="background-color:#FFF3CD; padding:20px; border-radius:10px; border-left: 6px solid #FFC107; height:200px;">
        <h4 style="color:#856404; margin:0;">2️⃣ PC는 죽지 않았다, 다만...</h4>
        <p style="color:#856404; font-size:0.95rem; margin-top:10px;">
            모두 스마트폰만 쓰는 줄 알았지만, <b>'교육'</b> 장르는 유일하게 스마트폰(600만 분)보다 <b>PC(730만 분) 시청 시간</b>이 더 많습니다. 공부할 때는 여전히 큰 화면을 씁니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_ins3:
    st.markdown("""
    <div style="background-color:#D4EDDA; padding:20px; border-radius:10px; border-left: 6px solid #28A745; height:200px;">
        <h4 style="color:#155724; margin:0;">3️⃣ 스포츠는 모바일 직관 시대</h4>
        <p style="color:#155724; font-size:0.95rem; margin-top:10px;">
            스포츠 경기 중계 시청은 PC보다 <b>스마트폰이 2.2배</b> 높습니다. TV 앞에 모이기보다 침대에 누워 모바일 화면으로 실시간 채팅을 치며 즐기는 문화가 정착되었습니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("---")

# 5. [인터랙티브 분석] 관심 분야 선택 상자
st.markdown("### 🎯 관심 있는 분석 분야를 선택해 보세요!")
selected_field = st.selectbox(
    "이 데이터를 통해 어떤 분야의 변화를 보고 싶나요?",
    [
        "선택해 주세요",
        "💼 일자리와 진로 (PC vs 스마트폰 사용처 차이)",
        "👵 세대 갈등과 소통 (연령별 미디어 관심사 격차)",
        "🛒 기업 마케팅과 비즈니스 (돈이 몰리는 미디어 장르)"
    ]
)

# 선택한 분야에 따른 맞춤형 풀이 및 그래프 제공
if selected_field == "선택해 주세요":
    st.info("💡 위의 상자를 클릭해 관심 분야를 선택하면 맞춤형 심층 분석과 화려한 그래프가 나타납니다!")

elif "일자리와 진로" in selected_field:
    st.subheader("💼 일자리와 진로: 미래 스마트 워커(Worker)의 장비 트렌드")
    
    col_g1, col_g2 = st.columns([3, 2])
    
    with col_g1:
        # 스트림릿 내장 바 차트로 변경 (추가 설치 불필요!)
        st.bar_chart(df_device)
        
    with col_g2:
        st.markdown("""
        #### 🔍 핵심 데이터 해석 (중고등학생 눈높이 설명)
        * **"노는 건 폰으로, 공부는 PC로!"**
            * '오락', '드라마' 같은 즐길 거리는 스마트폰이 PC보다 압도적으로 높습니다.
            * 반면 **'교육'** 장르는 유일하게 PC가 스마트폰보다 시청시간이 더 많습니다.
        * **미래 진로에 던지는 질문 🤔**
            * 여러분이 만약 **온라인 교육 콘텐츠 디자이너**나 **웹 개발자**가 되고 싶다면, 모바일 앱보다 **PC 웹 사이트 화면**을 더 사용하기 편하고 보기 좋게 만드는 법을 먼저 공부해야겠죠?
            * 반대로 웹툰이나 예능 피디(PD)가 되고 싶다면, 무조건 **한 손에 들어오는 세로형 뷰**에 초점을 맞추어야 성공할 수 있습니다.
        """)

elif "세대 갈등과 소통" in selected_field:
    st.subheader("👵 세대 갈등과 소통: 세대 간의 '관심 격차' 리포트")
    
    col_g1, col_g2 = st.columns([3, 2])
    
    with col_g1:
        # 스트림릿 내장 라인 차트로 변경 (추가 설치 불필요!)
        st.line_chart(df_age)
        
    with col_g2:
        st.markdown("""
        #### 🔍 핵심 데이터 해석 (중고등학생 눈높이 설명)
        * **"우리 부모님이 뉴스를 계속 보시는 이유"**
            * 50대와 60대 이상의 스마트폰 사용 시간에서 압도적인 1위는 바로 **'보도(뉴스)'**입니다. 
            * 반면 10대와 20대는 뉴스를 거의 보지 않고 **'오락(예능, 숏폼)'**과 **'드라마&영화'**에만 집중되어 있죠.
        * **소통의 지혜 💡**
            * 명절이나 저녁 시간에 할머니, 할아버지와 대화가 안 통한다고 느껴졌나요? 그건 머릿속을 가득 채우고 있는 **미디어 데이터의 성격**이 아예 다르기 때문입니다.
            * 부모님 세대는 세상을 '뉴스'를 통해 진지하게 파악하고 있고, 청소년 세대는 세상 트렌드를 '유튜브'나 '밈'을 통해 즐겁게 받아들입니다. 서로를 틀리다고 하기보다, 관심사가 이렇게 다르다는 걸 인정하는 것부터가 소통의 시작입니다.
        """)

elif "기업 마케팅과 비즈니스" in selected_field:
    st.subheader("🛒 기업 마케팅과 비즈니스: 기업들의 광고비는 어디로 흘러갈까?")
    
    col_g1, col_g2 = st.columns([3, 2])
    
    with col_g1:
        # 스마트폰 장르 비율 비교 바 차트로 대체
        st.bar_chart(df_device["스마트폰"])
        
    with col_g2:
        st.markdown("""
        #### 🔍 핵심 데이터 해석 (중고등학생 눈높이 설명)
        * **"왜 예능과 유튜브에 광고가 넘쳐날까?"**
            * 전체 스마트폰 시청 시간의 절반 가까이를 차지하는 장르는 바로 **'오락'**입니다. 
            * 대기업 광고 기획자들은 돈을 쓸 때 사람들이 가장 오래 머무는 곳에 씁니다. 그렇기 때문에 예능 프로그램이나 유튜브 채널 중간광고에 엄청난 돈이 쏠리는 것입니다.
        * **창업 및 마케팅 꿀팁 📈**
            * 만약 여러분이 나중에 화장품이나 의류 쇼핑몰을 창업한다면 어디에 마케팅 예산을 써야 할까요?
            * 스포츠나 뉴스 채널보다는, 사람들의 시선이 가장 오래 머무는 **오락 카테고리(웹예능, 숏폼 크리에이터 PPL)**에 투자하는 것이 돈을 낭비하지 않는 최선의 선택이 된다는 것을 이 그래프가 증명하고 있습니다.
        """)

st.markdown("---")
st.caption("데이터 출처: 방송통신위원회 2025년 스마트폰·PC 이용행태 조사 보고서")
