from praw.models import MoreComments
import login,time
reddit=login.reddit

log=open("log.txt","w+")
info="""
\n
\n
\n

^(ben bot | [github](https://www.github.com/kaansenol5/OwoYapar2023)) \n
\n
^(owofier geri dönecek demiştim...)
"""
def reply(content,info):
    new=content.replace("r","w").replace("l","w").replace("v","w").replace("R","W").replace("L","W") + info
    return new

subreddit=reddit.subreddit("kopyamakarna")



while True:
    for submission in subreddit.new():
        toReply=True
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
            if not submission.is_self:
                toReply=False
            if top_level_comment.author=="OwoYapar2023" or submission.selftext=='':
                toReply=False
                print("PASSED "+ submission.url)
                log.write("PASSED "+ submission.url+"\n")
        if toReply:
            try:
                new=reply(submission.selftext, info)
                submission.reply(new)
            except Exception as e:
                log.write("ERROR: " + str(e) + "   on submission " + submission.url)
            print("REPLIED "+ submission.url)
            log.write("REPLIED "+submission.url+"\n")
            try:
                time.sleep(60)
            except KeyboardInterrupt:
                log.close()

                exit()
