import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="School Analytics Dashboard", layout="wide")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
teachers = pd.read_csv("teachers.csv")
performance = pd.read_csv("performance.csv")
attendance = pd.read_csv("attendance.csv")

# --------------------------------------------------
# DATA MODELING (JOINS)
# --------------------------------------------------
df = performance.merge(teachers, on="teacher_id", how="left")
df_full = df.merge(attendance, on=["teacher_id", "month"], how="left")

# Fix month order for proper sorting
month_order = ["Jan","Feb","Mar","Apr","May","Jun",
               "Jul","Aug","Sep","Oct","Nov","Dec"]

df_full["month"] = pd.Categorical(df_full["month"],
                                  categories=month_order,
                                  ordered=True)

# --------------------------------------------------
# LOGIN SYSTEM
# --------------------------------------------------
if "login_status" not in st.session_state:
    st.session_state.login_status = False

def login():
    st.title("🔐 School Performance Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state.login_status = True
        else:
            st.error("Invalid Credentials")

if not st.session_state.login_status:
    login()
    st.stop()

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go To", ["Dashboard",
                                  "Teacher",
                                  "Late Count & Attrition"])

# Department Filter
st.sidebar.markdown("---")
dept_selected = st.sidebar.selectbox(
    "Select Department",
    ["All"] + list(teachers["department"].unique())
)

if dept_selected != "All":
    df_full = df_full[df_full["department"] == dept_selected]

# --------------------------------------------------
# DASHBOARD TAB
# --------------------------------------------------
if page == "Dashboard":

    st.title("📊 Overall Performance Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Teachers",
                df_full["teacher_id"].nunique())

    col2.metric("Average Score",
                round(df_full["overall_score"].mean(), 2))

    col3.metric("Total Late Count",
                int(df_full["late_count"].sum()))

    col4.metric("Attrition %",
                round(df_full["attrition_flag"].mean()*100, 2))

    st.markdown("---")

    # Performance Trend
    st.subheader("📈 Monthly Performance Trend")
    trend = df_full.groupby("month")["overall_score"].mean().reset_index()
    trend = trend.sort_values("month")

    fig1 = px.line(trend,
                   x="month",
                   y="overall_score",
                   markers=True)
    st.plotly_chart(fig1, use_container_width=True)

    # Department Average Chart
    st.subheader("🏆 Teacher Average Performance")
    teacher_perf = df_full.groupby("teacher_name")["overall_score"].mean().reset_index()

    fig2 = px.bar(teacher_perf,
                  x="teacher_name",
                  y="overall_score")
    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# TEACHER TAB
# --------------------------------------------------
elif page == "Teacher":

    st.title("👩‍🏫 Individual Teacher Analysis")

    teacher_selected = st.selectbox(
        "Select Teacher",
        sorted(df_full["teacher_name"].unique())
    )

    teacher_df = df_full[df_full["teacher_name"] == teacher_selected]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Overall Score Trend")
        fig3 = px.line(teacher_df,
                       x="month",
                       y="overall_score",
                       markers=True)
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        st.subheader("Skill vs Feedback Comparison")
        fig4 = px.bar(teacher_df,
                      x="month",
                      y=["skill_score", "student_feedback"],
                      barmode="group")
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("---")
    st.subheader("Attendance & Leave Details")
    st.dataframe(
        teacher_df[["month",
                    "skill_score",
                    "student_feedback",
                    "overall_score",
                    "late_count",
                    "leave_days"]]
        .sort_values("month")
    )

# --------------------------------------------------
# LATE COUNT & ATTRITION TAB
# --------------------------------------------------
elif page == "Late Count & Attrition":

    st.title("⏰ Late Count & Attrition Analysis")

    # Late Trend
    st.subheader("Monthly Late Count Trend")
    late_trend = df_full.groupby("month")["late_count"].sum().reset_index()
    late_trend = late_trend.sort_values("month")

    fig5 = px.line(late_trend,
                   x="month",
                   y="late_count",
                   markers=True)
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("---")

    # Attrition Table
    st.subheader("Attrition Cases")

    attrition_df = df_full[df_full["attrition_flag"] == 1][
        ["teacher_name", "department", "month"]
    ].sort_values("month")

    if attrition_df.empty:
        st.success("No Attrition Cases Found 🎉")
    else:

        st.dataframe(attrition_df)
