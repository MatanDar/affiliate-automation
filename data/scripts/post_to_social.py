import csv
import json
import time
from pathlib import Path

def load_products():
    with open("data/products.csv", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_state():
    with open("data/state.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_state(state):
    with open("data/state.json", "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def post_to_facebook(product):
    print(f"📌 Posting to Facebook: {product['product_name']} -> {product['affiliate_link']}")
    time.sleep(2)

def post_to_youtube(product):
    print(f"🎥 Posting Short to YouTube: {product['product_name']} -> {product['affiliate_link']}")
    time.sleep(2)

def main():
    products = load_products()
    state = load_state()
    index = state.get("last_index_posted", 0)
    
    if index >= len(products):
        print("No more products to post!")
        return
    
    product = products[index]
    print("🚀 Auto posting product:", product["product_name"])
    
    post_to_facebook(product)
    post_to_youtube(product)
    
    state["last_index_posted"] = index + 1
    save_state(state)

if __name__ == "__main__":
    main()
