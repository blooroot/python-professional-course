# Refiere al concepto de storear los elementos de una tupla en variables
# Puede hacerse con los índices o direcatamente con el nombre de la tupla

courses = ("Django", "Flask", "FastAPI", "Python", "SQLAlchemy")

var1, var2, var3, var4, var5 = courses
# var 1, var2, var3, var4, var5 = courses[0], courses[1], courses[2], courses[3], courses[4]

print(
    var1, var2, var3, var4, var5
)

# skippeando valores
# var1, var2, _, var4, _ = courses

# agrupando en sublista
# var1, var2, *sub_courses = courses

# python reconoce patrones
# var1, var2, *sub_courses, last_value = course

# omitiendo una brecha de valores
#  var1, var2, *_, last_value = courses
