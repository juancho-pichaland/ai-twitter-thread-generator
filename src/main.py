from src.services.twitter_service import TwitterService
from src.services.openai_service import OpenAIService
from src.utils.text_utils import split_thread
from src.utils.sheet_utils import read_topics

def main():
    print("🤖 Twitter AI Bot iniciado...")

    topics = read_topics()
    for topic in topics:
        print(f"🧠 Generando hilo sobre: {topic}")
        ai = OpenAIService()
        thread = ai.create_thread(topic)
        tweets = split_thread(thread)
        
        twitter = TwitterService()
        twitter.post_thread(tweets)
        print(f"✅ Hilo publicado correctamente sobre: {topic}")

if __name__ == "__main__":
    main()
