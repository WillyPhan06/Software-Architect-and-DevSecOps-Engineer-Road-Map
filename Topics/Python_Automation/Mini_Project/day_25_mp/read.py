import praw

YOUR_CLIENT_ID=""
YOUR_CLIENT_SECRET=""
YOUR_REDDIT_USERNAME=""

reddit = praw.Reddit(
    client_id=YOUR_CLIENT_ID,
    client_secret=YOUR_CLIENT_SECRET,
    user_agent=f"personal use script by {YOUR_REDDIT_USERNAME}",
)

print("Read-only:", reddit.read_only)  # True

for submission in reddit.subreddit("onepunchman").hot(limit=5):
    print(submission.title, "-", submission.score, "upvotes")
