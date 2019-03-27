import pickle
import time
import login
reddit=login.reddit


subreddit=reddit.subreddit("kopyamakarna")
for submission in subreddit.new():
    for comment in submission.get_comments(limit=None):
        if comment.author=="OwoYapar2023":
            pass
        else:
            newtxt=submission.content.replace("r","w").replace("l","w")
            submission.reply(newtxt)
