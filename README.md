# HW_04: Amy's Reddit Bots
 
 
**Below is information on my Reddit bots that generated 500+ comments and replies on different Reddit posts.**

---

## Politics & Media
![Political Debate Image](https://github.com/kimsngmin00/HW_04/blob/main/obama_and_trump.jpeg)

With python, I randomly generated 500+ comments that contain *positive* messages about Obama and Biden and *negative* messages about Trump. These comments varied from top level comments, subreddit posts, and replies to other existing comments. Python also allowed me to *upvote* positive posts about Obama and Biden and *downvote* comments about Trump. This experience made me realize how disruptive bots can be online and weary of the fact that online ratings or votes can be easily controlled with programming.


## Favorite Thread

My favorite thread involving my **akcs40bot** can be found [here](https://www.reddit.com/r/Thoughts/comments/r47usg/comment/hmfjsrj/?utm_source=share&utm_medium=web2x&context=3). It was funny to see the original poster responding to my bot who seemed confused but still continuing their "conversation" with my bot. Also, as you can see if you scroll down the thread, it was interesting to see my bot interacting with my classmates' and the original poster responding to those. While reading this comment thread was a fun and interesting experience, it also made me realize that the nature of bots is to respond to any and all comments including the ones critical of the bots and therefore can easily overwhelm the normal Reddit users.

![Reddit Bot Comment - Image](https://github.com/kimsngmin00/HW_04/blob/main/best_Reddit_comments.jpeg)


## Bot Counter

Below is the output of running the `bot_counter.py` for the **akcs40bot**:

```
len(comments)= 692
len(top_level_comments)= 184
len(replies)= 508
len(valid_top_level_comments)= 38
len(not_self_replies)= 507
len(valid_replies)= 487
========================================
valid_comments= 525
========================================
```


## Grade

| Task                                                                          | Grade       |
| :---                                                                          |    :----:   |
| Complete all tasks in `bot.py` file                                           | 18          |
| GitHub repo                                                                   | 2           |
| 1. Getting at least 100 valid comments posted                                 | 2           |
| 2. Getting at least 500 valid comments posted                                 | 2           |
| 4. Make your bot create new submission posts instead of just new comments (see `posts.py`)                                                                            | 2           |
| 7. Have your bot upvote or downvote any comment or submission (see `upvote.py`)| 2           |
| Using Markovify to generate comments (included in `markovify.py`)             | 5           |
| **Total**                                                                     | 33          |


## Extra Credit Results
### Post Submissions
Below is the end part of the output of running the `posts.py` for the **akcs40bot**:

```
link_post_count= 96
total_post_count= 96
link_post_count= 97
total_post_count= 97
link_post_count= 98
total_post_count= 98
link_post_count= 99
total_post_count= 99
link_post_count= 100
total_post_count= 100
link_post_count= 101
total_post_count= 101
link_post_count= 102
total_post_count= 102
link_post_count= 103
total_post_count= 103
^CTraceback (most recent call last):
  File "/Users/kimseungmin/Documents/GitHub/HW_04/posts.py", line 25, in <module>
    time.sleep(600)
KeyboardInterrupt
```



### Upvote/Downvote
Below is the end part of the output of running the `upvote.py` for the **akcs40bot**:

```
votes_for_submissions= 109
votes_for_comments= 496
votes_for_submissions= 109
votes_for_comments= 497
votes_for_submissions= 109
votes_for_comments= 498
votes_for_submissions= 109
votes_for_comments= 499
votes_for_submissions= 109
votes_for_comments= 500
votes_for_submissions= 109
votes_for_comments= 501
votes_for_submissions= 109
votes_for_comments= 502
votes_for_submissions= 109
votes_for_comments= 503
votes_for_submissions= 109
votes_for_comments= 504
^CTraceback (most recent call last):
  File "/Users/kimseungmin/Documents/GitHub/HW_04/upvote.py", line 44, in <module>
    time.sleep(600)
KeyboardInterrupt
```


---
**NOTE:** [here](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_04) is the link to the course project.
