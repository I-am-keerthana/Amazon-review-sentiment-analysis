import os
import urllib.request
import zipfile

DATASET_URL = "https://snap.stanford.edu/data/finefoods.txt.gz"
OUTPUT_FILE = "sample_data/amazon_reviews_sample.csv"

def download_and_sample():
    os.makedirs("sample_data", exist_ok=True)

    if os.path.exists(OUTPUT_FILE):
        print(f"Sample data already exists at {OUTPUT_FILE}")
        return

    print("Generating sample review data for testing...")

    sample_reviews = [
        (5, "This product is absolutely amazing! Best purchase I have made in years."),
        (5, "Exceeded all my expectations. Will definitely buy again."),
        (4, "Really good quality. Minor packaging issue but product itself is great."),
        (4, "Works as described. Happy with the purchase overall."),
        (3, "It is okay. Nothing special but does the job."),
        (3, "Average product. Expected a bit more for the price."),
        (2, "Disappointed with the quality. Does not match the description."),
        (2, "Arrived damaged. Customer service was slow to respond."),
        (1, "Terrible product. Complete waste of money. Do not buy."),
        (1, "Stopped working after one week. Absolute rubbish."),
        (5, "Fantastic flavour and great value for money."),
        (4, "Very pleased with this. Would recommend to friends."),
        (3, "Decent enough but I have had better."),
        (2, "Not as advertised. Very misleading product images."),
        (1, "Worst purchase ever. Returning immediately."),
        (5, "Outstanding quality. Will be ordering again soon."),
        (4, "Good product, fast delivery, well packaged."),
        (3, "It is fine. Nothing remarkable to say about it."),
        (2, "Quality has gone downhill since last time I ordered."),
        (1, "Do not waste your money. Completely useless."),
    ]

    import csv
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Id", "Score", "Text"])
        for i, (score, text) in enumerate(sample_reviews * 5, start=1):
            writer.writerow([i, score, text])

    print(f"Sample data saved to {OUTPUT_FILE}")
    print(f"100 sample reviews ready. Run: streamlit run app.py")

if __name__ == "__main__":
    download_and_sample()
