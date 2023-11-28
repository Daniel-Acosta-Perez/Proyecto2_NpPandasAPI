<h1> Proyecto 2; manejo de numpy, pandas y APIs</h1>

<h2>Parte 1: Introducción al análisis de datos</h2>

<p>El proyecto de este curso consiste en analizar el conjunto de datos introducido en esta sección, procesarlo, limpiarlo y finalmente ajustar modelos de machine learning para realizar predicciones sobre estos datos.</p>

<p>Vamos a trabajar con un dataset sobre fallo cardíaco</p>
<p>El dataset contiene registros médicos de 299 pacientes que padecieron insuficiencia cardíaca durante un período de seguimiento.</p>

<h3>Características Clínicas</h3>

<ul>
    <li><strong>Edad:</strong> edad del paciente (años)</li>
    <li><strong>Anemia:</strong> disminución de glóbulos rojos o hemoglobina (booleano)</li>
    <li><strong>Presión arterial alta:</strong> si el paciente tiene hipertensión (booleano)</li>
    <li><strong>Creatinina fosfoquinasa (CPK):</strong> nivel de la enzima CPK en la sangre (mcg/L)</li>
    <li><strong>Diabetes:</strong> si el paciente tiene diabetes (booleano)</li>
    <li><strong>Fracción de eyección:</strong> porcentaje de sangre que sale del corazón en cada contracción (porcentaje)</li>
    <li><strong>Plaquetas:</strong> plaquetas en la sangre (kiloplaquetas/mL)</li>
    <li><strong>Sexo:</strong> mujer u hombre (binario)</li>
    <li><strong>Creatinina sérica:</strong> nivel de creatinina sérica en la sangre (mg/dL)</li>
    <li><strong>Sodio sérico:</strong> nivel de sodio sérico en la sangre (mEq/L)</li>
    <li><strong>Fumar:</strong> si el paciente fuma o no (booleano)</li>
    <li><strong>Tiempo:</strong> período de seguimiento (días)</li>
    <li><strong>[Objetivo] Evento de fallecimiento:</strong> si el paciente falleció durante el período de seguimiento (booleano)</li>
</ul>

<p>Tu tarea para esta etapa del proyecto integrador es convertir la lista de edades a un arreglo de NumPy y calcular el promedio de edad de las personas participantes en el estudio.</p>

<h2>Parte 2: Carga de datos</h2>

<p>Continuando con la anterior sección del proyecto integrador, ahora debes realizar lo siguiente:</p>
<ul>
    <li>Convertir la estructura Dataset en un DataFrame de Pandas usando pd.DataFrame.</li>
    <li>Separar el dataframe en dos diferentes, uno conteniendo las filas con personas que perecieron (is_dead=1) y otro con el complemento.</li>
    <li>Calcular los promedios de las edades de cada dataset e imprimir.</li>
</ul>

<h2>Parte 3: Calculando analíticas simples</h2>

<p>Continuando con el DataFrame con todos los datos de la anterior subsección, ahora debes:</p>
<ul>
    <li>Verificar que los tipos de datos son correctos en cada colúmna (por ejemplo que no existan colúmnas numéricas en formato de cadena).</li>
    <li>Calcular la cantidad de hombres fumadores vs mujeres fumadoras (usando agregaciones en Pandas).</li>
</ul>

<h2>Parte 4: Procesando información en bruto</h2>

<p>Imagina que no tuvieramos el acceso fácil de estos datos a través de la librería y tuvieramos que descargar los datos usando requests.</p>

<ul>
    <li>Realiza un GET request para descargarlos y escribe la respuesta como un archivo de texto plano con extensión csv (no necesitas pandas para esto, sólo manipulación de archivos nativa de Python)</li>
    <li>Agrupa el código para esto en una función reutilizable que reciba como argumento la url.</li>
</ul>

<h2>Parte 5: Limpieza y preparación de datos</h2>

<p>Una vez cargado el csv mediante el request anterior, realiza lo siguiente:</p>

<ol>
    <li>Verificar que no existan valores faltantes</li>
    <li>Verificar que no existan filas repetidas</li>
    <li>Verificar si existen valores atípicos y eliminarlos</li>
    <li>Crear una columna que categorice por edades
        <ul>
                <li>0-12: Niño</li>
                <li>13-19: Adolescente</li>
                <li>20-39: Jóvenes adulto</li>
                <li>40-59: Adulto</li>
                <li>60-...: Adulto mayor</li>
        </ul>
    </li>
    <li>Guardar el resultado como csv</li>
</ol>

<p>Encapsula toda la lógica anterior en una función que reciba un dataframe como entrada.</p>

<h2>Parte 6: Automatizando el proceso</h2>

<p>Imagina que los datos que procesaste en anteriores etapas del proyecto integrador se van actualizando cada cierto tiempo, (manteniendo el formato) y la url siempre va apuntando a la versión más actual, en este caso conviene tener automatizado el procesamiento en un script que pedas llamar y siempre te dé un csv limpio y listo para su análisis.</p>

<p>Tu tarea en esta etapa del proyecto consiste en crear un script (un archivo .py) que realice todas las operaciones vistas hasta ahora (desde el módulo de APIS) que al ejecutarse:</p>

<ol>
    <li>Descargue los datos desde una url</li>
    <li>Convierta todo a un dataframe</li>
    <li>Categorice en grupos</li>
    <li>Exporte un csv resultante</li>
</ol>

<p>La URL a usar y obtener los datos es: 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'</p>

<p>La url no debe estar definida como una constante en el código, en su lugar usa argumentos por terminal <a href='https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/'>(revisar este enlace)<a> para enviarle la url al programa al ejecutarlo.</p>

<h2>Parte 7: Analizando distribuciones 1</h2>
<p>Una vez tenemos los datos exportados por nuestro script de ETL, podemos proceder a realizar gráficas de análisis. En esta etapa del proyecto usa matplotlib para:</p>

<ol>
    <li>Graficar la distribución de edades con un histograma</li>
    <li>Graficar histogramas agrupado por hombre y mujer:
        <ul>
                <li>cantidad de anémicos</li>
                <li>cantidad de diabéticos</li>
                <li>cantidad de fumadores</li>
                <li>cantidad de muertos</li>
        </ul>
    </li>
</ol>

<p>El segundo histograma debe verse así:</p>
<img src="https://media.ada-school.org/5fcd3ac12b22eab4d301d819/61345ed31a244b00166eb22c/figure_1-9757dc9d-1ae7-47b3-b30b-ba9aa6afcfd5.png" />



