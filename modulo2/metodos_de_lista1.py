#             0         1         2        3            4
#            -5        -4        -3       -2           -1
courses = ["MongoDB", "Excel", "Power BI", "Python", "Django"]
courses_extend = ["HTML", "CSS", "JavaScript"]

# METODOS PARA AGREGAR

# agregar elementos al final
courses.append("SQL")
courses.append("Flask")
courses.append("Ruby on Rails")
# agregar en un indice especifico
courses.insert(4, "NoSQL")
# añadir otra lista
courses.extend(courses_extend)

# METODOS DE CONSULTA

# verificar si elemento está en la lista
print("Python" in courses)
# consultar el indice de un elemento
print(
    courses.index("Power BI"),
    courses.index("Ruby on Rails"),
    sep = "\n"
)

# METODOS DE ELIMINACION

courses.remove("Excel")  # elimina por valor
deleted = courses.pop(2)
courses.clear() # elimina todos los elementos de la lista

print(deleted)
print(courses)

