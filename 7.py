database = {
    'серёга': 'омск',
    'соня': 'москва',
    'миша': 'москва',
    'дима': 'челябинск',
    'алина': 'красноярск',
    'егор': 'пермь',
    'коля': 'красноярск'
}

def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'

def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(database)
        return f'у тебя {format_friends_count(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(database)
        return f'твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(database.values())
        cities_string = ', '.join(unique_cities)
        return f'твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'

print('привет, я анфиса!')
print(process_anfisa('сколько у меня друзей?'))
print(process_anfisa('кто все мои друзья?'))
print(process_anfisa('где все мои друзья?'))
print(process_anfisa('кто виноват?'))