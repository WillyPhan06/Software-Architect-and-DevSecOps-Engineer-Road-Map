import praw
import csv
from read import YOUR_CLIENT_ID, YOUR_CLIENT_SECRET, YOUR_REDDIT_USERNAME

# Initialize Reddit client
reddit = praw.Reddit(
    client_id=YOUR_CLIENT_ID,
    client_secret=YOUR_CLIENT_SECRET,
    user_agent=f"personal use script by {YOUR_REDDIT_USERNAME}",
)

print("Read-only:", reddit.read_only)  # Should print True

# Open a CSV file for writing
with open("onepunchman_hot.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Score", "URL"])  # header row

    # Loop through the top 5 hot posts
    for submission in reddit.subreddit("onepunchman").hot(limit=5):
        writer.writerow([submission.title, submission.score, submission.url])
        print(f"Saved: {submission.title}")

print("✅ Data saved to onepunchman_hot.csv successfully!")
