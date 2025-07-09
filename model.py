from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)

# Load your trained weights
model.load_state_dict(torch.load("model/sentiment_model.pt", map_location='cpu'))
model.eval()

labels = ['Negative', 'Neutral', 'Positive']

def predict_sentiment(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        confidence, pred = torch.max(probs, dim=1)
        return labels[pred], confidence.item()
