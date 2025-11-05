def split_thread(text):
    tweets = []
    current = ''
    for word in text.split():
        if len(current) + len(word) + 1 > 280:
            tweets.append(current.strip())
            current = ''
        current += word + ' '
    if current:
        tweets.append(current.strip())
    return tweets
