from gnews import GNews
import pandas as pd

def fetch_real_news_gnews(language='en', max_results=100):
    google_news = GNews(language=language, max_results=max_results)
    articles = google_news.get_news('latest')

    real_news = []
    for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')
        content = f"{title} {description}".strip()
        if content:
            real_news.append({'content': content, 'label': 0})

    return pd.DataFrame(real_news)

if __name__ == "__main__":
    df_real_news = fetch_real_news_gnews()
    df_real_news.to_csv('data/raw/RealNews_API.csv', index=False)
    print(f"Saved {len(df_real_news)} real news articles to data/raw/RealNews_API.csv")
