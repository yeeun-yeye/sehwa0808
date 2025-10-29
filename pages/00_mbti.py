import streamlit as st

st.set_page_config(page_title="🌟 MBTI 기반 진로 추천!", page_icon="💫", layout="wide")

st.title("💖 MBTI로 보는 나의 인생 직업 ✨")
st.subheader("너의 성격 속에 숨겨진 미래 직업을 찾아보자! 🚀")

mbti = st.selectbox(
    "🌈 너의 MBTI를 선택해줘!",
    [
        "INFP", "ENFP", "INFJ", "ENFJ",
        "INTP", "ENTP", "INTJ", "ENTJ",
        "ISFP", "ESFP", "ISTP", "ESTP",
        "ISFJ", "ESFJ", "ISTJ", "ESTJ"
    ]
)

info = {
    "INFP": {
        "emoji": "🦋💭🌷",
        "character": "라푼젤 (Tangled)",
        "trait": "감성 폭발형 몽상가 💖 — 세상에 없는 낭만을 그리며 감정의 파도 속을 헤엄치는 타입!",
        "truth": "팩폭 💥 : 이상은 높지만, 현실엔 약함. 계획보다 꿈이 앞서서 종종 길을 잃는다!",
        "job": "작가 ✍️, 심리상담사 💬, 일러스트레이터 🎨, 콘텐츠 크리에이터 🌈",
        "match": "ENFJ 💞 or ENFP 💫"
    },
    "ENFP": {
        "emoji": "🔥🎉🌈",
        "character": "알라딘 (Aladdin)",
        "trait": "자유로운 영혼의 모험가 💫 — 틀에 박힌 삶을 싫어하고, 세상 모든 게 흥미로운 타입!",
        "truth": "팩폭 💥 : 열정은 넘치지만 오래 못 간다… 시작은 불꽃, 끝은 재.",
        "job": "광고기획자 📺, 유튜버 📸, 마케터 💡, 스타트업 창업자 🚀",
        "match": "INFJ 💞 or INTJ 💫"
    },
    "INFJ": {
        "emoji": "🌙🕊️💎",
        "character": "엘사 (Frozen)",
        "trait": "조용한 이상주의자 ❄️ — 세상을 따뜻하게 바꾸고 싶지만, 속마음은 쉽게 말 못 하는 타입.",
        "truth": "팩폭 💥 : 남 생각 너무 하다가 자기 마음은 꽁꽁 얼어붙음.",
        "job": "심리학자 🧠, 상담교사 🍀, 작가 🖋️, 사회운동가 🌍",
        "match": "ENFP 💞 or ENTP 💫"
    },
    "ENFJ": {
        "emoji": "🌟💝🫶",
        "character": "벨 (Beauty and the Beast)",
        "trait": "따뜻한 리더 🌸 — 사람을 진심으로 아끼고, 모두가 잘 되길 바라는 진정한 서포터!",
        "truth": "팩폭 💥 : 남 챙기느라 정작 본인 인생은 뒷전 😭",
        "job": "교사 👩‍🏫, 상담가 💬, 홍보전문가 📣, 사회복지사 🕊️",
        "match": "INFP 💞 or ISFP 💫"
    },
    "INTP": {
        "emoji": "🧩🧠📚",
        "character": "이안 (Onward)",
        "trait": "논리의 미로를 즐기는 사색가 ⚙️ — 비합리적인 건 딱 질색!",
        "truth": "팩폭 💥 : 생각만 많고 실행은 느림. 현실감 제로.",
        "job": "연구원 🔬, 프로그래머 💻, 과학자 🧪, 철학자 📖",
        "match": "ENTJ 💞 or ESTJ 💫"
    },
    "ENTP": {
        "emoji": "⚡🎭🔥",
        "character": "잭 스패로우 (Pirates of the Caribbean)",
        "trait": "입담 최강! 토론광 해적왕 🗣️ — 규칙을 깨며 세상을 새롭게 본다.",
        "truth": "팩폭 💥 : 말은 많고 실행은 글쎄… 계획보다 즉흥이 먼저!",
        "job": "기획자 💡, PD 🎥, CEO 💼, 혁신 컨설턴트 🌐",
        "match": "INFJ 💞 or INTJ 💫"
    },
    "INTJ": {
        "emoji": "🧊🎯🔮",
        "character": "말레피센트 (Maleficent)",
        "trait": "전략형 천재 🧠 — 머릿속에 이미 세상의 설계도가 완성돼 있음.",
        "truth": "팩폭 💥 : 완벽주의 + 감정표현 0%, 인간관계 피로감 200%",
        "job": "전략가 🧩, 데이터분석가 📊, 변호사 ⚖️, 연구자 🧬",
        "match": "ENFP 💞 or ENTP 💫"
    },
    "ENTJ": {
        "emoji": "👑🔥🚀",
        "character": "심바 (The Lion King)",
        "trait": "카리스마 리더 💪 — 목표를 정하면 절대 물러서지 않는 승부사!",
        "truth": "팩폭 💥 : 효율 빼면 남는 게 없음. 감정표현 = ERROR ❌",
        "job": "CEO 💼, 경영컨설턴트 📊, 변호사 ⚖️, 관리자 🧱",
        "match": "INTP 💞 or INFP 💫"
    },
    "ISFP": {
        "emoji": "🌸🎶🍃",
        "character": "포카혼타스 (Pocahontas)",
        "trait": "예술 감성 장인 🎨 — 감정의 색채로 세상을 느끼는 사람.",
        "truth": "팩폭 💥 : 갈등 싫어서 회피하다가 혼자 끙끙 앓음 🥲",
        "job": "디자이너 🎨, 플로리스트 🌷, 포토그래퍼 📷, 메이크업아티스트 💄",
        "match": "ESFP 💞 or ENFJ 💫"
    },
    "ESFP": {
        "emoji": "🎤🌞💃",
        "character": "에리얼 (The Little Mermaid)",
        "trait": "파티의 중심 🌟 — 매사에 긍정적이고, 인생은 즐기는 거야!",
        "truth": "팩폭 💥 : 즉흥적이라 계획 세우면 바로 망함 😂",
        "job": "연예인 🎤, 이벤트기획자 🎪, 여행가 ✈️, 아나운서 🎙️",
        "match": "ISFP 💞 or ESTP 💫"
    },
    "ISTP": {
        "emoji": "🛠️🏍️😎",
        "character": "플린 라이더 (Tangled)",
        "trait": "쿨한 해결사 ⚙️ — 감정보다 행동! 문제 생기면 바로 수리 들어감.",
        "truth": "팩폭 💥 : 감정표현 부족해서 오해받기 쉬움.",
        "job": "엔지니어 🔧, 정비사 ⚙️, 파일럿 ✈️, 프로게이머 🎮",
        "match": "ESTP 💞 or ESFP 💫"
    },
    "ESTP": {
        "emoji": "⚡🏎️🔥",
        "character": "버즈 라이트이어 (Toy Story)",
        "trait": "액션형 현실주의자 🚀 — ‘생각은 나중에!’ 지금이 중요해!",
        "truth": "팩폭 💥 : 계획? 그런 건 필요 없어 😏 하지만 가끔 사고침.",
        "job": "사업가 💼, 스포츠선수 ⚽, 세일즈맨 💰, 기자 📰",
        "match": "ISTP 💞 or ESFP 💫"
    },
    "ISFJ": {
        "emoji": "🧺🩵🌿",
        "character": "신데렐라 (Cinderella)",
        "trait": "헌신의 천사 💎 — 남을 도와주는 게 행복인 따뜻한 사람.",
        "truth": "팩폭 💥 : ‘괜찮아요’가 입버릇… 근데 사실은 안 괜찮음 😢",
        "job": "간호사 🏥, 교사 👩‍🏫, 행정직 🗂️, 사회복지사 🌸",
        "match": "ESFJ 💞 or ESTJ 💫"
    },
    "ESFJ": {
        "emoji": "🎀🍰💐",
        "character": "안나 (Frozen)",
        "trait": "친절한 사회형 인간 🌈 — 모두의 행복이 곧 나의 행복!",
        "truth": "팩폭 💥 : 남 눈치 보다가 자기 생각은 뒤로 미룸 🥹",
        "job": "교사 👩‍🏫, 홍보담당 📣, 간호사 🏥, 인사담당자 🧾",
        "match": "ISFJ 💞 or ISTJ 💫"
    },
    "ISTJ": {
        "emoji": "📘🧱🏛️",
        "character": "세바스찬 (The Little Mermaid)",
        "trait": "원칙주의자 🧭 — 계획 없으면 불안! 질서와 책임감의 화신.",
        "truth": "팩폭 💥 : 융통성 0, 즉흥상황에서 오류남 ⚠️",
        "job": "공무원 🏛️, 회계사 📊, 연구원 🧬, 군인 🪖",
        "match": "ESFJ 💞 or ESTJ 💫"
    },
    "ESTJ": {
        "emoji": "🦁🏆💼",
        "character": "우디 (Toy Story)",
        "trait": "현실형 리더 💪 — 팀을 이끌고 목표를 향해 달리는 추진력의 상징!",
        "truth": "팩폭 💥 : 자기 방식만 옳다고 믿는 경향 강함 😤",
        "job": "경영자 💼, 경찰관 🚔, 변호사 ⚖️, 관리자 🧱",
        "match": "ISTJ 💞 or INTP 💫"
    }
}

if mbti:
    data = info[mbti]
    st.markdown(f"## {data['emoji']} **{mbti} — {data['character']} 스타일!**")
    st.markdown(f"### 💫 {data['trait']}")
    st.markdown(f"### 😈 {data['truth']}")
    st.markdown(f"### 💼 어울리는 직업: {data['job']}")
    st.markdown(f"### 💞 찰떡궁합 MBTI: {data['match']}")

st.markdown("---")
st.caption("✨ 만든이: 예은 ✨ | ☁️ Powered by Streamlit & ChatGPT GPT-5 💫")
