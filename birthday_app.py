import streamlit as st
import time

# 初始化 session_state
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0

# 標題
st.title("👑 思怡姐 ᕼᗩᑭᑭY ᗷIᖇTᕼᗞᗩY")

# 初始祝賀語
if st.session_state.step == 0:
    st.write("親愛的姐生日快樂🥳🥳準備了幾個禮物給你，你總共有3次機會，看看可以拿到幾個禮物吧 😏")
    if st.button("開始遊戲"):
        st.session_state.step = 1

# 互動流程
elif st.session_state.step == 1:
    st.write(f"請輸入1至5任一數字 (剩下 {3 - st.session_state.attempts} 次機會)")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image("gift.png", caption="1", use_column_width=True)
    with col2:
        st.image("gift.png", caption="2", use_column_width=True)
    with col3:
        st.image("gift.png", caption="3", use_column_width=True)
    with col4:
        st.image("gift.png", caption="4", use_column_width=True)
    with col5:
        st.image("gift.png", caption="5", use_column_width=True)

    choice = st.number_input("請輸入數字：", min_value=1, max_value=5, step=1)
    if st.button("確認選擇"):
        st.session_state.attempts += 1
        if st.session_state.attempts == 1:
            st.write("🎶 獨一無二的祝壽舞來囉，請戴上耳機好好欣賞 🎶")
            video_file = open('videoA.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
        elif st.session_state.attempts == 2:
            st.write("💌 感人肺腑的祝壽卡來囉，請備好衛生紙好好閱讀 💌")
            video_file = open('videoB.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)
        elif st.session_state.attempts == 3:
            st.write("🍽️ 垂涎欲滴的生日餐點來囉，請務必找個時間好好享受 🍽️")
            st.image("qrcode.png", caption="星巴克兌換券", use_column_width=True)
            st.success("祝你生日快樂！🎂")
            st.session_state.step = 2

# 結束畫面
elif st.session_state.step == 2:
    st.write("🎁 所有禮物都已送出，祝你有個美好的一天！")

