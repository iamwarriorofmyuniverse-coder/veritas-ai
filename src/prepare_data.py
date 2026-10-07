import pandas as pd
from sklearn.model_selection import train_test_split

# Load fake news dataset (update path if needed)
fake_df = pd.read_csv('data/raw/Fake.csv')

# Load real news dataset (update path if needed)
real_df = pd.read_csv('data/raw/True.csv')

# Identify text column names in both datasets (adjust if different)
fake_text_col = 'text' if 'text' in fake_df.columns else 'content'
real_text_col = 'text' if 'text' in real_df.columns else 'content'

# Extract text column and assign label=1 for fake news
fake_news = fake_df[[fake_text_col]].rename(columns={fake_text_col: 'text'})
fake_news['label'] = 1

# Extract text column and assign label=0 for real news
real_news = real_df[[real_text_col]].rename(columns={real_text_col: 'text'})
real_news['label'] = 0

# Combine the datasets
combined_df = pd.concat([fake_news, real_news], ignore_index=True)

# Shuffle the combined dataset
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Split into train and validation sets (80-20 split)
train_df, val_df = train_test_split(combined_df, test_size=0.2, stratify=combined_df['label'], random_state=42)

# Save to CSV files for use in BERT fine-tuning
train_df.to_csv('data/train.csv', index=False)
val_df.to_csv('data/val.csv', index=False)

print(f"Training samples: {len(train_df)}")
print(f"Validation samples: {len(val_df)}")

print(f"Sample training data:\n{train_df.head()}")
