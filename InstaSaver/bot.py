import pytube
import telebot
import config

DOWNLOAD_FOLDER = 'D:\Projects\InstaSaver\downloads'

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types='text')
def downloadFromYoutube(message):
    message_link = message.text
    video_obj = pytube.YouTube(message_link)
    video = video_obj.streams.get_highest_resolution()
    video.download(DOWNLOAD_FOLDER)
    video_open = open('downloads\###.mp4', 'rb')
    bot.send_video(message.chat.id, video_open)
    video_open.close()


bot.polling(none_stop=True)
