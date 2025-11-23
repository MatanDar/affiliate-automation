# update_products.py
# רץ ב-GitHub Actions. מושך מוצרים (placeholder) ומעדכן CSV.
import csv
import os
import requests

# --- הגדרות ---
CSV_PATH = "products.csv"  # אם ה-CSV שלך במיקום אחר - שנה כאן לנתיב המדויק, לדוגמה "data/products.csv"
APP_KEY = os.getenv("ALI_APP_KEY")
APP_SECRET = os.getenv("ALI_APP_SECRET")

# --- פונקציות עזר ---
def get_existing_ids(path):
    ids = set()
    if not os.path.exists(path):
        return ids
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            ids.add(r.get("product_id", "").strip())
    return ids

def fetch_products_from_aliexpress():
    """
    דוגמה פשוטה - כאן תכנס קריאה אמיתית ל-AliExpress Affiliate API.
    עכשיו זה מחזיר דוגמת מוצרים לדמו.
    החליף את הפונקציה הזאת בלוגיקה של ה-API שלך.
    """
    # ---- דוגמת נתונים (מחק או החלף) ----
    return [
        {
            "product_id": "demo-123",
            "product_title": "Demo Product 123",
            "product_image": "https://via.placeholder.com/300",
            "promotion_link": "https://aliexpress.com/demo-affiliate-link-123"
        },
        {
            "product_id": "demo-124",
            "product_title": "Demo Product 124",
            "product_image": "https://via.placeholder.com/300",
            "promotion_link": "https://aliexpress.com/demo-affiliate-link-124"
        }
    ]

def append_new_products_to_csv(path, products, existing_ids):
    fieldnames = ["product_id", "title", "image", "affiliate_link"]
    file_exists = os.path.exists(path)
    # אם הקובץ לא קיים - נכתוב גם header
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        added = 0
        for p in products:
            pid = p.get("product_id", "").strip()
            if not pid or pid in existing_ids:
                continue
            writer.writerow({
                "product_id": pid,
                "title": p.get("product_title", ""),
                "image": p.get("product_image", ""),
                "affiliate_link": p.get("promotion_link", "")
            })
            added += 1
    return added

def main():
    existing = get_existing_ids(CSV_PATH)
    products = fetch_products_from_aliexpress()
    added = append_new_products_to_csv(CSV_PATH, products, existing)
    print(f"Existing IDs: {len(existing)}, Products fetched: {len(products)}, Added: {added}")

if __name__ == "__main__":
    main()
