import streamlit as st

# 1. 页面基础设置 (设置网页标签页的名字和图标)
st.set_page_config(
    page_title="许卫栋的个人主页",
    page_icon="💼",
    layout="wide"  # 使用宽屏模式，让页面更大气
)

# --- 侧边栏：个人概况 ---
with st.sidebar:
    # [图片区域]
    # 这里我放了一个灰色的占位图，请把引号里的链接换成你的真实照片链接
    # 如果是本地照片，就把链接换成文件名，如 "my_photo.jpg"
    photo_url = "https://media.licdn.com/dms/image/v2/D5603AQEVwtgpSenwsA/profile-displayphoto-shrink_400_400/B56ZOuwUZJGcAg-/0/1733803725997?e=1769040000&v=beta&t=XwLvE0byrcUdaCfy5Cdhb3kQza9zTvwrgaWet863w0A"
    st.image(photo_url, caption="许卫栋", use_container_width=True)

    st.markdown("---")  # 分割线

    # [联系方式]
    st.subheader("📬 联系方式")
    st.write("📧 **Email**:")
    st.code("xuweidong@ksztone.com", language="text")  # 使用代码框方便复制

    st.write("📧 **微信**:")
    st.code("wayneshun", language="text")  # 使用代码框方便复制

    st.write("📍 **职业**:")
    st.write("CONSTRUCT 战略负责人")

# --- 主页面：详细经历 ---

# 标题区域
st.title("👋 你好，我是许卫栋")
st.write("在CONSTRUCT负责战略和新业务探索。")

st.divider()  # 画一条长分割线

# 2. 教育背景板块
st.header("🎓 教育背景")

# 使用列布局来让时间显示在右边，学校显示在左边
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader("中南财经政法大学")
    st.write("本科 | 劳动与社会保障")  # 如果你想加专业可以改这里
with col2:
    st.write("📅 2008 - 2012")

st.divider()

# 3. 工作经历板块
st.header("💼 主要工作经历")

# 这里我们用“字典”结构：左边是公司，冒号后面是具体经历
# 你可以在引号里随意修改文字
experiences = {
    "九合创投 (Unity Ventures)  2018-2021": "在此期间主要负责社交和娱乐领域的创业公司，同时也对消费领域感兴趣，负责早期项目的筛选与评估。投资了Uki 、Scooper等公司，自己个人投资了Litmatch 、斑码编程等公司。",
    "璀璨资本 (Bright Capital)  2017-2018": "专注于早期投资，深入研究了消费互联网领域的商业模式，投资了口袋狼人杀等项目。",
    "盛大 (Shanda) 2015-2017": "参与了VR领域的投资，负责了数十家公司的投后管理工作。",
    "腾讯 (Tencent) 2013-2015": "在职期间积累了深厚的产品思维与用户运营经验。",
    "新浪 (Sina) 2012-2013": "早期互联网从业经历，建立了对网络媒体和内容社区的深刻认知。"
}

# 遍历字典，company 是公司名，desc 是描述
for company, desc in experiences.items():
    with st.container():
        # 这里的 f"{company}" 是把公司名字填进去
        st.subheader(f"🏢 {company}")

        # 显示对应的工作描述
        st.write(desc)

        # 加个分割线，让排版更清晰
        st.markdown("---")


    # 4. 底部互动
st.info("如果您对战略合作或投资机会感兴趣，欢迎通过邮件与我联系。")




