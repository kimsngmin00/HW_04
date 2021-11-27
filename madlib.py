import praw
import time
import random

reddit = praw.Reddit('bot', user_agent='cs40')

'''
This lab has three tasks.

TASK 1:
Implement the `generate_comment` function below.

TASK 2:
Redefine the `madlibs` and `replacements` variables so that the generated comments are what you want your reddit bot to say.
You must have at least 6 different madlibs.
Each madlib should be 2-5 sentences long and have at least 5 [REPLACEMENT] [WORDS].

TASK 3:
Use your `generate_comment` function to post at least 100 messages to the `Practice posting messages here :)` submission, located at:
https://old.reddit.com/r/BotTown/comments/qr05je/practice_posting_messages_here/
You should have at least 10 top level comments and at least 10 replies to comments (but it's okay if they're all replies to the same comment).

SUBMISSION:
Upload your bot's name and your `madlib.py` file to sakai.
'''



madlibs = [
    "[PYTHON] is a [GREAT] [TOOL].  It [CAN_DO] [LOTS] of [STUFF]. [EVERYONE] [SHOULD] [LEARN] [PYTHON] and [BECOME] a [PROGRAMMER].",
    "[COOKING] is a [GREAT] [HOBBY]. [EVERYONE] [CAN] [COOK]! [SHARING] [FOOD] also [FEELS] [GREAT]. I [LOVE] [FOOD].",
    "[SOUTH_KOREA] is a [GREAT] [COUNTRY]. Their [FOOD] is [DIVERSE] and [GOOD]. My [FAMILY] [WENT] [LAST_YEAR]. I [WANT] to [VISIT] soon.",
    "[CMC] is a [GREAT] [SCHOOL]. It has a [BEAUTIFUL] [CAMPUS] and [GREAT] [STUDENTS]. My [BROTHER] also [WENT_TO] [CMC]. I [LOVE] my [CMC] [FRIENDS].",
    "[SLEEP] is [VERY] [IMPORTANT]. [EVERYONE] should [HAVE] a [HEALTHY] [SLEEP_SCHEDULE]. [TEA] or [MEDITATION] always help. Keep [YOURSELF] well [RESTED].",
    "I [LOVE] [DOGS]. They are [VERY] [CUTE] and [SMART]. [ALSO], they are [VERY] [LOYAL].",
    "I [LOVE] [MUSIC]. [GOOD] [SONGS] make me [HAPPY]. [MUSIC] also helps me [WORK]. I also [LOVE] [SINGING]. My favorite [ARTIST] is [BRUNO_MARS]."
    ]

replacements = {
    'PYTHON' : ['Python', 'Programming', 'Coding'],
    'GREAT' : ['great', 'awesome', 'amazing', 'wonderful', 'fantastic'],
    'TOOL' : ['tool', 'skill'],
    'CAN_DO' : ['can do', 'is able to do', 'accomplishes', 'enables me to do', 'helps me do'],
    'LOTS'  : ['lots', 'a whole lot', 'ridiculous amounts'],
    'STUFF' : ['stuff', 'things', 'fun things'],
    'SHOULD' : ['should', 'must', 'need to'],
    'BECOME' : ['become', 'turn into', 'try to be'],
    'PROGRAMMER' : ['programmer', 'developer', 'pythonista', 'software engineer'],
    'LEARN' : ['learn', 'master', 'study'],
    'COOKING' : ['Cooking', 'Baking', 'Making food'],
    'HOBBY' : ['hobby', 'fun', 'skill'],
    'EVERYONE' : ['Everyone', 'Anyone', 'All people'],
    'CAN' : ['can', 'is able to', 'should', 'can already'],
    'COOK'  : ['cook', 'bake', 'chef it up'],
    'SHARING' : ['Sharing', 'eating', 'smelling'],
    'FOOD' : ['food', 'meals', 'snacks', 'cuisine'],
    'FEELS' : ['feels', 'makes you feel', 'lets you feel'],
    'SOUTH_KOREA' : ['South Korea', 'Japan', 'Italy', 'France'],
    'COUNTRY' : ['country', 'nation', 'place'],
    'DIVERSE' : ['diverse', 'diversified', 'varied'],
    'FAMILY' : ['family', 'friends', 'sister'],
    'WENT' : ['went', 'visited', 'traveled there'],
    'LAST_YEAR' : ['last year', 'this summer', 'last winter'],
    'WANT' : ['want', 'hope', 'wish'],
    'VISIT' : ['visit', 'go', 'travel'],
    'CMC' : ['CMC', 'Claremont McKenna College', 'Pomona College', 'Scripps College', 'Pitzer College', 'Harvey Mudd College'],
    'SCHOOL' : ['school', 'college', 'liberal arts college'],
    'BEAUTIFUL' : ['beautiful', 'pretty', 'fascinating'],
    'CAMPUS' : ['campus', 'school area', 'landscape'],
    'STUDENTS'  : ['students', 'faculty', 'staff'],
    'BROTHER' : ['brother', 'sister', 'mom', 'dad'],
    'WENT_TO' : ['went to', 'studied at', 'graduated'],
    'LOVE' : ['love', 'adore', 'really like', 'like'],
    'FRIENDS' : ['friends', 'peers', 'classmates', 'professors'],
    'SLEEP' : ['Sleep', 'Sleeping', 'Sleep schedule'],
    'VERY' : ['very', 'really', 'extremely', 'greatly', 'so'],
    'IMPORTANT' : ['important', 'crucial', 'essential'],
    'HAVE' : ['have', 'maintain', 'develop', 'start'],
    'HEALTHY'  : ['healthy', 'regular', 'good', 'nice'],
    'SLEEP_SCHEDULE' : ['sleep schedule', 'sleep pattern', 'sleeping pattern'],
    'TEA' : ['Tea', 'Warm tea', 'Warm milk', 'Books'],
    'MEDITATION' : ['meditation', 'listening to music', 'ASMR videos'],
    'YOURSELF' : ['yourself', 'your friends', 'you body', 'your family'],
    'RESTED' : ['rested', 'slept'],
    'DOGS' : ['dogs', 'cats', 'birds', 'rabbits'],
    'CUTE' : ['cute', 'lovely', 'adorable'],
    'SMART' : ['smart', 'intelligent', 'bright', 'clever'],
    'ALSO' : ['Also', 'Plus', 'Moreover', 'In addition'],
    'LOYAL'  : ['loyal', 'trustworthy', 'trusty', 'nice'],
    'MUSIC' : ['music', 'melodies', 'good songs', 'good singers'],
    'GOOD' : ['Good', 'Well-made', 'Amazing', 'Heart-touching'],
    'SONGS' : ['songs', 'music', 'lyrics'],
    'HAPPY' : ['happy', 'satisfied', 'blissful', 'comfortable', 'joyful'],
    'WORK'  : ['work', 'sleep', 'work out', 'study'],
    'SINGING' : ['singing', 'dancing', 'composing'],
    'ARTIST' : ['artist', 'musician', 'singer'],
    'BRUNO_MARS' : ['Bruno Mars', 'Ariana Grande', 'Billie Eilish', 'Beyonce'],
    }


submission = reddit.submission('r0yi9l')

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.

    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.

    For example, if we randomly selected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''
    comment = random.choice(madlibs)
    for key in replacements:
        w = random.choice(replacements[key])
        comment = comment.replace('[' + key + ']',w)
    return comment


i = 0
while i<100:
    submission.reply(generate_comment())
    print(i)
    time.sleep(600)
    i+=1        

i = 0
while i<10:
    submission.comments[i].reply(generate_comment())
    print(i)
    time.sleep(600)
    i+=1
