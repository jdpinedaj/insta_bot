# insta_bot
![badge1](https://img.shields.io/badge/language-Python-01B0F0.svg)
> An Instagram Bot which is useful to increase your followers gradually.
## Increase your Instagram followers gradually
This bot can be used to increase dozens of followers every day.
The bot search random posts on Instagram using a list of defined hastags, and then, it will like and comment the post, and follow the author. Later, many users will follow you back.

## How to use  insta_bot
### 1. Prerequisites
To be able to run this little bot, you need to have:
* [Python](https://www.python.org/downloads/)
* [Selenium](https://selenium-python.readthedocs.io/installation.html)
* [Chromedriver](http://chromedriver.chromium.org)
* Google Chrome (English version)
### 2. Configuration
After simply downloading this repository, open **config.py** , you’ll have to change some lines, considering the hashtags you want to use and the custom comments you would like to post.

Then, you have to create the file **credentials.py** and create three values:

    USERNAME = "your_username"
    PASSWORD = "your_password*"
    my_path = "your_path_to_chromedriver". Example: "/home/.../chromedriver"

### 3. Run
Once the configuration is complete, it's time to run this bot.
Simply run the command line below in a terminal:
```
$> python insta_bot.py
```
