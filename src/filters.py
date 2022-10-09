import pole


def ep(message):
    members = message


def get_entities(message):
    entities = message.entities
    for entity in entities:
        print(entity.type)
        print(entity.url)
        print(entity.offset)
        print(entity.length)
        print(entity.user)


def filter_message(message, handler=True):
    text = message.text
    # get_entities(message)

    if str(text).find('pole'):
        if handler:
            return True
        return pole.return_message(message)

    match text:
        case 'Ep!':
            return ep(message)
