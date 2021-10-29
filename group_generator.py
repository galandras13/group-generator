import itertools


def write_results(results):
    size = len(results)
    if size < 2:
        file = open("output.txt", 'w')
        if size == 1:
            file.write(", ".join(results[0][0]))
        else:
            file.write("not possible to form groups")
        file.close()
    else:
        for i in range(size):
            file = open(f"output_{i + 1}.txt", 'w')
            for j in range(len(results[i])):
                file.write(", ".join(results[i][j]) + '\n')
            file.close()


def get_prevoius_groups_from_file(file_name):
    file = open(file_name, 'r')
    previous_groups = [group.replace('\n', '').split(', ') for group in file.readlines()]
    file.close()
    return previous_groups


def get_all_students(previous_groups):
    students = set()
    for group in previous_groups:
        for student in group:
            students.add(student)
    return sorted(list(students))


def had_common_group(previous_groups, possible_group):
    for i in range(len(possible_group) - 1):
        for j in range(i + 1, len(possible_group)):
            for group in previous_groups:
                if possible_group[i] in group and possible_group[j] in group:
                    return True
    return False


def get_all_possible_groups(students, group_size):
    return [[student for student in group] for group in itertools.combinations(students, group_size)]


def remove_students_from_group(groups: list, students):
    for student in students:
        i = 0
        while i < len(groups):
            if student in groups[i]:
                groups.remove(groups[i])
            else:
                i += 1


def get_optimal_groups(groups):
    result = []
    optimal_groups = groups[:]
    i = 0
    while i < len(optimal_groups):
        variation = []
        while len(optimal_groups) > 0:
            variation.append(optimal_groups[0])
            remove_students_from_group(optimal_groups, optimal_groups[0])
        result.append(variation)
        i += 1
        optimal_groups = groups[i:]
    return result


def generate_groups(file, group_size):
    previous_groups = get_prevoius_groups_from_file(file)
    students = get_all_students(previous_groups)

    while group_size > len(students):
        print(f"There are not enough students for {group_size} sized groups!")
        group_size = get_group_size()

    possible_groups = get_all_possible_groups(students, group_size)
    groups = []
    i = 0
    while i < len(possible_groups):
        if not had_common_group(previous_groups, possible_groups[i]):
            groups.append(possible_groups[i])
            # remove_students_from_group(possible_groups, possible_groups[i])
            # i = 0
        # else:
        #     pass
        i += 1
    print(groups)
    write_results(get_optimal_groups(groups))


def get_group_size():
    group_size = input("Enter a group size:\n")
    while not group_size.isnumeric() or int(group_size) < 2:
        group_size = input("Invalid group size!\nPlease enter an integer greater than 1:\n")
    return int(group_size)


def main():
    group_size = get_group_size()
    generate_groups('test_.txt', group_size)

    # TODO:
    # - generate different variations of optimal groups
    #   of all students if possible
    # - write the result(s) into file(s)


if __name__ == '__main__':
    main()
