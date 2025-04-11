import os
import pandas as pd
from pymongo import MongoClient

# ✅ Hardcoded MongoDB credentials
MONGO_URI = "mongodb+srv://caniketbawankar:aCuMbMgFzhqx3LEf@gift-recommendation.dcta7.mongodb.net/flask_db?retryWrites=false&w=majority&tls=true"
DATABASE_NAME = "flask_db"
COLLECTION_NAME = "Database"

# ✅ Connect to MongoDB
try:
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    print("✅ Connected to MongoDB successfully!")
except Exception as e:
    print(f"❌ MongoDB Connection Error: {e}")
    exit()

# ✅ Load CSV file safely
try:
    df = pd.read_csv("Assignment.csv", on_bad_lines="skip")
    print(f"✅ CSV Loaded Successfully! Total Rows: {len(df)}")
except Exception as e:
    print(f"❌ Error Loading CSV: {e}")
    exit()

# ✅ Clean Data (Remove Empty Rows)
df.dropna(inplace=True)
print(f"✅ Cleaned Data. Rows after dropna: {len(df)}")

# ✅ Convert to dictionary
data_dict = df.to_dict(orient="records")

# ✅ Insert data
try:
    if data_dict:
        collection.insert_many(data_dict)
        print("✅ CSV data successfully inserted into MongoDB!")
    else:
        print("⚠ No valid data found to insert.")
except Exception as e:
    print(f"❌ Error Inserting Data: {e}")
