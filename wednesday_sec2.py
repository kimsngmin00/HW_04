import praw
reddit = praw.Reddit('bot')

url = "https://old.reddit.com/r/funny/comments/qqvl9q/gingerbread_fun/"
submission = reddit.submission(url=url)

for top_level_comment in submission.comments:
#ask for permission strategy
    #if type(top_level_comment) == praw.models.reddit.comment.Comment:
        #print(top_level_comment.body)


#ask for forgiveness strategy
    #try:
        #print(top_level_comment.body)
    #except AttributeError:
        #pass


    print('type(top_level_comment)=', type(top_level_comment))