import streamlit as st

# 设置页面标题
st.set_page_config(page_title="我的博客", page_icon="📝")

st.title("📝 许卫栋的博客")

# 模拟一篇博客文章
st.subheader("第一篇：关于战略规划的思考")
st.caption("发布日期：2024-01-20")
st.write("""
这是我的第一篇博客文章。在这里，我分享关于 CONSTRUC 战略规划的一些深度思考...
(你可以在这里写很长的文章内容)
""")
st.markdown("---")

# 模拟第二篇
st.subheader("第二篇：从腾讯到九合创投")
st.caption("发布日期：2023-12-15")
st.write("回顾过去几年的职业生涯，我发现...")
