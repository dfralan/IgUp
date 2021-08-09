from instabot import Bot
import glob, random, time, shutil


while True:
    shutil.rmtree('config/', ignore_errors=True) #delete config folder to loggin again
    bot = Bot()
    bot.login(username="REPLACE_WITH_USERNAME", password="REPLACE_WITH_PASSWORD")
    to = 'photo/' #photo folder directory
    toUp = random.choice(glob.glob(to + '*.jpg'))
    subList = ["🌈", "❤️", "🔥", "✌", "🧠", "👅", "🍀", "🌿", "🌷", "🌕", "🍏", "🥝", "🍟"] #replace with the captions of your choice
    sub = random.choice(subList)
    bot.upload_photo(toUp, caption=sub)
    sleeper = random.randint(50, 60) #time interval to start over
    print(str("Success, go to sleep for " + str(sleeper) + "seconds."))
    time.sleep(sleeper)
