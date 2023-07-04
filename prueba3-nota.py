nota_prueba_1 = 4
nota_prueba_2 = 2.8
nota_prueba_3 = 4
nota_proyecto = 6
nota_actividades_clases = 6

promedio_prueba = (nota_prueba_1+nota_prueba_2+nota_prueba_3)/3
promedio_prueba = round(promedio_prueba,1)
if promedio_prueba >= 4:
    nota_final =  promedio_prueba * 0.5 + nota_proyecto * 0.3 + nota_actividades_clases * 0.2
else:
    nota_final =  promedio_prueba * 0.8 + nota_proyecto * 0.1 + nota_actividades_clases * 0.1
nota_final = round(nota_final,1)
print(f"Mi nota final es {nota_final}")
if nota_final >= 3.5 and nota_final < 4:
    print(f"Puede ir a repechaje")
elif nota_final < 3.5:
    print(f"Reprobado el curso :(")

for posible_nota_p3 in range (10,71,1):
    posible_nota_p3 = posible_nota_p3 /10
    promedio_prueba = (nota_prueba_1+nota_prueba_2+posible_nota_p3)/3
    promedio_prueba = round(promedio_prueba,1)
    if promedio_prueba >= 4:
        nota_final =  promedio_prueba * 0.5 + nota_proyecto * 0.3 + nota_actividades_clases * 0.2
    else:
        nota_final =  promedio_prueba * 0.8 + nota_proyecto * 0.1 + nota_actividades_clases * 0.1
    nota_final = round(nota_final,1)
    if nota_final >= 3.5 and nota_final < 4:
        print(f"Puede ir a repechaje con promedio 3.5, y necesitarás un {posible_nota_p3} en la prueba 3")
        break
    elif nota_final >= 4:
        print(f"No necesitas ir a repechaje, y necesitarás un {posible_nota_p3} en la prueba 3")
        break

