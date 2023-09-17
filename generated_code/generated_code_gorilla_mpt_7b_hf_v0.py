from transformers import T5Tokenizer, T5ForConditionalGeneration
tokenizer = T5Tokenizer.from_pretrained('google/flan-t5-xl')
model = T5ForConditionalGeneration.from_pretrained('google/flan-t5-xl')
input_text = "translate I love you from English to Bulgarian:"
input_ids = tokenizer(input_text, return_tensors="pt").input_ids
outputs = model.generate(input_ids)
translated_text = tokenizer.decode(outputs[0])
