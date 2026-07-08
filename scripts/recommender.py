
import pandas as pd

def get_recommendations(risk_appetite):
    file_path = r'C:\Users\Shiva\Downloads\bluestock\data\raw\07_scheme_performance.csv'
    df = pd.read_csv(file_path)
    filtered_df = df[df['risk_grade'] == risk_appetite]
    recommendations = filtered_df.sort_values(by='sharpe_ratio', ascending=False).head(3)
    return recommendations[['scheme_name', 'sharpe_ratio']]

if __name__ == "__main__":
    user_risk = input("Enter Risk Appetite (Low/Moderate/High): ")
    print(f"\nTop 3 funds for {user_risk} risk:")
    print(get_recommendations(user_risk))
