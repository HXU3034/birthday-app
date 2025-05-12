import streamlit as st
import random

# 設定網頁標題與 emoji
st.set_page_config(page_title="長官生日快樂！", page_icon="🎂")

# 主標題
st.title("🎉 生日快樂，長官！ 🎉")

# 祝賀語選項
messages = [
    "祝您生日快樂，長官！",
    "生日快樂，願您每一天都充滿快樂與成就！",
    "願您擁有一個美好的生日，祝一切順利！"
]

# 使用 radio 元件讓使用者選擇祝賀語
choice = st.radio("請選擇您想要的祝賀語：", messages)

# 送出祝賀
if st.button("🎈 送出祝福"):
    st.success(f"您選擇的是：{choice}")
    st.markdown("---")
    
    # 顯示星巴克兌換券
    st.subheader("🎁 星巴克咖啡兌換券")
    st.markdown("""
    ```
    +--------------------------------------+
    |         🎉 星巴克咖啡兌換券 🎉         |
    |                                      |
    |     憑券可兌換任選一杯咖啡乙杯 ☕     |
    |     有效期限：今年內                |
    |                                      |
    |     🎂 祝您天天開心、事事順利！       |
    +--------------------------------------+
    ```
    👉 請向系統設計者兌換實體飲品 😄
    """)

# 版權
st.caption("由您的敬愛部屬精心打造 🎁")
