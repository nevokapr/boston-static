import random

import requests

NASA_KEY = ''

# Implementing echoing: repetition of sent messages.


def echo(update, context):
    added = ', понял, спасибо.'
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text + added)

# Implementing /iss command: function that accesses iss api and returns results


def iss(update, context):
    loc_resp = requests.get('http://api.open-notify.org/iss-now.json').json()
    pep_resp = requests.get('http://api.open-notify.org/astros.json').json()
    if loc_resp['message'] != 'success':
        return context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Ошибка сервера!'
        )
    elif pep_resp['message'] != 'success':
        return context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Ошибка сервера!'
        )

    lon, lat = (loc_resp['iss_position']['longitude'],
                loc_resp['iss_position']['latitude']
                )

    coord_msg = (
        f'МКС прямо над этим местом!\nДолгота — {lon}\nШирота — {lat}'
    )

    names = []
    for human in pep_resp['people']:
        names.append(human['name'])

    names = ', '.join(names)
    names_msg = f'А вот какие прекрасные люди там находятся: {names}'

    return(
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'{coord_msg}\n\n\n{names_msg}'
        )
    )


# random xkcd


def xkcd(update, context):
    # Randomizing link, and concatenating into a url, then requesting from api
    number = random.randint(1, 2461)

    url = 'https://xkcd.com/' + str(number) + '/info.0.json'
    response = requests.get(url).json()

    return context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=response["img"],
        caption='Here goes an xkcd.com by a number ' + str(number),
        )


def nasa_apod(update, context):
    response = requests.get(
        f'https://api.nasa.gov/planetary/apod{NASA_KEY}'
    ).json()

    return context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=response["hdurl"],
        caption=response['title'],
        )


'''
Random cat!
sample response (it's 0'th index)
[{'breeds': [], 'categories': [{'id': 2,'name': 'space'}],
'id': '63', 'url': 'https://cdn2.thecatapi.com/images/63.
gif', 'width': 489, 'height': 400}]
can't get description key as of now.

[{"breeds":[],"id":"e60","url":"https://cdn2.thecatapi.com/images/e60.jpg","width":2203,"height":2606}]
'''


def cat(update, context):
    response = requests.get(
        'https://api.thecatapi.com/v1/images/search?api_key=KEY'
        ).json()
    if 'message' in response == 400:
        print(response)
        return context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Ошибка сервера!'
        )
    return context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=response[0]['url'],
        caption='Держи ко_та!\n ..от api.thecatapi.com'
    )
