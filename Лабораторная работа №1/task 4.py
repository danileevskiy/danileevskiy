users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
reestr = { "Общее количество": 0, "Уникальные посещения": 0 }
sum_of_numbers = len(users)
unique_numbers = len(set(users))
reestr["Общее количество"]=sum_of_numbers
reestr["Уникальные посещения"]=unique_numbers
print(reestr)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
