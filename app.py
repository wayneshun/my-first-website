import streamlit as st

# 1. 设置页面标题
st.title("👋 许卫栋的个人主页")
st.write("这是我独立开发的第一个个人页面。")

# --- 核心布局部分 ---

# 2. 创建两列布局
# [1, 2] 的意思是：左边占 1 份宽度，右边占 2 份宽度
# 这样右边的文字区域会比左边的图片区域宽一些，看起来更协调
col_left, col_right = st.columns([1, 2])

# 3. 在左边一列放头像
with col_left:
    # 这里用了一个网络头像生成器的链接，你可以换成任何图片链接
    avatar_url = "https://api.dicebear.com/9.x/avataaars/svg?seed=Felix"
    # 把 column 换成 container
    st.image(avatar_url, caption="我是一个努力学习的零基础工程师", use_container_width=True)
# 4. 在右边一列放技能列表
with col_right:
    st.subheader("🛠️ 我的技能栈")

    # 使用 markdown 语法写列表
    st.write("""
    作为一个正在努力学习的初学者，我已经掌握了：

    - 🐍 **Python 基础**: 变量、循环、函数
    - 🌐 **Streamlit**: 快速搭建网页
    - 📊 **数据思维**: 正在学习如何处理数据
    - 🇬🇧 **英语能力**: 能看懂基本的报错信息
    """)

    # 加一个进度条装饰一下，假装在展示熟练度
    st.write("Python 学习进度：")
    st.progress(30)  # 30% 的进度

# --- 底部互动 ---
st.divider()  # 画一条分割线
if st.button("给我的主页点个赞 👍"):
    st.toast("谢谢你的鼓励！🎉")  # 弹出一条小消息

