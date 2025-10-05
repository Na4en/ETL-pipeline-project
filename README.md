# 🧠 University Data ETL Pipeline

## 📋 Project Overview
This project demonstrates a simple ETL (Extract, Transform, Load) process using Python, Pandas, and SQLite.  
It extracts data about universities in the United States, filters for universities in California, and loads the data into a local SQLite database.

## ⚙️ Tech Stack
- Python 3.x  
- Pandas  
- Requests  
- SQLite (via SQLAlchemy)

## 🧱 Steps
1. **Extract** – Fetch data from [Hipolabs University API](http://universities.hipolabs.com)
2. **Transform** – Filter and clean the dataset
3. **Load** – Save the data into a local SQLite database

## 🚀 How to Run
```bash
pip install -r requirements.txt
python etl_pipeline.py
```

The database will be created at:
```
data/university_data.db
```

## 📂 Output Table
| Column | Description |
|--------|--------------|
| name | University Name |
| country | Country |
| domains | Domain Names |
| web_pages | University Websites |
