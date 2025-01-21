import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

def read_excel(file_path):
    return pd.read_excel(file_path)

def filter_data_analyst_candidates(df):
    # Filter candidates with Data Analysis skills
    candidates = df[df['Skill'].str.contains('Data Analysis')]
    # Include only relevant columns
    candidates = candidates[['Name', 'Mobile Number', 'Skill', 'Age']]
    return candidates.head(5)

def save_to_excel(df):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"top_data_analyst_candidates_{timestamp}.xlsx"
    df.to_excel(filename, index=False)
    return filename

def visualize_data(df, chart_type):
    top_candidates = filter_data_analyst_candidates(df)
    if chart_type == 'pie':
        top_candidates['Skill'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Top Candidates Skills Distribution')
        plt.ylabel('')
    elif chart_type == 'bar':
        skill_levels = {'Beginner': 1, 'Intermediate': 2, 'Advanced': 3, 'Expert': 4}
        top_candidates['Skill Level'] = top_candidates['Skill'].apply(lambda x: skill_levels.get(x.split(' - ')[1], 0))
        top_candidates.groupby('Name')['Skill Level'].sum().plot(kind='bar', title='Candidates Skill Levels')
        plt.xlabel('Candidate Name')
        plt.ylabel('Total Skill Level')
    plt.show()

def main():
    print("Welcome to the Data Analyst Candidate Selection Tool\n")
    file_path = input("Enter the path to the Excel file: ")
    df = read_excel(file_path)

    candidates = filter_data_analyst_candidates(df)
    print("\nTop 5 Data Analyst Candidates:")
    print(candidates)

    saved_file = save_to_excel(candidates)
    print(f"Candidates saved to {saved_file}")
    
    vis_choice = input("Do you want to visualize the data? (none/pie/bar): ")
    if vis_choice.lower() in ['pie', 'bar']:
        visualize_data(df, vis_choice)

if __name__ == "__main__":
    main()
