import streamlit as st
import pandas as pd

# 1. 페이지 설정
st.set_page_config(
    page_title="2025 미디어 이용행태 데이터 분석",
    page_icon="📊",
    layout="wide"
)

# 2. 데이터 가공 및 탑재 (스마트폰 및 PC 2025년 12월 데이터)
@st.cache_data
def load_data():
    categories = ["교육", "드라마&영화", "보도", "스포츠", "어린이(유아)", "오락", "정보"]
    
    # 연령대별 스마트폰 총 시청시간 합계 (남+여 합산, 단위: 만분)
    smartphone_data = {
        "10대 (13-19세)": [7.6, 7287.4, 3589.3, 956.9, 391.7, 36396.2, 2912.2],
        "20대 (20-29세)": [16.3, 19120.2, 12173.5, 2338.7, 530.3, 97397.9, 8499.9],
        "30대 (30-39세)": [3.2, 46187.2, 37732.9, 5681.5, 1614.5, 135916.9, 14437.2],
        "40대 (40-49세)": [121.7, 78407.4, 63908.6, 6813.3, 975.7, 166676.0, 13900.0],
        "50대 (50-59세)": [154.9, 100976.7, 136557.5, 8165.9, 1491.5, 174661.3, 20545.4],
        "60대 이상": [296.4, 41290.5, 164758.7, 5692.8, 1098.4, 134098.1, 20573.4]
    }
    
    # 기기별 비교 데이터 (단위: 만분)
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
        실제 통계 데이터를 근거로 과학적인 미디어 소비 트렌드를 도출합니다. [데이터 소스: 방송통신위원회]
    </p>
</div>
""", unsafe_allow_html=True)

# 4. [신규 추가] 한 눈에 보는 핵심 핵심 데이터 메트릭 (접속하자마자 수치 확인 가능)
st.markdown("### 📈 데이터 핵심 지표 (Key Metrics)")
col_m1, col_m2, col_m3, col_m4 = st.columns(4)

# 원본 데이터 기준 주요 통계량 계산
total_smartphone_time = df_device["스마트폰"].sum()
total_pc_time = df_device["PC"].sum()
edu_pc_ratio = (df_device.loc["교육", "PC"] / (df_device.loc["교육", "스마트폰"] + df_device.loc["교육", "PC"])) * 100
teens_news_vs_seniors = df_age.loc["보도", "60대 이상"] / df_age.loc["보도", "10대 (13-19세)"]

with col_m1:
    st.metric(
        label="스마트폰 총 이용시간 (만 분)", 
        value=f"{total_smartphone_time:,.1f}", 
        delta="PC 대비 약 14.5배"
    )
with col_m2:
    st.metric(
        label="PC 총 이용시간 (만 분)", 
        value=f"{total_pc_time:,.1f}"
    )
with col_m3:
    st.metric(
        label="교육 분야 PC 이용 비중", 
        value=f"{edu_pc_ratio:.1f}%", 
        delta="유일하게 PC 우세"
    )
with col_m4:
    st.metric(
        label="60대 이상 vs 10대 뉴스 시청비", 
        value=f"{teens_news_vs_seniors:.1f} 배", 
        delta="세대 간 극단적 격차"
    )

st.write("")
st.markdown("---")

# 5. [메인 인사이트] 데이터로 검증하는 3대 발견 (구체적 수치 제시)
st.markdown("### 🚨 통계적 근거를 바탕으로 한 3대 사실 발견")
col_ins1, col_ins2, col_ins3 = st.columns(3)

with col_ins1:
    news_10s = df_age.loc["보도", "10대 (13-19세)"]
    news_60s = df_age.loc["보도", "60대 이상"]
    st.markdown(f"""
    <div style="background-color:#EBF5FF; padding:20px; border-radius:10px; border-left: 6px solid #007BFF; height:220px;">
        <h4 style="color:#004085; margin:0;">1️⃣ 세대 간 뉴스 소비량 '45.9배' 격차</h4>
        <p style="color:#004085; font-size:0.95rem; margin-top:10px;">
            <b>근거 데이터:</b> 10대의 뉴스 시청 시간은 <b>{news_10s:,.1f}만 분</b>인 반면, 60대 이상은 <b>{news_60s:,.1f}만 분</b>에 달합니다. 
            청소년층이 기성 언론(보도) 미디어 생태계로부터 거의 완벽히 이탈했음을 수치가 증명합니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_ins2:
    edu_phone = df_device.loc["교육", "스마트폰"]
    edu_pc = df_device.loc["교육", "PC"]
    st.markdown(f"""
    <div style="background-color:#FFF3CD; padding:20px; border-radius:10px; border-left: 6px solid #FFC107; height:220px;">
        <h4 style="color:#856404; margin:0;">2️⃣ 교육 장르, 유일무이한 PC의 판정승</h4>
        <p style="color:#856404; font-size:0.95rem; margin-top:10px;">
            <b>근거 데이터:</b> 교육 콘텐츠의 스마트폰 시청은 <b>{edu_phone:,.1f}만 분</b>에 그쳤으나, PC는 <b>{edu_pc:,.1f}만 분</b>을 기록했습니다. 
            모바일 퍼스트 시대에도 학습 몰입을 위한 도구는 'PC'라는 것을 보여줍니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_ins3:
    sports_phone = df_device.loc["스포츠", "스마트폰"]
    sports_pc = df_device.loc["스포츠", "PC"]
    st.markdown(f"""
    <div style="background-color:#D4EDDA; padding:20px; border-radius:10px; border-left: 6px solid #28A745; height:220px;">
        <h4 style="color:#155724; margin:0;">3️⃣ 스포츠 관람, 모바일 이주 현상</h4>
        <p style="color:#155724; font-size:0.95rem; margin-top:10px;">
            <b>근거 데이터:</b> 스포츠 시청 시간은 스마트폰이 <b>{sports_phone:,.1f}만 분</b>으로 PC(<b>{sports_pc:,.1f}만 분</b>)의 2.2배가 넘습니다. 
            인터랙티브 응원 문화가 모바일 스포츠 중계를 주도하고 있음을 보여줍니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("---")

# 6. [인터랙티브 분석] 관심 분야 선택 상자
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

if selected_field == "선택해 주세요":
    st.info("💡 위의 상자를 클릭해 관심 분야를 선택하면 통계 데이터와 시각화 자료를 함께 확인할 수 있습니다.")

elif "일자리와 진로" in selected_field:
    st.subheader("💼 일자리와 진로: 미래 스마트 워커(Worker)의 장비 트렌드")
    
    col_g1, col_g2 = st.columns([3, 2])
    
    with col_g1:
        st.bar_chart(df_device)
        
    with col_g2:
        st.markdown(f"""
        #### 📊 통계 기반 학술적 데이터 풀이
        1. **데이터 팩트 체크:**
            * 스마트폰의 주 시청 장르는 **'오락'({df_device.loc['오락', '스마트폰']:,.0f}만 분)**으로, PC 오락 소비량({df_device.loc['오락', 'PC']:,.0f}만 분)의 **14.6배** 수준입니다.
            * 반대로 **'교육'** 장르는 유일하게 PC 시청시간이 스마트폰보다 **{df_device.loc['교육', 'PC'] - df_device.loc['교육', '스마트폰']:,.1f}만 분** 더 많습니다.
        
        2. **해석과 생각거리:**
            * 왜 이런 격차가 날까요? 스마트폰은 간편하고 빠르게 소비하는 콘텐츠(스낵 미디어)에 적합하지만, 코딩 실습이나 필기, 긴 집중 시간이 필요한 **학습 목적(교육)**에는 키보드가 있고 화면이 큰 PC가 절대적 우위에 있음을 정량적 데이터가 증명합니다.
            * 만약 미래에 교육용 에듀테크 플랫폼을 개발하는 진로를 꿈꾼다면, 모바일 전용 앱 개발보다는 안정적인 웹 기반(PC 지원) 대시보드 환경을 갖추는 기획이 훨씬 논리적인 전략입니다.
        """)

elif "세대 갈등과 소통" in selected_field:
    st.subheader("👵 세대 갈등과 소통: 세대 간의 '관심 격차' 리포트")
    
    col_g1, col_g2 = st.columns([3, 2])
    
    with col_g1:
        st.line_chart(df_age)
        
    with col_g2:
        # 데이터 계산
        percent_news_60s = (df_age.loc["보도", "60대 이상"] / df_age["60대 이상"].sum()) * 100
        percent_news_10s = (df_age.loc["보도", "10대 (13-19세)"] / df_age["10대 (13-19세)"].sum()) * 100
        st.markdown(f"""
        #### 📊 통계 기반 학술적 데이터 풀이
        1. **데이터 팩트 체크:**
            * 60대 이상 인구는 스마트폰 이용 시간의 무려 **{percent_news_60s:.1f}%**를 **'보도(뉴스)'** 시청에 할애하고 있습니다.
            * 반면, 10대 청소년층은 스마트폰 이용 시간 중 뉴스가 차지하는 비중이 단 **{percent_news_10s:.1f}%**에 불과하며, 대신 **'오락'** 장르가 전체의 **{ (df_age.loc["오락", "10대 (13-19세)"]/df_age["10대 (13-19세)"].sum())*100 :.1f}%**를 독차지합니다.
        
        2. **해석과 생각거리:**
            * 흔히 윗세대와 말이 안 통한다고 불평하는 경우가 많습니다. 실제 데이터를 뜯어보면 세대 간 갈등은 가치관 차이 이전에 **"매일 접하는 미디어 장르(정보의 소스)"**가 완전히 다른 데에서 기인합니다. 
            * 10대와 20대는 텍스트 기반의 전통 뉴스가 아닌, SNS 숏폼이나 유튜브 크리에이터를 통해 요약 정보를 습득합니다. 이러한 데이터 불일치를 인지하는 것이 상호 존중과 갈등 해결을 위한 데이터 과학적 분석 결과입니다.
        """)

elif "기업 마케팅과 비즈니스" in selected_field:
    st.subheader("🛒 기업 마케팅과 비즈니스: 기업들의 광고비는 어디로 흘러갈까?")
    
    col_g1, col_g2 = st.columns([3, 2])
    
    with col_g1:
        st.bar_chart(df_device["스마트폰"])
        
    with col_g2:
        # 데이터 계산
        ent_ratio = (df_device.loc["오락", "스마트폰"] / df_device["스마트폰"].sum()) * 100
        st.markdown(f"""
        #### 📊 통계 기반 학술적 데이터 풀이
        1. **데이터 팩트 체크:**
            * 스마트폰 내 전체 이용시간 합계 {df_device["스마트폰"].sum():,.0f}만 분 중 **'오락'**이 차지하는 양만 **{df_device.loc["오락", "스마트폰"]:,.0f}만 분**으로, 전체의 **{ent_ratio:.1f}%**를 단독 지배하고 있습니다.
            * 이는 '드라마&영화'({df_device.loc["드라마&영화", "스마트폰"]:,.0f}만 분)나 '보도'({df_device.loc["보도", "스마트폰"]:,.0f}만 분)를 다 합친 것보다도 압도적인 점유율입니다.
        
        2. **해석과 생각거리:**
            * 광고주와 마케터들이 가장 선호하는 플랫폼은 트래픽(체류시간)이 길게 유지되는 곳입니다. 대중이 모바일에서 머무는 시간의 절반이 '오락'인 만큼, 비즈니스 관점에서 최고의 마케팅 성과를 거두려면 자본을 '오락 콘텐츠 커머스(유튜브 브랜디드 광고, 예능 PPL 등)'에 배분하는 것이 통계적으로 가장 확실한 선택입니다.
        """)

st.markdown("---")
st.caption("데이터 출처: 방송통신위원회 2025년 스마트폰·PC 이용행태 조사 보고서 (실제 2025년 12월 장르별 데이터 반영)")
