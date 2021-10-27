import itertools


INPUTFILE = "SPOILER_test_input.txt"


def write_results(results):
    size = len(results)
    if size < 2:
        file = open("output.txt", 'w')
        if size == 1:
            group = ""
            for i in range(len(results[0])):
                group += f"{results[0][i]}, "
            group = group[:-2]
            file.write(group)
        else:
            file.write("not possible to form groups")
        file.close()
    else:
        for i in range(size):
            file = open(f"output_{i + 1}", 'w')
            group = ""
            for j in range(len(results[i])):
                group += f"{results[i][j]}, "
            group = group[:-2]
            file.write(group + '\n')
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


def remove_students_from_group(students, groups: list):
    i = 0
    while i < len(groups):
        for student in students:
            if student in groups[i]:
                groups.remove(groups[i])
        i += 1


def generate_groups(file, group_size):
    previous_groups = get_prevoius_groups_from_file(file)
    students = get_all_students(previous_groups)

    while group_size > len(students):
        print(f"There are not enough students for {group_size} sized groups!")
        group_size = get_group_size()

    possible_groups = get_all_possible_groups(students, group_size)
    optimal_groups = []
    for possible_group in possible_groups:
        if not had_common_group(previous_groups, possible_group):
            optimal_groups.append(possible_group)
    return optimal_groups


def get_group_size():
    group_size = input("Enter a group size:\n")
    while not group_size.isnumeric() or int(group_size) < 2:
        group_size = input("Invalid group size!\nPlease enter an integer greater than 1:\n")
    return int(group_size)


def main():
    # group_size = get_group_size()
    # generate_groups('test_.txt', group_size)

    print(generate_groups(INPUTFILE, 2))
    write_results(generate_groups(INPUTFILE, 2))

    # TODO:
    # - generate different variations of optimal groups
    #   of all students if possible
    # - write the result(s) into file(s)


if __name__ == '__main__':
    main()
