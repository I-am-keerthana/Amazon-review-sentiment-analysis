# Amazon review sentiment analysis

> NLP pipeline that analyzes 100,000+ Amazon product reviews using two
> approaches — NLTK VADER and a RoBERTa transformer model — and compares
> their accuracy on real-world review data.

---

## 🧩 Problem it solves

Customer reviews contain a goldmine of product feedback, but manually reading
thousands of them is impractical. This project automates sentiment
classification at scale, compares a lightweight rule-based model (VADER) against
a deep learning transformer (RoBERTa), and surfaces which approach performs
better on real Amazon data — giving businesses a tool to monitor product
perception instantly.

---

## 🛠️ Technologies used

| Tool | Purpose |
|---|---|
| Python | Core language |
| NLTK (VADER) | Rule-based sentiment scoring |
| HuggingFace Transformers | RoBERTa pre-trained model |
| Pandas | Data loading and preprocessing |
| Matplotlib / Seaborn | Sentiment distribution charts |
| Streamlit | Interactive sentiment meter UI |

---

## ⚙️ Installation & setup

**1. Clone the repo**
```bash
git clone https://github.com/I-am-keerthana/Amazon-review-sentiment-analysis.git
cd Amazon-review-sentiment-analysis
```

**2. Install dependencies**
```bash
pip install nltk transformers pandas matplotlib seaborn streamlit torch
```

**3. Download NLTK data**
```python
import nltk
nltk.download('vader_lexicon')
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## 📊 Key findings

- **VADER** is fast and works well for short, informal reviews with clear
  positive/negative language
- **RoBERTa** significantly outperforms VADER on sarcastic, nuanced, or
  mixed-sentiment reviews
- Approximately **65% positive**, **20% neutral**, and **15% negative** reviews
  in the 100k dataset
- Reviews with 1-star ratings occasionally score as "positive" in VADER —
  a key failure case that RoBERTa handles correctly

---

## 📁 Dataset

This project uses the
[Amazon Product Reviews dataset](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
(publicly available on Kaggle). Download and place it in the project root as
`reviews.csv` before running.

---

## 💡 How it works

```
Raw reviews → Text cleaning → VADER scoring → RoBERTa scoring
           → Side-by-side comparison → Sentiment meter visualization
```
