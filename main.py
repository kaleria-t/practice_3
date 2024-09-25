homework_counter = 12
time_counter = 1.5
course_name = 'Python'
needed_time = (float(time_counter) / float(homework_counter))
print(needed_time)
print('Курс: ' + course_name + ', всего задач: ' + str(homework_counter) + ', затрачено часов: ' + str(time_counter) + ', среднее время выполнения ' + str(needed_time) + ' часа.') # вариант через конкатенацию, но с сохранённой пунктуацией
print('Курс:', course_name, 'всего задач:', homework_counter, 'затрачено часов:', time_counter, 'среднее время выполнения', needed_time, 'часа.') # вариант по заданию, через перечисление, но без пунктуации
