def process_query(query):
    name, question = query.split(', ', 1)
    
    if name == 'анфиса':
        return process_anfisa(question)

def process_anfisa(question):
    if question == 'сколько у меня друзей?':
        return 'У тебя друзей много!'
    elif question == 'кто все мои друзья?':
        return 'Твои друзья: Коля, Соня, Маша'
    elif question == 'где все мои друзья?':
        return 'Коля в городе Красноярск, Соня в Москве, Маша в Питере'
    else:
        return None

print(process_query('анфиса, сколько у меня друзей?'))
print(process_query('анфиса, кто все мои друзья?'))
print(process_query('анфиса, где все мои друзья?'))
print(process_query('анфиса, кто виноват?'))
print(process_query('соня, ты где?'))