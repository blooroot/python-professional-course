#             0         1         2        3            4
#            -5        -4        -3       -2           -1
courses = ["MongoDB", "Excel", "Power BI", "Python", "Django"]

copy_list = courses.copy() # courses[:]
print(copy_list)

courses.reverse() # courses[::-1]
print(courses)
# reverse modifica la lista original
# slicing hace una nueva

courses.sort(reverse = True)
print(courses)




