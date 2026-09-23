# Shivam Bhardwaj - IPL Match Prediction Project

## Project Overview

This project analyzes Indian Premier League (IPL) match data from 2008 to 2026 to predict the likely match winner using historical pattern analysis. The system uses machine learning to evaluate match conditions such as team selection, toss decision, city, target score, and venue-related patterns to estimate whether the chasing team or the team batting first is more likely to win.

## Objective

The main goal is to build a complete prediction application with both a backend API and a frontend dashboard. This makes the project more practical and presentation-friendly for an internship or academic demonstration.

## Dataset

- Dataset Name: IPL Matches Data 2008-2026
- Source: Kaggle
- Link: https://www.kaggle.com/code/shayanzk/ipl-2008-2026-what-19-seasons-of-data-actually-say
- File used in this project: IPL_Matches_Data_2008_2026.csv
- Dataset folder: project root

## Features Used

- team1
- team2
- city
- toss_winner
- toss_decision
- target
- winner
- result_type

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Joblib
- Streamlit
- FastAPI
- Uvicorn

> If Windows blocks the XGBoost native DLL, the application automatically continues with Logistic Regression and Random Forest instead of failing to load the frontend.

## Methodology

1. Load the IPL dataset from the project root or data folder
2. Clean and standardize team names
3. Filter completed matches and relevant teams
4. Engineer batting-first and chasing-team variables
5. Train and compare multiple models
6. Save the best-trained model
7. Expose prediction through FastAPI
8. Use Streamlit for user interaction and visualization

## Dashboard Features

- Match prediction form with team, city, toss, and target inputs
- Predicted winner and confidence score
- Historical KPI cards for completed matches, chase-win rate, and average target
- Outcome comparison chart for chasing versus batting-first teams
- City distribution chart showing the most represented venues in the dataset

The charts are rendered with lightweight HTML/CSS bars instead of Streamlit's Altair chart helpers, so the frontend does not require PyArrow's native DLL on Windows systems with application-control restrictions.

## Models Used

- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

## Project Structure

- app.py
- backend/
  - **init**.py
  - model.py
  - api.py
- IPL_Matches_Data_2008_2026.csv
- model/
  - ipl_match_model.pkl
- requirements.txt
- README.md
- ShivamBhardwaj_ProjectReport.docx

## Setup Instructions

1. Install Python 3.9 or above.
2. Open the project folder.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

The application uses `IPL_Matches_Data_2008_2026.csv` from the project root. It also supports the same file under `data/`; see the dataset candidates in `backend/model.py`.

## Run the Application

### Frontend (Streamlit)

Open one terminal in the project folder and run:

```bash
streamlit run app.py
```

Open the frontend at `http://localhost:8501`.

### Backend API (FastAPI)

Open a second terminal in the same project folder and run:

```bash
python -m uvicorn backend.api:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

Example API request:

```bash
curl -X POST http://127.0.0.1:8000/predict ^
  -H "Content-Type: application/json" ^
  -d "{\"team1\":\"Mumbai Indians\",\"team2\":\"Chennai Super Kings\",\"city\":\"Mumbai\",\"toss_winner\":\"Mumbai Indians\",\"toss_decision\":\"field\",\"target\":170}"
```

## Expected Output

When the backend runs successfully, the app loads the IPL dataset, trains the model, and predicts the current match scenario based on the input values.

## Result Summary

The project compares multiple machine learning models and selects the best one for prediction. The output includes the predicted winner and a confidence score based on the user's input values.

The dashboard also presents descriptive statistics and charts from the historical dataset so that the prediction is shown alongside useful match context.

## Conclusion

This project demonstrates practical data analytics and AI usage in sports prediction. It also showcases a modern application architecture with both a machine learning backend and a user-friendly frontend.

## Limitations

- The model learns from historical match conditions and is not a guaranteed forecast of future seasons.
- It does not use live player form, injuries, playing XI announcements, or live match data.
- Predictions are estimates and should be interpreted alongside the confidence score.

## Author

Shivam Bhardwaj

## Internship Context

IBM SkillsBuild Data Analytics with AI Academic Internship Program
BharatCares in association with AICTE
