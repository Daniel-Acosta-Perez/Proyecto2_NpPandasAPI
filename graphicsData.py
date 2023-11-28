import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_age_distribution(data):
    # Configuración de estilo
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # Histograma con estilo Seaborn
    sns.histplot(data['age'], bins=20, kde=True, color='skyblue', edgecolor='black')

    # Añadir título y etiquetas
    plt.title('Distribución de Edades', fontsize=16)
    plt.xlabel('Edad', fontsize=14)
    plt.ylabel('Frecuencia', fontsize=14)

    # Añadir malla y leyenda
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend(['Densidad'], loc='upper right', fontsize='small')

    # Guardar la figura como una imagen
    plt.savefig('age_distribution.png', bbox_inches='tight')

    # Mostrar el gráfico
    plt.show()
    plt.close()

def plot_gender_comparison(data):
    # Leer el archivo CSV
    df = data
    # Dividir los datos por género
    m = df[df['sex'] == 1]  
    f = df[df['sex'] == 0]  

    # Calcular sumas para hombres
    smoking_m = m['smoking'].sum()  
    diabetes_m = m['diabetes'].sum()
    anemia_m = m['anaemia'].sum()
    deaths_m = m['DEATH_EVENT'].sum()

    # Calcular sumas para mujeres
    smoking_f = f['smoking'].sum()
    diabetes_f = f['diabetes'].sum()
    anemia_f = f['anaemia'].sum() 
    deaths_f = f['DEATH_EVENT'].sum()

    # Definir categorías y datos
    categorias = ['Anemicos', 'Diabeticos', 'Fumadores', 'Muertos']
    datos_m = [anemia_m, diabetes_m, smoking_m, deaths_m]
    datos_f = [anemia_f, diabetes_f, smoking_f, deaths_f]

    index = np.arange(len(datos_m))
    width = 0.30

    # Crear el gráfico
    fig, ax = plt.subplots()

    ax.bar(index-width/2, datos_m, width)
    ax.bar(index+width/2, datos_f, width)

    for i, j in zip(index, datos_m):
        ax.annotate(j, xy=(i-0.2,j+0.2))

    for i, j in zip(index, datos_f):
        ax.annotate(j, xy=(i+0.1,j+0.2))

    ax.set_title('Gráfico de comparación por género')
    ax.set_xticks(index)
    ax.set_xticklabels(categorias)
    ax.set_xlabel('Categorias')
    fig.legend(['Hombres', 'Mujeres'], loc='upper right', fontsize='small')

    fig.savefig('gender_comparison.png')
    plt.show()

def main():
    # Cargar el archivo 'cleaned_data.csv'
    clean_data = pd.read_csv('cleaned_data.csv')

    # Mostrar la distribución de edades
    plot_age_distribution(clean_data)
    # Mostrar comparacion por caracteristicas
    plot_gender_comparison(clean_data)

if __name__ == "__main__":
    main()
