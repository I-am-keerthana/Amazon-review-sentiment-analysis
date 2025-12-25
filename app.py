import nltk
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from tqdm.notebook import tqdm
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
from nltk.sentiment import SentimentIntensityAnalyzer
#from tqdm notebook import tqdm
import pandas as pd
plt.style.use('ggplot')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('punkt_tab')
nltk.download('vader_lexicon')
data=pd.read_csv('C:\\Users\\vishn\\Documents\\keerthana jobs\\reviews\\Reviews.csv')
data=data.head(1000)
ax=data['Score'].value_counts().sort_index().plot(kind='bar',color='blue',title="counting review by score",figsize=(6,6))
ax.set_xlabel('Review Score')
#plt.show()
example=data['Text'][50]
#this is using the nltk library basic word tokenization and pos tagging
tokens=nltk.word_tokenize(example)
tokens[:10]
tagged=nltk.pos_tag(tokens)
#entities=nltk.chunk.ne_chunk(tagged)
#entities.pprint()
#this is using the vader sentiment analysis
sia=SentimentIntensityAnalyzer()
sentiment=sia.polarity_scores(example)
res={}
for i,row in tqdm(data.iterrows(),total=len(data)):
    text=row['Text']
    id=row['Id']
    res[id]=sia.polarity_scores(text)
vaders=pd.DataFrame(res).T
vaders=vaders.reset_index().rename(columns={'index':'Id'})
vaders=vaders.merge(data,how='left')
ax=sns.barplot(x='Score',y='compound',data=vaders)
ax.set_title("Average Compound Sentiment Score by Review Score")
#plt.show()
fig,axs=plt.subplots(1,3,figsize=(12,3))
axs=axs.flatten()
sns.barplot(data=vaders,x='Score',y='pos',ax=axs[0])
sns.barplot(data=vaders,x='Score',y='neu',ax=axs[1])
sns.barplot(data=vaders,x='Score',y='neg',ax=axs[2])
axs[0].set_title('Positive Sentiment by Review Score')
axs[1].set_title('Neutral Sentiment by Review Score')
axs[2].set_title('Negative Sentiment by Review Score') 
#plt.show()
#this is using the transformer model for sentiment analysis
#the model is trained usinga pretrainedmodel from cardiffnlp
#provided by huggingface
model=f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer=AutoTokenizer.from_pretrained(model)
pt_model=AutoModelForSequenceClassification.from_pretrained(model)
encoded_text = tokenizer(example, return_tensors='pt')
output = model(**encoded_text)
scores = output[0][0].detach().numpy()
scores = softmax(scores)
scores_dict = {
    'roberta_neg' : scores[0],
    'roberta_neu' : scores[1],
    'roberta_pos' : scores[2]
}
print(scores_dict)
#a horizontal bar plot for the roberta sentiment scores
labels = ["Positive", "Neutral", "Negative"]
values = [scores_dict['roberta_pos'], scores_dict['roberta_neu'], scores_dict['roberta_neg']]
plt.figure()
plt.barh(labels, values)
plt.xlim(0, 1)
plt.title("Sentiment Scores")
plt.show()
