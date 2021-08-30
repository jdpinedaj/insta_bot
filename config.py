from random import randint
# Own modules
from credentials import *

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
***IMPORTANT***
Please be aware of Instagram's daily limits for likes and comments to avoid getting banned
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Local path to chrome driver
chromedriver_path = my_path # Change this to your own chromedriver path! Example: '/home/.../chromedriver'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Make all the adjustments you like
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# List of hashtags
hashtag_list = ['visitluxembourg', 'bestdestinations', 'nature_photography', 'luxembourg']

# List of comments to be randonmly chosen from
comments_list = ['Really cool!', 'Nice work ❤️', '👏👏', 'wow 👏', 'Amazing picture! continue the good work!', 'well said', 'so cool! 🙌', '❤️', 'lovely 😍', 'amazing 👌', 'amazing', 'wow ❤️', 'well said 👏', '👏👏👏👏', 'Nice!', 'nice 🔥', 'feels good 😍', 'Good job! 😊', '❤️🔥🔥😍', 'thoughtful 👌', 'that is really deep!', 'intense 💯', '😊😊', 'i will take it as quote of the day','too much motivation 👌','very inspiring ❤️🔥']

# Number of posts to go through per hashtag
number_of_posts = 20

# Chance of commenting on photo
# i.e. chance_to_comment = 4 means a 1/4 chance
chance_to_comment = 1

# Time to wait in between processing instagram posts in seconds
# Enter lower and upper limit in randint()
wait_between_posts = randint(7, 16)

# Time to wait in between liking a post and commenting on it in seconds
# Enter lower and upper limit in randint()
wait_to_comment = randint(5, 15)