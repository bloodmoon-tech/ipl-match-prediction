

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import joblib


def run_ipl_pipeline():
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_FOLDER_PATH = os.path.join(SCRIPT_DIR, 'data')
    DEFAULT_DATASET_PATH = os.path.join(SCRIPT_DIR, 'ipl_comprehensive_dataset.csv')
    PROJECT_DATASET_PATH = os.path.join(DATA_FOLDER_PATH, 'IPL_Matches_Data_2008_2026.csv')
    FALLBACK_DATASET_PATH = r'C:\Users\SHIVAM\Downloads\IPL_Matches_Data_2008_2026.csv'

    if os.path.exists(DEFAULT_DATASET_PATH):
        dataset_path = DEFAULT_DATASET_PATH
    elif os.path.exists(PROJECT_DATASET_PATH):
        dataset_path = PROJECT_DATASET_PATH
    elif os.path.exists(FALLBACK_DATASET_PATH):
        dataset_path = FALLBACK_DATASET_PATH
    else:
        raise FileNotFoundError(
            f"Dataset file not found in either: {DEFAULT_DATASET_PATH}, {PROJECT_DATASET_PATH}, or {FALLBACK_DATASET_PATH}\n"
            "Please place the CSV file in the same folder as this script or in the project data folder."
        )

    df = pd.read_csv(dataset_path)
    
   
    team_mappings = {
        'Delhi Daredevils': 'Delhi Capitals',
        'Kings XI Punjab': 'Punjab Kings',
        'Royal Challengers Bangalore': 'Royal Challengers Bengaluru',
        'Deccan Chargers': 'Sunrisers Hyderabad'
    }
    
    for col in ['team1', 'team2', 'toss_winner', 'winner']:
        df[col] = df[col].replace(team_mappings)
        
   
    active_teams = [
        'Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bengaluru',
        'Kolkata Knight Riders', 'Punjab Kings', 'Chennai Super Kings',
        'Rajasthan Royals', 'Delhi Capitals'
    ]
    
    df = df[df['team1'].isin(active_teams) & df['team2'].isin(active_teams)]
    df = df[df['result_type'] == 'complete'].dropna(subset=['winner', 'city', 'venue'])

    df['bat_first'] = np.where(
        (df['toss_winner'] == df['team1']) & (df['toss_decision'] == 'bat'), df['team1'],
        np.where((df['toss_winner'] == df['team2']) & (df['toss_decision'] == 'bat'), df['team2'],
        np.where((df['toss_winner'] == df['team1']) & (df['toss_decision'] == 'field'), df['team2'], df['team1']))
    )
    
    df['bat_second'] = np.where(df['bat_first'] == df['team1'], df['team2'], df['team1'])
    df['first_innings_runs'] = np.where(df['bat_first'] == df['team1'], df['team1_runs'], df['team2_runs'])
    df['target'] = df['first_innings_runs'] + 1
    
  
    df['chase_won'] = np.where(df['winner'] == df['bat_second'], 1, 0)
    
    
    features_df = df[['bat_first', 'bat_second', 'city', 'toss_winner', 'toss_decision', 'target', 'chase_won']].dropna()
    
    X = features_df.drop(columns=['chase_won'])
    y = features_df['chase_won']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    categorical_cols = ['bat_first', 'bat_second', 'city', 'toss_winner', 'toss_decision']
    trf = ColumnTransformer([
        ('trf', OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore'), categorical_cols)
    ], remainder='passthrough')
    
   
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'XGBoost': XGBClassifier(n_estimators=100, learning_rate=0.05, random_state=42)
    }
    
    print("--- Model Performance Metrics ---")
    best_pipe = None
    best_acc = 0.0
    
    for name, model in models.items():
        pipe = Pipeline(steps=[('preprocessor', trf), ('classifier', model)])
        pipe.fit(X_train, y_train)
        y_pred = pipe.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"{name} Accuracy: {acc:.4f}")
        
        if acc > best_acc:
            best_acc = acc
            best_pipe = pipe
            
  
    joblib.dump(best_pipe, 'ipl_match_prediction_model.pkl')
    print("\nBest model saved successfully as ipl_match_prediction_model.pkl")

if __name__ == '__main__':
    run_ipl_pipeline()