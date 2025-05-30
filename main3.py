import streamlit as st

# 질문 목록
questions = [
    "1. 저는 새로운 사람을 만나는 것을 좋아합니다.",
    "2. 계획 없이 즉흥적으로 행동하는 것을 선호합니다.",
    "3. 감정보다 논리를 더 중시합니다.",
    "4. 대규모 모임보다 소규모 모임이 더 편안합니다.",
    "5. 개방적인 대화보다 깊이 있는 대화를 선호합니다.",
    "6. 이론적인 아이디어를 제시하는 것을 좋아합니다.",
    "7. 다른 사람의 기분을 잘 이해합니다.",
    "8. 실패 보다 성공을 더 중시합니다.",
    "9. 세부적인 것보다 전체적인 경향을 중요하게 생각합니다.",
    "10. 무언가를 계획하고 미리 준비하는 것을 좋아합니다."
]

# MBTI 설문 응답 초기화
responses = []

# Streamlit 애플리케이션 제목
st.title("MBTI 유형 검사")

# 질문 출력 및 응답 수집
for question in questions:
    response = st.radio(question, options=["예", "아니오"], key=question)
    responses.append(response)

# 결과 확인 버튼
if st.button("결과 확인"):
    # MBTI 유형 계산
    e_i = sum(1 for response in responses[:5] if response == "예")
    t_f = sum(1 for response in responses[2:4] if response == "예") + sum(1 for response in responses[7:8] if response == "아니오")
    j_p = sum(1 for response in responses[1:2] if response == "예") + sum(1 for response in responses[6:9] if response == "아니오")

    # 유형 결정
    e_i_type = "E" if e_i >= 3 else "I"
    t_f_type = "T" if t_f >= 2 else "F"
    j_p_type = "J" if j_p >= 2 else "P"

    mbti_type = e_i_type + t_f_type + j_p_type
    st.write(f"당신의 MBTI 유형은: **{mbti_type}**입니다.")

