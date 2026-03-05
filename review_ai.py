from textblob import TextBlob
"""
Game & Anime Review Sentiment Analyzer
Developed by Lim Junhan
This script uses Natural Language Processing (NLP) to analyze user reviews
and automatically categorize them as Positive, Negative, or Neutral.
"""

def analyze_sentiment(review_text):
    analysis = TextBlob(review_text)
    score = analysis.sentiment.polarity

    if score > 0.1:
        return "Positive Review 😊"
    elif score < -0.1:
        return "Negative Review 😠"
    else:
        return "Neutral Review 😐"


print("--- Game & Anime Review AI ---")
print("Type 'quit' to exit.")

# This creates an infinite loop so you can keep testing new sentences!
while True:
    user_input = input("\nEnter a review to analyze: ")

    if user_input.lower() == 'quit':
        print("Shutting down AI...")
        break

    result = analyze_sentiment(user_input)
    print(f"AI Verdict: {result}")