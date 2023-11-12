def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    participants_first_set = set(participants_first_group.split(delimiter))
    participants_second_set = set(participants_second_group.split(delimiter))
    common_participants = list(participants_first_set.intersection(participants_second_set))
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(result)