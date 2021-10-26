INPUTFILE = "SPOILER_test_input.txt"


def get_prevoius_groups_from_file(file_name=INPUTFILE):
    file = open(file_name, 'r')
    previous_groups = [group.replace('\n', '').split(', ') for group in file.readlines()]
    file.close()
    return previous_groups


def get_all_students():
    previous_groups = get_prevoius_groups_from_file()
    students = set()
    for group in previous_groups:
        for student in group:
            students.add(student)
    return list(students)


def get_number_of_students():
    students = get_all_students()
    return len(students)


def is_valid_group_size(group_size: str):
    if not group_size.isnumeric() or int(group_size) < 2 or int(group_size) > get_number_of_students():
        return False
    return True


def get_all_possible_groups(group_size):
    students = get_all_students()
    groups = []
    for i in range(len(students) - group_size + 1):
        group = []
        for j in range(group_size):
            group.append(students[i])
        groups.append(group)
    return groups


def generate_groups(file, group_size):
    previous_groups = get_prevoius_groups_from_file()
    students = get_all_students()
    while len(students) > 0:
        for group in previous_groups:
            pass
        students.pop(0)

    # TODO:
    # -- check if any two people teamed before in a group
    # -- generete every possible groups from students of groups_size
    # - loop through every variation of students
    # - check if they were in the same group previously
    # - if not, create a new group of them
    # - do this for group_size sized groups
    pass


def get_group_size():
    group_size = input("Enter a group size:\n")
    while not is_valid_group_size(group_size):
        group_size = input("Invalid group size!\nPlease enter a positive integer:\n")
    return int(group_size)


def main():
    group_size = get_group_size()
    print(group_size)
    # generate_groups('test_.txt', group_size)
    generate_groups(INPUTFILE, group_size)


if __name__ == '__main__':
    main()
