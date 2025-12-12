#             0         1         2        3            4
#            -5        -4        -3       -2           -1
# slicing: [inicial:final:skip]
# slicing: [:] # shallow copy
# [::2] # shallow copy skipping every 2 elements
courses = ["MongoDB", "Excel", "Power BI", "Python", "Django"]

sub_list = courses[::-1]

print(sub_list)