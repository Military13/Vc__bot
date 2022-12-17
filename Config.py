import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "18302370"))
    API_HASH = os.environ.get("API_HASH", "03c2cced4dea9b1e96dce87558dd2381")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5807239493:AAHKLRz3UViw5PEh-TJLx42WtPbMWOTEio4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLEBu5q2HIIqlB_ieJF49XkzgtRbI6m-YfbK9zMJq70cupPiyxD7BSn6hsu0khCgQKR0KH82SyB7oG5FStJ9sqpQ1bZ8R3ztbnqyR9DfvEa8JbL0Si9mPsd8rCQzRiaOfGp8ZO-FQKp23wQwnQnAab78Ck2CTF4HFjKZF3JjboO2AR1ttsN-rO7ERpiVLneEl4xaBiQx_v2wNk6mCAzACqXq1c1ARLj-txxIPBfXR87mS0PFuomjfcz8zb9QtE7bmWngrMqj8UtJR_5naFTmve21IqES22Yj-ddZ2Cry-p1555JGdbxCozgDHk_MyepywkCZa7u4cZD8FXIwuZ7JY0S0os0=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Vc_Muic_Bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "2044151750")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
