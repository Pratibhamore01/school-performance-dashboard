📊 School Performance Analytics Dashboard

Data Analyst – Dashboard 


🚀 Project Overview

This project replicates and enhances the provided dashboard using Python and Streamlit.

The goal was to:
-- Recreate the original dashboard structure
-- Improve UI/UX design
-- Build strong backend data modeling
-- Create a realistic relational dataset
-- Implement meaningful interactivity and insights

The dashboard is fully interactive and dynamically filters data based on user selections.


🛠️ Tools & Technologies

Python 3.8+
Streamlit
Pandas
Plotly
CSV (Relational Dataset)


📂 Project Structure
School_Dashboard
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── teachers.csv
│   ├── performance.csv
│   └── attendance.csv
│
├── outputs/
│   └── screenshots/
│
└── environment/


🗄️ Dataset Description

1️⃣ teachers.csv

teacher_id
teacher_name
department
experience_years
qualification

2️⃣ performance.csv

teacher_id
month
skill_score
student_feedback
overall_score

3️⃣ attendance.csv

teacher_id
month
late_count
leave_days
attrition_flag

📌 Total Records: ~1250+

Proper relational joins were implemented using:

teacher_id
month

📊 Dashboard Features
🔐 Login Page

Secure authentication
Controlled access to dashboard


📈 Dashboard Tab

KPI Cards:

Total Teachers
Average Score
Total Late Count
Attrition Percentage
Monthly Performance Trend (Line Chart)
Teacher Performance Comparison (Bar Chart)
Department Filter (Dynamic)


👩‍🏫 Teacher Tab

Individual Teacher Selection
Overall Score Trend
Skill vs Feedback Comparison
Attendance & Leave Breakdown


⏰ Late Count & Attrition Tab

Monthly Late Count Trend

Attrition Cases Table

Department-level filtering

🧠 Backend & Data Modeling

Clean relational data structure

Proper joins using pandas.merge()

Categorical month ordering for correct sorting

Aggregations:

Average Score → mean()

Total Late Count → sum()

Attrition % → mean() * 100

Realistic attrition simulation (8%)

📈 Key Insights Generated

Department-wise performance trends

Individual teacher performance variation

Late attendance patterns

Attrition tracking

Skill vs Feedback comparison analysis

⚙️ How to Run the Project
Step 1: Install Requirements
pip install -r requirements.txt


Step 2: Run Application
streamlit run app.py


🔑 Login Credentials

Username: admin
Password: admin123

📌 Assumptions

attrition_flag = 1 indicates teacher exit

Scores represent monthly average evaluation

Late count and leave days are monthly totals

Departments distributed realistically

8% attrition probability applied

✅ Conclusion

This dashboard demonstrates:

Strong data modeling

Analytical thinking

Clean UI/UX

Meaningful interactivity

Organized project structure