import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv  # Load environment variables

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Get MongoDB credentials securely
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

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
    df = pd.read_csv("dataset.csv", on_bad_lines="skip")  # Skips corrupted lines
    print(f"✅ CSV Loaded Successfully! Total Rows: {len(df)}")
except Exception as e:
    print(f"❌ Error Loading CSV: {e}")
    exit()

# ✅ Check & Clean Data (Remove Empty Rows)
df.dropna(inplace=True)  # Remove rows with missing values

# ✅ Convert DataFrame to Dictionary
data_dict = df.to_dict(orient="records")

# ✅ Insert into MongoDB with Error Handling
try:
    if data_dict:
        collection.insert_many(data_dict)
        print("✅ CSV data successfully inserted into MongoDB!")
    else:
        print("⚠ No valid data found to insert.")
except Exception as e:
    print(f"❌ Error Inserting Data: {e}")
