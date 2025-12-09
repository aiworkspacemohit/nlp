# model_def.py

import torch
from torch import nn
from transformers import BertModel

class MultiTaskBERT(nn.Module):
    def __init__(self, n_cat, n_prio):
        super().__init__()
        self.bert = BertModel.from_pretrained("bert-base-uncased")
        self.dropout = nn.Dropout(0.2)

        hidden_size = self.bert.config.hidden_size  # 768

        self.category_head = nn.Linear(hidden_size, n_cat)
        self.priority_head = nn.Linear(hidden_size, n_prio)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )

        cls_output = outputs.last_hidden_state[:, 0, :]
        cls_output = self.dropout(cls_output)

        category_logits = self.category_head(cls_output)
        priority_logits = self.priority_head(cls_output)

        return category_logits, priority_logits
