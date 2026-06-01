import streamlit as st
import pandas as pd
import plotly.express as px

st.title("数据分析可视化平台")

uploaded_file = st.file_uploader("上传Excel文件", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.subheader("数据预览")
    st.dataframe(df)
    st.subheader("数据基本信息")
    st.write(f"共 {df.shape[0]} 行，{df.shape[1]} 列")

    st.sidebar.subheader("图表设置")
    col_x = st.sidebar.selectbox("X轴（横轴）", df.columns)
    col_y = st.sidebar.selectbox("Y轴（纵轴）", df.columns)
    chart_type = st.sidebar.radio("图表类型", ["柱状图", "折线图", "饼图", "散点图"])

    if chart_type == "柱状图":
        fig = px.bar(df, x=col_x, y=col_y)
    elif chart_type == "折线图":
        fig = px.line(df, x=col_x, y=col_y)
    elif chart_type == "饼图":
        fig = px.pie(df, names=col_x, values=col_y)
    else:
        fig = px.scatter(df, x=col_x, y=col_y)

    st.subheader(f"{chart_type}")
    st.plotly_chart(fig)
else:
    st.info("请上传一个 Excel 文件开始分析")
