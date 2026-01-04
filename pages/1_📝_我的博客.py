import streamlit as st

# ==========================================
# 1. 博客文章列表 (注意格式：大括号 {} 之间要有逗号)
# ==========================================
posts = [
    {
        "title": "第一篇：关于战略规划的思考",
        "date": "2026-01-05",
        "summary": "这是我的第一篇博客文章...",
        "content": """
        ### 深度思考的正文
        这里是文章的详细内容。
        - 观点 1
        - 观点 2
        """
    },
    {
        "title": "第二篇：我的职业选择",
        "date": "2026-01-15",
        "summary": "回顾过去几年的职业生涯...",
        "content": """
        ### 职业选择的故事
        那是一个风雨交加的夜晚...
        """
    },
    {
        "title": "第三篇：我的人生故事",
        "date": "2026-01-30",
        "summary": "这是第三篇的简介...",
        "content": """
        ### 我的人生故事
        这里是第三篇文章的内容...
        """
    }
]

# ==========================================
# 2. 页面显示逻辑 (不用动)
# ==========================================

# 初始化状态
if "current_post" not in st.session_state:
    st.session_state.current_post = None

# 如果有选中的文章 -> 显示文章详情
if st.session_state.current_post:
    post = st.session_state.current_post
    if st.button("⬅️ 返回列表"):
        st.session_state.current_post = None
        st.rerun()

    st.title(post["title"])
    st.caption(f"发布日期: {post['date']}")
    st.markdown(post["content"])

# 否则 -> 显示文章列表
else:
    st.title("📝 我的博客")
    for i, post in enumerate(posts):
        st.subheader(post["title"])
        st.caption(post["date"])
        st.write(post["summary"])
        if st.button("阅读全文", key=i):
            st.session_state.current_post = post
            st.rerun()
        st.divider()
