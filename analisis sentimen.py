
from textblob import TextBlob
import matplotlib.pyplot as plt

print("ANALISIS SENTIMEN")
print("===========================================\n")

tweets = [
    "I am very happy today",
    "This product is really bad",
    "The weather is just ordinary",
    "The store service is very friendly",
    "I hate long queues",
    "The movie is really good",
    "The food is delicious",
    "Too expensive for its quality",
    "Today is fun",
    "I am disappointed with this service",
    "The vacation was amazing",
    "I am tired and bored",
    "The product quality is very good",
    "Not satisfied with the result",
    "The performance is entertaining",
    "I am angry because of the delay",
    "This place is comfortable",
    "Bad service",
    "I am satisfied with this experience",
    "The weather is unpleasant",
    "My favorite food is available",
    "I am very disappointed",
    "This event is very fun",
    "The price is too high",
    "I am happy I could attend",
    "Bad experience today",
    "High-quality product",
    "Slow service",
    "I am happy to help",
    "Hot and boring weather",
    "This place is beautiful",
    "I am sad because of failure",
    "Fast and efficient service",
    "Product was damaged upon arrival",
    "Today is very enjoyable",
    "I am angry about this decision",
    "Delicious and fresh food",
    "I dont like this color",
    "Enjoyable vacation",
    "Disappointing service",
    "The event went smoothly",
    "I am tired after the trip",
    "The parking area is comfortable",
    "Low product quality",
    "I am happy to meet old friends",
    "Rainy weather makes me sad",
    "This store is very neat",
    "I am disappointed with the service",
    "The event is very boring",
    "My favorite product is available",
    "I am happy today"
]

positif = 0
negatif = 0
netral = 0


for tweet in tweets:
    analysis = TextBlob(tweet)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        positif += 1
    elif polarity < 0:
        negatif += 1
    else:
        netral += 1

total = positif + negatif + netral

print("Hasil Analisis Sentimen: ")
print(f"Positif: {positif} ({positif/total*100:.1f}%)")
print(f"Negatif: {negatif} ({negatif/total*100:.1f}%)")
print(f"Netral: {netral} ({netral/total*100:.1f}%)")


labels = ['Positif', 'Negatif', 'Netral']
sizes = [positif, negatif, netral]
colors = ['#4CAF50', '#F44336', '#FFC107']

plt.figure(figsize=(7,7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title("Persentase Sentimen (Manual)")
plt.show()
