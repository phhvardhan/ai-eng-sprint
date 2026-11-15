import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
PRICE_PER_MILLION = 0.0004

samples = {
    "short_english": "the quick brown fox jumps over the lazy dog",
    "long_english": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "python_code": "def add(a,b):\n    return a + b",
    "telugu": "నేను రేపు ఆఫీసుకు వెళ్తాను",
    "product_code": "PROD-SKU-7842X",
}

for name, text in samples.items():
    tokens = enc.encode(text)
    words = len(text.split())
    cost = len(tokens)/1_000_000 * PRICE_PER_MILLION
    print(f"{name}: {len(tokens)} tokens, {words} words,"
          f" {len(tokens)/words:,.2f} tokens/word, ${cost:.8f}")
