from transformers import AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("gpt2")

token_ids = tokenizer.encode("Hello World")
print("Tokens:   ", tokenizer.convert_ids_to_tokens(token_ids))
print("Token IDs:", token_ids)
