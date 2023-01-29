import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np

MODEL_NAME = f"./EmotionAnalysisModel"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME).to(device)

def id2label(x):
    return model.config.id2label[x]

def inference(text):
    inputs = tokenizer(text, return_tensors="pt")
    model.eval()
    with torch.no_grad():
        outputs = model(
            inputs["input_ids"].to(device),
            inputs["attention_mask"].to(device),
        )

    y_preds = np.argmax(outputs.logits.to("cpu").detach().numpy().copy(), axis=1)
    y_dash = id2label(y_preds[0])
    return y_dash
