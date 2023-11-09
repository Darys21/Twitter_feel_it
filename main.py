import tweepy
from textblob import TextBlob
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# API credentials
API_KEY = "TwXwS1INoTZd5T5TXXG7sI3RQ"
API_SECRET_KEY = "CkD8byGjP24ruqIWMvYmXx6d61hixuXl45mxCfA9LlGpcOavNG"
ACCESS_TOKEN = "1612085306567671809-c82PJJnI11wSu9K4JjIdeBUqZQzz8v"
ACCESS_TOKEN_SECRET = "gyQeKrxX7lEbtiKLkx9oP63LQqXbnFVHrCndoLZf0sM8Y"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Collecte des données
search_query = "Gabon"
tweets = []
for tweet in tweepy.Cursor(api.search_tweets, q=search_query, tweet_mode="extended").items(100):
    tweets.append(tweet.full_text)

# Prétraitement des données
preprocessed_tweets = []
for tweet in tweets:
    # Appliquer des traitements de prétraitement au tweet (ex: suppression des caractères spéciaux, normalisation, etc.)
    preprocessed_tweets.append(tweet)

# Extraction de fonctionnalités
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(preprocessed_tweets)

# Étiquettes de classification de sentiment (exemple simplifié)
y = [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]  # 0: sentiment négatif, 1: sentiment positif

# Séparation des données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Choix et entraînement du modèle
model = LogisticRegression()
model.fit(X_train, y_train)

# Évaluation du modèle
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Utilisation du modèle pour prédire le sentiment de nouveaux tweets
new_tweets = ["I love Gabon!", "Gabon is a beautiful country"]
new_tweets_preprocessed = []
for tweet in new_tweets:
    # Appliquer le même prétraitement aux nouveaux tweets
    new_tweets_preprocessed.append(tweet)

X_new = vectorizer.transform(new_tweets_preprocessed)
predictions = model.predict(X_new)

for tweet, prediction in zip(new_tweets, predictions):
    print("Tweet:", tweet)
    if prediction == 0:
        print("Sentiment: Negative")
    else:
        print("Sentiment: Positive")