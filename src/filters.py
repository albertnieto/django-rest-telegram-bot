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

def filter(message):
    text = message.text
    get_entities(message)



    match text:
        case 'Ep!':
            return ep(message)