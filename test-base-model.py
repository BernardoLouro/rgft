import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

base_model_name = "unsloth/mistral-7b-bnb-4bit" #path/to/your/model/or/name/on/hub"

model = AutoModelForCausalLM.from_pretrained(
    base_model_name,
    device_map='auto',
    load_in_8bit=True,
)

model.bfloat16()

tokenizer = AutoTokenizer.from_pretrained(base_model_name)

input_text = "input_given"

input_ids = tokenizer(input_text, return_tensors="pt").input_ids

outputs = model.generate(input_ids, max_new_tokens=1000)

print(tokenizer.decode(outputs[0]))