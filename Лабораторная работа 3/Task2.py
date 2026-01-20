def find_common_participants(participants_first_group, participants_second_group, delim =','):
    common = set(participants_first_group.split(delim))
    return sorted(common.intersection(participants_second_group.split(delim)))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
