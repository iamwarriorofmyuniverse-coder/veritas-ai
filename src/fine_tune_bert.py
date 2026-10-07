from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import torch

# Load CSV dataset
data_files = {"train": "data/train.csv", "validation": "data/val.csv"}
dataset = load_dataset('csv', data_files=data_files)

# Load pretrained BERT tokenizer and model for sequence classification
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Tokenize function - preprocess text to input IDs and masks
def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True, max_length=512)

# Map tokenization across datasets in batches for speed
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Tell Hugging Face which columns are inputs and labels
tokenized_datasets.set_format(type='torch', columns=['input_ids', 'attention_mask', 'label'])

# Training arguments: adjust epochs/batch size accordingly
training_args = TrainingArguments(
    output_dir='./results',
    eval_strategy="epoch",            # use "eval_strategy", not "evaluation_strategy"
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    logging_dir='./logs',
    logging_steps=500,
)


# Define compute metrics function (optional but recommended)
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = torch.argmax(torch.tensor(logits), axis=1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average='binary')
    acc = accuracy_score(labels, predictions)
    return {'accuracy': acc, 'f1': f1, 'precision': precision, 'recall': recall}

# Initialize Trainer object
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    compute_metrics=compute_metrics,
)

# Start training
trainer.train()

# Save fine-tuned model and tokenizer
model.save_pretrained("models/bert_fake_news")
tokenizer.save_pretrained("models/bert_fake_news")

print("Training complete and model saved!")
