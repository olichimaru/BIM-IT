# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, delimiter=','):

    participants1 = set(first_group.split(delimiter))
    participants2 = set(second_group.split(delimiter))


    common_participants = list(participants1.intersection(participants2))
    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(result)

# TODO Провеьте работу функции с разделителем отличным от запятой
