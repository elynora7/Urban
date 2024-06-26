def lesson2():
    tasks_count = 12
    spent_hours = 1.5
    course_name = 'Python'
    task_time = spent_hours / tasks_count

    print(
        f'Курс: {course_name}, всего задач: {tasks_count}, затрачено часов: {spent_hours}, среднее время выполнения {task_time} часа.')


if __name__ == '__main__':
    lesson2()
