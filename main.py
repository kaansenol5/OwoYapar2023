from praw.models import MoreComments
import login,time
reddit=login.reddit

info="""
\n
\n
\n

^(ben bot| [kod](https://www.github.com/kaansenol5/OwoYapar2023))
"""
def reply(content,info):
    new=content.replace("r","w").replace("l","w").replace("v","w")+ info
    return new

subreddit=reddit.subreddit("kopyamakarna")
for submission in subreddit.new():
    toReply=True
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        if top_level_comment.author=="OwoYapar2023":
            toReply=False
            print("PASSED "+ submission.url)
    if toReply:
        new=reply(submission.selftext, info)
        submission.reply(new)
        print("REPLIED "+ submission.url)
        time.sleep(60)