import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader
from torch.utils.data.dataset import Dataset
import numpy as np

# Загрузка предобученной модели BERT и токенизатора
model_name = 'bert-base-multilingual-cased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Загрузка данных из файла
class CustomDataset(Dataset):
    def __init__(self, file_path):
        self.data = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                self.data.append(line.strip())

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


# Функция предобработки данных для BERT
def preprocess_text(text):
    inputs = tokenizer(text, padding='max_length', truncation=True, max_length=128, return_tensors='pt')
    return inputs


# Классификация текста
def classify_text(text):
    inputs = preprocess_text(text)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1).squeeze().numpy()
    return probs  # Вероятности принадлежности к обоим классам для всего батча текстов


# Путь к файлу с данными
file_path = 'test.txt'

# Создание экземпляра Dataset и DataLoader
dataset = CustomDataset(file_path)
data_loader = DataLoader(dataset, batch_size=8, shuffle=False)
i = 0
# Классификация данных и вывод результатов
for batch_texts in data_loader:
    probs = classify_text(batch_texts)
    for prob in probs:
        i+=1
        print(i)
        print(f"Вероятность принадлежности к классу 'термины из категории беспилотных авиационных систем и их контекст': {prob[1]:.4f}")