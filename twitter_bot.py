import os
import time
import tweepy
import openai
import schedule
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Twitter API Authentication
client = tweepy.Client(
    consumer_key=os.getenv('TWITTER_API_KEY'),
    consumer_secret=os.getenv('TWITTER_API_SECRET'),
    access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
    access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
)

# OpenAI Authentication
openai.api_key = os.getenv('OPENAI_API_KEY')

class TwitterBot:
    def __init__(self):
        self.client = client
        self.conversation_history = []
        
    def generate_response(self, tweet_text, context=""):
        """Generate a human-like response using GPT"""
        try:
            prompt = f"""Context: You are responding as the account owner. 
            Previous context: {context}
            Tweet to respond to: {tweet_text}
            Generate a natural, engaging response in under 280 characters."""
            
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": prompt}],
                max_tokens=100,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating response: {e}")
            return None

    def handle_mentions(self):
        """Handle new mentions and respond appropriately"""
        try:
            # Get recent mentions
            mentions = self.client.get_users_mentions(
                self.client.get_me().data.id,
                max_results=10
            )
            
            if not mentions.data:
                return
            
            for mention in mentions.data:
                # Check if we've already responded
                if mention.id in self.conversation_history:
                    continue
                
                # Generate and post response
                response = self.generate_response(mention.text)
                if response:
                    self.client.create_tweet(
                        text=response,
                        in_reply_to_tweet_id=mention.id
                    )
                    self.conversation_history.append(mention.id)
                    time.sleep(30)  # Rate limiting
                
        except Exception as e:
            print(f"Error handling mentions: {e}")

    def scan_timeline(self):
        """Scan timeline for interesting tweets to engage with"""
        try:
            timeline = self.client.get_home_timeline(max_results=10)
            
            for tweet in timeline.data:
                if tweet.id in self.conversation_history:
                    continue
                    
                # Decide whether to engage (you can customize this logic)
                if self.should_engage(tweet):
                    response = self.generate_response(tweet.text)
                    if response:
                        self.client.create_tweet(
                            text=response,
                            in_reply_to_tweet_id=tweet.id
                        )
                        self.conversation_history.append(tweet.id)
                        time.sleep(30)  # Rate limiting
                        
        except Exception as e:
            print(f"Error scanning timeline: {e}")

    def should_engage(self, tweet):
        """Decision logic for engaging with tweets"""
        # Add your custom logic here
        # For example: check tweet popularity, content relevance, etc.
        return True  # Placeholder

def main():
    bot = TwitterBot()
    
    # Schedule regular checks
    schedule.every(15).minutes.do(bot.handle_mentions)
    schedule.every(30).minutes.do(bot.scan_timeline)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main() 