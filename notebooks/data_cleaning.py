import os
import pandas as pd

def clean_sales_data():
    # Base path script ki location ke hisab se setup karna
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    raw_data_path = os.path.join(base_dir, 'data', 'raw', 'raw_sales_data.csv')
    processed_dir = os.path.join(base_dir, 'data', 'processed')
    processed_data_path = os.path.join(processed_dir, 'cleaned_sales_data.csv')
    
    print("--- Data Cleaning Process Shuru Ho Raha Hai ---")
    
    # Baaki ka code bilkul same rahega...
    if not os.path.exists(raw_data_path):
        print(f"Error: Raw file nahi mili.\nDhoondha gaya path: {raw_data_path}\nKripya check karein file isi jagah par hai ya nahi.")
        return
        
    df = pd.read_csv(raw_data_path)
    print(f"Original Data Shape: {df.shape} rows aur {df.shape[1]} columns.")
    
    # 3. Duplicates handle karna
    duplicate_count = df.duplicated().sum()
    print(f"Total Duplicates mile: {duplicate_count}")
    if duplicate_count > 0:
        df = df.drop_duplicates(keep='first')
        print("Success: Duplicates ko remove kar diya gaya hai.")
        
    # 4. Null Values handle karna
    print("\nNull values check:")
    print(df.isnull().sum())
    
    if 'Region' in df.columns:
        df['Region'] = df['Region'].fillna('Unknown')
        
    if 'Profit' in df.columns:
        df['Profit'] = df['Profit'].fillna(0.00)
        
    print("Success: Null values ko successfully handle kar liya gaya hai.")
    
    # 5. Date Features ready karna
    if 'Order_Date' in df.columns:
        df['Order_Date'] = pd.to_datetime(df['Order_Date'])
        df['Year'] = df['Order_Date'].dt.year
        df['Quarter'] = 'Q' + df['Order_Date'].dt.quarter.astype(str)
        df['Month'] = df['Order_Date'].dt.strftime('%B')
    
    # 6. Cleaned data ko save karna
    os.makedirs(processed_dir, exist_ok=True)
    df.to_csv(processed_data_path, index=False)
    
    print("\n--- Cleaning Complete! ---")
    print(f"Cleaned Data Shape: {df.shape}")
    print(f"File yahan save ho gayi hai: {processed_data_path}")

if __name__ == "__main__":
    clean_sales_data()