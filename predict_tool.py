import streamlit as st

# 页面配置
st.set_page_config(page_title="抖音视频AB预测工具", layout="centered")

# 标题
st.title("📊 抖音视频预测 & A/B测试原型工具")
st.markdown("输入两个版本的视频标题和脚本，AI助手将预测哪一个更可能成为爆款，并给出优化建议。")

# 输入表单
with st.form("prediction_form"):
    st.subheader("版本 A")
    title_a = st.text_input("标题 A", "从120斤瘦到95斤，我只做了一件事")
    script_a = st.text_area("脚本 A", "如果你也曾讨厌镜子里的自己，请坚持看完这30秒……")

    st.subheader("版本 B")
    title_b = st.text_input("标题 B", "3个健身小动作，每天10分钟=甩脂20斤！")
    script_b = st.text_area("脚本 B", "每天10分钟，在家搞定减脂。动作一：深蹲30秒。……")

    submitted = st.form_submit_button("开始预测")

if submitted:
    def score_script(title, script):
        score = 0
        keywords = ["瘦", "减脂", "爆", "挑战", "对比", "坚持", "转变", "打卡", "动作", "干货", "揭秘", "30天"]
        for kw in keywords:
            if kw in title:
                score += 5
            if kw in script:
                score += 2
        if any(char.isdigit() for char in title):
            score += 3
        return score

    score_a = score_script(title_a, script_a)
    score_b = score_script(title_b, script_b)

    st.markdown("## 🔍 预测结果")
    st.markdown(f"**版本 A 预测得分：** {score_a}分")
    st.markdown(f"**版本 B 预测得分：** {score_b}分")

    if score_a > score_b:
        st.success("✅ 推荐使用版本 A，它在情绪触发与关键词覆盖上表现更优。")
    elif score_b > score_a:
        st.success("✅ 推荐使用版本 B，它在结构清晰与信息密度上更有优势。")
    else:
        st.info("⚖️ 两个版本得分相近，建议结合封面设计进一步测试。")

    st.markdown("## ✨ 优化建议（AI助手）")
    if "瘦" not in title_a and "减脂" not in title_a:
        st.markdown("- A版标题建议增加关键词：如“减脂”、“瘦身”，提升推荐率。")
    if len(script_b.split()) < 30:
        st.markdown("- B版脚本偏短，可增加挑战感或用户互动引导，如“评论区打1我发完整计划”。")

    st.markdown("_此为原型演示版，后续可添加自动识图、BGM识别与完整AI优化建议。_")
