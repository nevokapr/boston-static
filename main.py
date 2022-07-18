from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

import core


def main():

    # Booting bot

    token = 'TOKEN'
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    # Handling the handlers

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # sun_local_handler = CommandHandler('sun_local', core.sun_local)
    # dispatcher.add_handler(sun_local_handler)

    # save_handler = MessageHandler(Filters.photo, save_pic)
    # dispatcher.add_handler(save_handler)

    cat_handler = CommandHandler('cat', core.cat)
    dispatcher.add_handler(cat_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), core.echo)
    dispatcher.add_handler(echo_handler)

    iss_handler = CommandHandler('iss', core.iss)
    dispatcher.add_handler(iss_handler)

    xkcd_handler = CommandHandler('xkcd', core.xkcd)
    dispatcher.add_handler(xkcd_handler)

    apod_handler = CommandHandler('nasa_apod', core.nasa_apod)
    dispatcher.add_handler(apod_handler)

    # Asking tg server for messages
    updater.start_polling()

    # Stop the bot with SIGINT, SIGTERM, or SIGABRT
    updater.idle()

# Enabling /start command: defining a function that will send a message.


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='''Бот умер,да здравствует бот!.
        Прямо как @Nevokapr. Я умею давать вам кота! (или кошку)'''
        )


if __name__ == '__main__':
    main()
