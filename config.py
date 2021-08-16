from random import randint

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
***IMPORTANT***
Please be aware of Instagram's daily limits for likes and comments to avoid getting banned
https://socialpros.co/instagram-daily-limits#Instagram%E2%80%99s_Daily_Limits_in_2020
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Local path to chrome driver
chromedriver_path = '/home/juan/Desktop/insta/venv/chromedriver' # Change this to your own chromedriver path!


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Make adjustments below to tweak the bot to your liking
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# List of hashtags to go through
hashtag_list = ['beautifuldestinations', 'photobomb', 
                #'nature_photography', 'visitluxembourg', 'bestdestinations', 'luxembourg'
                ]

# List of comments to be randonmly chosen from
commentsList = ['Really cool!', 'Nice work ❤️', '👏👏', 'wow 👏', 'well said', 'so cool! 🙌', '❤️', 'lovely 😍', 'amazing 👌', 'amazing', 'wow ❤️', 'well said 👏', '👏👏👏👏', 'Nice!', 'nice 🔥', 'feels good 😍', 'Good job! 😊', '❤️🔥🔥😍', 'thoughtful 👌', 'thatz deep', 'intense 💯', '😊😊', 'i will take it as quote of the day','too much motivation 👌','very inspiring ❤️🔥']

# Number of posts to go through per hashtag
number_of_posts = 10

# Chance of commenting on photo
# i.e. chance_to_comment = 4 means a 1/4 chance
chance_to_comment = 2

# Time to wait in between processing instagram posts in seconds
# Enter lower and upper limit in randint()
wait_between_posts = randint(7, 16)

# Time to wait in between liking a post and commenting on it in seconds
# Enter lower and upper limit in randint()
wait_to_comment = randint(10, 20)