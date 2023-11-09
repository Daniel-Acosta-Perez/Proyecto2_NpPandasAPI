from datasets import load_dataset
import numpy as np

#* Se carga el conjunto de datos
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

#* Acceder a la característica 'age' y convertirla a un arreglo de NumPy
ages = np.array(data['age'])
has_anemia = np.array(data['has_anaemia'])

#* Calcular el promedio de edad
average_age = np.mean(ages)
#* Calcular las personas con anemia
sum_has_anemia = np.sum(has_anemia)

# TODO: print(has_anemia) 
# TODO: print(data)
# TODO: print(ages)
print(f"El promedio de edad de las personas participantes en el estudio es: {average_age:.2f}" )
print(f"\n{sum_has_anemia} personas tienen anemia.")




