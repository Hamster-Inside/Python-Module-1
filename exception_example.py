class DownGradeException(Exception):
    pass


def lower_grade(actual_grade):
    actual_grade -= 1
    if actual_grade < 1:
        raise DownGradeException('Cannot be lower than 1')
    return actual_grade


try:
    grade = 2
    print(grade)
    grade = lower_grade(grade)
    print(grade)
    grade = lower_grade(grade)
    print(grade)
except DownGradeException as exception:
    print(exception)
finally:
    print('Done')