import streamlit as st

# 🌈 페이지 설정
st.set_page_config(page_title="✨ MBTI 진로 추천소 ✨", page_icon="💫", layout="wide")

# 💖 CSS 스타일 추가 (배경, 글꼴, 애니메이션 등)
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #FFD1FF, #C2E9FB);
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .title {
        font-size: 60px;
        text-align: center;
        color: #5D3FD3;
        text-shadow: 2px 2px 10px #fff;
    }
    .subtitle {
        font-size: 25px;
        text-align: center;
        color: #333;
    }
    .recommend-box {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
        text-align: center;
        font-size: 22px;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 🎉 제목
st.markdown("<div class='title'>🌟 MBTI로 알아보는 나의 진로 🌟</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>당신의 성격 유형에 딱 맞는 직업을 찾아드려요 💼✨</div>", unsafe_allow_html=True)

st.write("")

# 💫 MBTI 선택
mbti = st.selectbox(
    "👇 당신의 MBTI를 선택하세요 👇",
    ["선택하세요", "ISTJ", "ISFJ", "INFJ", "INTJ",
     "ISTP", "ISFP", "INFP", "INTP",
     "ESTP", "ESFP", "ENFP", "ENTP",
     "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
)

# 🌟 MBTI별 직업 추천 데이터
job_recommendations = {
    "ISTJ": "🧮 회계사, 👮 경찰, 🧰 엔지니어, 📊 공무원",
    "ISFJ": "👩‍⚕️ 간호사, 👨‍🏫 교사, 🧸 사회복지사, 🏠 상담가",
    "INFJ": "🎨 예술가, 💬 심리상담가, ✍️ 작가, 🎭 콘텐츠 크리에이터",
    "INTJ": "🧠 전략기획가, 👩‍💻 데이터사이언티스트, 💼 컨설턴트, 🛰️ 연구원",
    "ISTP": "🔧 기술자, 🚗 자동차정비사, 🧭 파일럿, 🏍️ 모험가",
    "ISFP": "🎶 음악가, 🎨 디자이너, 📷 사진작가, 🌿 플로리스트",
    "INFP": "🖋️ 작가, 🎭 예술가, 💌 상담가, 🌍 NGO활동가",
    "INTP": "🧬 과학자, 👩‍💻 프로그래머, 🧩 철학자, 🧠 연구원",
    "ESTP": "🚀 마케터, 💸 세일즈맨, 🎤 방송인, 🏋️ 트레이너",
    "ESFP": "🎤 배우, 🎶 가수, 💃 댄서, 🛍️ 패션디자이너",
    "ENFP": "🎯 크리에이터, 🧑‍🏫 강사, 🎬 PD, 🌈 기획자",
    "ENTP": "🧠 스타트업 창업자, 🎙️ 토론가, 📈 벤처사업가, 💡 발명가",
    "ESTJ": "🏛️ 관리자, 📋 프로젝트매니저, 👨‍⚖️ 법률가, 🧱 건축가",
    "ESFJ": "👩‍🍳 요리사, 🧑‍🏫 교사, 💕 간호사, 🎉 이벤트플래너",
    "ENFJ": "💬 상담가, 🎤 리더, 🧑‍🏫 교사, 🌍 사회활동가",
    "ENTJ": "👑 CEO, 📈 전략가, 🧠 컨설턴트, 💼 사업가"
}

# 💎 결과 출력
if mbti != "선택하세요":
    st.markdown(f"""
        <div class='recommend-box'>
            <h2>{mbti} ✨ 당신에게 어울리는 직업은...</h2>
            <p>{job_recommendations.get(mbti, "😅 아직 데이터가 없어요!")}</p>
            <br>
            🌟 자신만의 길을 만들어가는 당신을 응원합니다 💫
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<div class='recommend-box'>🔮 MBTI를 선택하면 결과가 나타납니다!</div>", unsafe_allow_html=True)

# 🦋 푸터
st.markdown("<br><hr><p style='text-align:center;'>💖 Created with Streamlit by Your Name 💖</p>", unsafe_allow_html=True)
