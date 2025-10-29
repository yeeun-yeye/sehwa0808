import streamlit as st

# 🌈 페이지 설정
st.set_page_config(page_title="✨ MBTI 진로 추천소 ✨", page_icon="💫", layout="wide")

# 💖 CSS 스타일 추가
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
        background-color: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        text-align: center;
        font-size: 22px;
        margin-top: 40px;
        transition: all 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# 🎉 제목
st.markdown("<div class='title'>🌟 MBTI로 알아보는 나의 진로 🌟</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>성격도 팩폭하고, 디즈니 속 나도 찾아보자! 🏰💼</div>", unsafe_allow_html=True)
st.write("")

# 💫 MBTI 선택
mbti = st.selectbox(
    "👇 당신의 MBTI를 선택하세요 👇",
    ["선택하세요", "ISTJ", "ISFJ", "INFJ", "INTJ",
     "ISTP", "ISFP", "INFP", "INTP",
     "ESTP", "ESFP", "ENFP", "ENTP",
     "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
)

# 🌟 MBTI별 정보 데이터
mbti_data = {
    "ISTJ": {
        "emoji": "🐢",
        "color": "#D0E6A5",
        "job": "🧮 회계사, 👮 경찰, 🧰 엔지니어, 📊 공무원",
        "roast": "“규칙 어기면 스트레스 받죠? 근데 가끔 너무 딱딱해요 😅”",
        "disney": "🦁 무파사 (라이온킹) – 책임감 강하고, 원칙적인 리더!",
        "quote": "당신의 성실함은 세상을 움직이는 숨은 엔진이에요 ⚙️"
    },
    "ISFJ": {
        "emoji": "🐰",
        "color": "#FFDD95",
        "job": "👩‍⚕️ 간호사, 🧑‍🏫 교사, 🧸 사회복지사, 🏠 상담가",
        "roast": "“남 챙기느라 정작 본인은 맨날 후순위 🥹”",
        "disney": "🧚 신데렐라 – 묵묵하지만 진심으로 사람을 아끼는 따뜻한 영혼 💖",
        "quote": "당신의 다정함은 세상을 포근하게 감싸요 ☁️"
    },
    "INFJ": {
        "emoji": "🦋",
        "color": "#FFC9DE",
        "job": "🎨 예술가, 💬 심리상담가, ✍️ 작가, 🎭 콘텐츠 크리에이터",
        "roast": "“남들 고민 다 들어주고 자기 고민은 일기장에 써요 📖”",
        "disney": "🌹 벨 (미녀와 야수) – 깊은 내면과 철학적 사색의 여왕 👑",
        "quote": "당신의 통찰은 세상에 의미를 불어넣어요 💫"
    },
    "INTJ": {
        "emoji": "🦉",
        "color": "#A8E6CF",
        "job": "🧠 전략기획가, 👩‍💻 데이터사이언티스트, 💼 컨설턴트, 🛰️ 연구원",
        "roast": "“마음속으로 ‘저건 비효율적이야’ 100번 외치죠 🤓”",
        "disney": "🧊 엘사 (겨울왕국) – 차가워 보이지만 내면은 따뜻한 완벽주의자 ❄️",
        "quote": "당신의 논리는 현실을 바꾸는 설계도예요 🏗️"
    },
    "INFP": {
        "emoji": "🌷",
        "color": "#B5EAD7",
        "job": "🖋️ 작가, 🎭 예술가, 💌 상담가, 🌍 NGO활동가",
        "roast": "“현실이 너무 시끄러워서 상상의 나라로 도망 중 🌈”",
        "disney": "🐠 에리얼 (인어공주) – 이상주의자, 자유와 꿈을 좇는 낭만주의자 💖",
        "quote": "당신의 감성은 세상을 더 아름답게 물들여요 🎨"
    },
    "ENTP": {
        "emoji": "🐉",
        "color": "#E2F0CB",
        "job": "🧠 스타트업 창업자, 🎙️ 토론가, 📈 벤처사업가, 💡 발명가",
        "roast": "“말싸움에서 진 적 없지만 싸움 끝나면 현타 와요 😂”",
        "disney": "🦊 주디 (주토피아) – 호기심 많고 말 잘하고 아이디어 뱅크 💥",
        "quote": "당신의 재치는 모든 벽을 허무는 힘이에요 🚀"
    },
    "ENFP": {
        "emoji": "🔥",
        "color": "#FFDAC1",
        "job": "🎯 크리에이터, 🧑‍🏫 강사, 🎬 PD, 🌈 기획자",
        "roast": "“열정 100℃, 하지만 집중력은 잠깐만요~ ☕️”",
        "disney": "☀️ 라푼젤 – 호기심과 에너지로 세상을 물들여요 🌸",
        "quote": "당신의 열정은 주위에 빛을 전하는 태양이에요 🌞"
    },
    "ENTJ": {
        "emoji": "🦁",
        "color": "#B0E0E6",
        "job": "👑 CEO, 📈 전략가, 🧠 컨설턴트, 💼 사업가",
        "roast": "“비전은 거대하지만… 팀원은 이미 지쳐있어요 😅”",
        "disney": "🐾 우디 (토이 스토리) – 리더십 넘치지만 은근히 귀여운 완벽주의자 🤠",
        "quote": "당신의 추진력은 세상을 움직이는 엔진이에요 ⚡️"
    },
}

# 💎 결과 출력
if mbti != "선택하세요":
    data = mbti_data.get(mbti)
    if data:
        st.markdown(f"""
            <style>
            body {{
                background: linear-gradient(135deg, {data['color']}, white);
            }}
            </style>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class='recommend-box'>
            <h1>{data['emoji']} {mbti}</h1>
            <h2>✨ 당신에게 어울리는 직업은...</h2>
            <p>{data['job']}</p>
            <br>
            <h3>{data['roast']}</h3>
            <p>💫 디즈니로 비유하자면... <b>{data['disney']}</b></p>
            <p>🌟 {data['quote']}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("😅 아직 이 MBTI에 대한 정보가 없어요!")
else:
    st.markdown("<div class='recommend-box'>🔮 MBTI를 선택하면 성격 팩폭과 캐릭터 매칭 결과가 나타납니다!</div>", unsafe_allow_html=True)

st.markdown("<br><hr><p style='text-align:center;'>💖 Created with Streamlit by 김예은 💖</p>", unsafe_allow_html=True)
