# 🤖 AI-Based Group Project Team Builder

## 📌 Overview
This project helps schools and universities automatically **form balanced student project teams** using AI/ML.  
Instead of random assignment, the system considers:
- Skills (Python, Web Dev, AI, etc.)
- Interests
- GPA / performance
- Diversity balance (optional)

The goal is to create **well-rounded teams** where students can complement each other.

---

## ⚙️ Features
✅ Upload student data (CSV/Excel)  
✅ AI clustering algorithm for team formation  
✅ Web interface for teachers/admins  
✅ Export teams in CSV/Excel format  
✅ Extendable to career path recommendations  

---

## 🛠️ Tech Stack
- **Python** (Pandas, Scikit-Learn, Flask)
- **HTML/CSS/JS** for frontend
- **Matplotlib/Seaborn** for data visualization
- **Jupyter Notebook** for prototyping

---

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/ai-team-builder.git
   cd ai-team-builder
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run sample algorithm:
   ```bash
   python src/team_builder.py
   ```

4. Run web app:
   ```bash
   python webapp/app.py
   ```

---

## 📊 Example Dataset
`students.csv`:
| Name      | Skills              | Interests       | GPA |
|-----------|---------------------|-----------------|-----|
| A. Albern | Python, ML          | AI, Research    | 8.5 |
| Rahul     | Web Dev, JS         | Startup, Design | 7.8 |
| Priya     | Data Science, SQL   | Analytics, Data | 9.0 |

---

## 🔮 Future Improvements
- Add **NLP resume parser** (students upload CVs)
- Use **Graph Neural Networks** for smarter grouping
- Integrate with **Google Classroom / Moodle**

---

## 📜 License
MIT License
