# model_loader.py

import torch
import pickle
from transformers import BertTokenizer

from model_def import MultiTaskBERT
from technician_assignment import assign_technician

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Load label encoders
cat_encoder = pickle.load(open("category_encoder.pkl", "rb"))
prio_encoder = pickle.load(open("priority_encoder.pkl", "rb"))

# Load trained multi-task model
model = MultiTaskBERT(
    n_cat=len(cat_encoder.classes_),
    n_prio=len(prio_encoder.classes_)
)
model.load_state_dict(torch.load("multitask_bert_ticket.pt", map_location=device))
model.to(device)
model.eval()


def predict_ticket(title: str, description: str):
    text = title + " - " + description

    encoding = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=64,
        return_tensors="pt"
    )

    input_ids = encoding["input_ids"].to(device)
    attention_mask = encoding["attention_mask"].to(device)

    with torch.no_grad():
        cat_logits, prio_logits = model(input_ids, attention_mask)

    cat_id = cat_logits.argmax(dim=1).item()
    prio_id = prio_logits.argmax(dim=1).item()

    return {
        "category": cat_encoder.inverse_transform([cat_id])[0],
        "priority": prio_encoder.inverse_transform([prio_id])[0],
    }


def classify_and_assign(title: str, description: str):
    prediction = predict_ticket(title, description)
    category = prediction["category"]
    priority = prediction["priority"]

    assignment = assign_technician(category, priority)

    return {
        "category": category,
        "priority": priority,
        "assign_to_team": assignment["team"],
        "assigned_technician": assignment["technician"]
    }
