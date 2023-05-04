# Proyecto de Ingeniería - Grupo2

[ENLACE COMPETICIÓN](https://nuwe.io/dev/competitions/reto-ensena-oracle-espana)

<details>
  <summary>Reto 1 - Reconocimiento de imágenes</summary>
  En 2024, NUWE unirá tecnología y restauración lanzando en España la cadena de restaurantes del futuro: “NUWE EVA”. En “NUWE EVA" podrás elegir de entre un gran abanico de deliciosos platos que a simple vista parecerán la típica comida fast food, pero que estarán elaborados con los mejores ingredientes para que puedas disfrutar del mejor sabor y de la mejor calidad. Estarás comiendo en el restaurante healthy del momento. Y eso no es todo. Nuestro robot y talentoso camarero, “EVA”, os atenderá con gusto para ofreceros la mejor experiencia. (Caso ficticio)

  ## 🎯 Objetivo:
  Crea una clasificación de alimentos que estén o estarán presentes en nuestra carta, para que nuestro robot “EVA” pueda detectar lo que pedirán los comensales. Aquí tienes el data set para el desarrollo de tu reto.

  ## 💯 Evaluación:
  La evaluación y puntuación de este primer reto se evaluará con el criterio de F1-score macro.

  Está permitido tanto el entrenamiento manual del modelo como el transfer learning. El uso de datos externos puede ser penalizado.

  ## ✅ Formato de entrega
  Para el archivo que tiene que enviar le presentamos una plantilla de ejemplo de cómo tiene que ser el JSON:

  JSON template: https://storage.googleapis.com/challenges_events/01_2023/Vueling/Data/Vueling_F1/template.json

  En este fichero JSON es muy importante aclarar lo siguiente: Debes indicar la clave objetivo de cómo se visualiza; el valor será el JSON de los resultados del modelo de predicción. En estas predicciones la clave corresponderá a la fila con el idx_test y el valor será la predicción realizada por tu modelo.
</details>
<details>
  <summary>Reto 2 - Procesamiento del lenguaje natural</summary>
  
  ## ℹ️ Contexto
  “NUWE EVA”, la cadena de restauración fast food y healthy, sigue creciendo y queremos dar un paso más para mejorar y ofrecer el mejor servicio posible a nuestros clientes.

  Queremos evolucionar y ofrecer nuevas capacidades a nuestro robot y talentoso camarero, “EVA”, añadiendo la función de poder detectar, a través de frases y palabras utilizadas por los comensales, el grado de satisfacción de los platos probados y así ver qué platos y productos han gustado más o menos a los clientes.

  Nuestro robot ya sabe detectar lo que pedirán los comensales según los productos elegidos. Ahora queremos saber cuál es el feedback de cada cliente para detectar si le ha gustado o no el plato servido.
Dataset

  Para este reto, dispondrás de 2 CSVs: Train y Test. Como sus nombres indican, el primero te servirá para entrenar tu modelo de clasificación y el test para saber a qué etiqueta pertenecen. Contarás con los siguientes atributos para poder realizar las clasificaciones:

    train_idx/test_idx: Identificador de texto.
    text: revisar los datos para clasificar si son positivos o negativos.
    label: integer representation of the sentiment
    label_text: text of the sentiment

  Hay dos archivos descargables:

  - train.csv: [Descargar train.csv](https://storage.googleapis.com/challenges_events/03_2023/Oracle%202nd%20Reto/Data/train.csv)
  - test.csv: [Descargar test.csv](https://storage.googleapis.com/challenges_events/03_2023/Oracle%202nd%20Reto/Data/test.csv)


  ## 📖 Tareas
  Crea un modelo predictivo de clasificación para poder ordenar y o catalogar las reseñas. Primero entrena tu modelo con las reseñas de entrenamiento. Una vez tengas el modelo que maximice la puntuación F1 (macro.), utiliza las reseñas de prueba como entrada para tu modelo.

  ## ✅ Formato de entrega
  Para el archivo que tiene que enviar le presentamos una plantilla de ejemplo de cómo tiene que ser el JSON:

  JSON template: https://storage.googleapis.com/challenges_events/03_2023/Oracle%202nd%20Reto/Data/template.json

  En este fichero JSON es muy importante aclarar lo siguiente: Debes indicar la clave objetivo de cómo se visualiza; el valor será el JSON de los resultados del modelo de predicción. En estas predicciones la clave corresponderá a la fila con el idx_test y el valor será la predicción realizada por tu modelo.
  
  ⚠️ CONDICIONES PARA QUE SU SOLUCIÓN SEA EVALUADA CORRECTAMENTE:
  
  Su repositorio debe ser público.

  Tu repositorio debe estar en la rama 'main'. Si creaste tu repo desde VSCode y tu rama principal superior es 'master'. Necesitas crear una rama llamada 'main' y mover todo a esta rama.

  Dentro de tu repositorio debe estar el archivo 'predictions.json'.

  Si tu enlace termina en '.git' quita el '.git' de la url y pégalo.

  👍 Link correcto: https://github.com/CarlosIbCu/example_se
  
  👎 Link incorrecto: https://github.com/CarlosIbCu/example_se.git

  ## 💯 Evaluación
  La evaluación y puntuación de este segundo reto se evaluará también con el criterio de F1-score macro.

  Está permitido tanto el entrenamiento manual del modelo como el transfer learning. El uso de datos externos puede ser penalizado.
</details>
<details>
  <summary>Reto 3 - Modelo predictivo valor EUR/USD</summary>
  
  ## ➡️ Contexto:

NUWE EVA es una cadena de restaurantes innovadora y disruptiva que emplea robots para realizar todas las tareas humanas. Además de esta característica única, también buscan diferenciarse de los demás restaurantes en la forma en que asignan los precios a su carta. Han decidido vincular los precios del menú a las fluctuaciones del mercado de divisas, específicamente en el valor EUR/USD.

Si bien esta estrategia de pricing tiene el potencial de atraer a muchos comensales curiosos, también presenta un riesgo significativo para la estabilidad del negocio debido a la imprevisibilidad de los ingresos.

## 📄 Dataset:

Para este reto tendréis dos archivos descargables: un 'training_set.csv' y 'testing_set.csv'. El primero se debe emplear para el entrenamiento del modelo, y el segundo para introducirlo como input a tu modelo y entregar las predicciones. Abajo los parámetros que hay tener en cuenta:

- Time: Indica la fecha y hora en la que se registró el precio del par de divisas EUR/USD. Esto es fundamental para analizar las fluctuaciones y tendencias del mercado en diferentes períodos de tiempo.

- Open: Representa el precio de apertura del par EUR/USD en el período de tiempo especificado. Es el primer precio registrado al comienzo de dicho intervalo, como una hora, un día o una semana.

- High: Muestra el precio más alto alcanzado por el par EUR/USD durante el período de tiempo analizado. Este valor es útil para identificar los niveles de resistencia en el análisis técnico.

- Low: Refleja el precio más bajo alcanzado por el par EUR/USD en el período de tiempo estudiado. Este valor es relevante para determinar los niveles de soporte en el análisis técnico.

- Close: Indica el precio de cierre del par EUR/USD en el período de tiempo especificado. Es el último precio registrado antes de que finalice dicho intervalo, proporcionando una idea de cómo terminó la sesión de negociación.

- Volume: Muestra la cantidad de unidades de EUR/USD negociadas durante el período. El volumen puede ayudar a identificar la fuerza de una tendencia o confirmar la validez de un movimiento de precios.

- Label: Es la clase que les permitirá predecir ciertas dinámicas del mercado, permitiéndoles así estimar los márgenes de beneficio que tendrán en sus menús con antelación. Esta será la variable que se tendrá que predecir en el dataset de test.

Hay dos archivos descargables:

- training_set.csv: [Descargar training_set.csv.](https://challenges-asset-files.s3.us-east-2.amazonaws.com/0-challenges_data/2023_04/Oracle_3rd_challenge/training_set.csv)
- testing_set.csv: Se trata de una tabla que relaciona el EUR/USD del conjunto de datos de prueba con los atributos descritos anteriormente, excepto la etiqueta. [Descargar testing_set.csv](https://challenges-asset-files.s3.us-east-2.amazonaws.com/0-challenges_data/2023_04/Oracle_3rd_challenge/testing_set.csv)


## 🎯 Objetivo:

Crea un modelo predictivo de clasificación para poder entender las dinámicas de movimiento del EUR/USD, únicamente en base a valores del pasado y presente y por último integra el uso de APEX en el mismo.

1. Realiza un análisis exploratorio de los datos empleando APEX.

2. Crea un modelo predictivo que maximice la puntuación F1-score (macro). Entrenando tu modelo con el dataset de training (trainig_test.csv), y efectuando las predicciones sobre el dataset de testing (testing_set.csv).

3. Crea una presentación (máx 9 slides) con la siguiente estructura:
- Portada.
- Análisis exploratorio de los datos: Resumen y visualizaciones clave.
- Preprocesamiento de los datos: Pasos principales y criterios utilizados.
- Modelos y técnicas de predicción: Modelos seleccionados y justificación.
- Entrenamiento, validación y resultados: Proceso y métricas principales.
- Conclusiones.

Se pueden usar fuentes de datos externas para la resolución del reto, como por ejemplo datos históricos de tweets, noticias, etc.

IMPORTANTE:
Hay que tener cuidado de no incurrir en el look-ahead bias. Esto será penalizado. El modelo solo puede utilizar valores actuales (t) o pasados (t-1,...t-n) como elementos predictivos. Si el modelo emplea datos futuros, es decir (t+n), el modelo estaría accediendo a información futura, por lo que la predicción no será válida.

EJEMPLO:
Para predecir el label del día 18 de Mayo de 2018, el modelo tan solo podrá usar las variables de predicción referentes al 18 de Mayo de 2018 y de los días previos (17,16,15... de Mayo de 2018).

Os dejamos un vídeo con trucos para el desarrollo del tercer reto, de la mano de Joan Itarte, Technical Manager - Emerging Technology en Oracle España: [VER VÍDEO (ESP)](https://videohub.oracle.com/media/t/1_vwnhlwt2)

## ℹ️ APEX:

Pasos para solicitar un workspace en APEX: Los equipos participantes del reto deberán cursar los siguientes pasos para acceder a la prueba gratuita de APEX y solicitar un workspace:

- Acceder URL: https://apex.oracle.com/es/
- Seleccionar opción “Comenzar prueba gratuita hoy mismo”.
- Solicitar un espacio de trabajo gratuito en apex.oracle.com .
- Identificar nombre, apellido, correo electrónico, nombre del workspace
- Responder cuestionario.
- Submit Request
- Acceder correo electrónico identificado para realizar el “cambio de contraseña” y acceder al workspace generado.

Aquí tenéis un video explicativo de los pasos a seguir para solicitar workspace en APEX: VER VÍDEO (ENG) . SQL para crear la tabla:

CREATE TABLE RELACION_EUR_USD(  "ID" NUMBER NOT NULL ENABLE,
      "TIME" TIMESTAMP (6) NOT NULL ENABLE,      
      "OPEN" NUMBER,
      "HIGH" NUMBER,
      "LOW" NUMBER,
      "CLOSE" NUMBER,
      "VOLUME" NUMBER,
      "LABEL" NUMBER,
      CONSTRAINT "RELACION_EUR_USD_PK" PRIMARY KEY ("ID")
USING INDEX ENABLE
) ;

## ✅ Formato de entrega:

Debe de haber al menos los siguientes 3 archivos:

1. Archivo predictions.json
   
   Las predicciones del dataset 'testing_set.csv' deben estar en un archivo JSON llamado predictions.json, un ejemplo se puede encontrar en el siguiente link.
   
   En este fichero de predicciones, en formato json, cada fila corresponderá al valor predicho del test_idx , es decir, si el primer valor es un 2 significa que este 2 corresponde al primer fichero del conjunto de datos de prueba.
   
   Es IMPORTANTE llamar a la columna target tal y como se especifica en el formato. Recuerda que puedes usar la función to_json de pandas para convertir tu dataframe a json, la longitud de las predicciones tiene que ser la misma que en testing_set.csv.

2. Archivo 2: presentation.pdf: Este archivo debe de contener la presentación.

3. Archivo 3: main.py or main.ipynb: Este archivo debe contener el main de tu código fuente.

## ✍️ Evaluación:

En la evaluación se tendrá en cuenta lo siguiente:

- 1000/1500 (presentación): La presentación será evaluado por un jurado compuesto por el equipo técnico de Oracle. Los campos en los que se valoraran en esta presentación son:
        250 pts: Claridad en la exposición del EDA (Análisis exploratorio de los datos) y empleo de APEX.
        250 pts: Coherencia y organización del proceso de resolución.
        250 pts: Calidad y justificación de las técnicas y métodos empleados.
        250 pts: Interpretación de resultados y aplicabilidad de las soluciones.

- 500/1500 (F1 score): A partir de F1-score (macro) del modelo predictivo. Comparando las predicciones de tu modelo del dataset de testing, con las del ground truth.

Está permitido el uso de transfer learning y de datos externos como tweets, noticias, etc... IMPORTANTE: Hay que tener cuidado de no incurrir en el look-ahead bias. Esto será penalizado.

REFERENCIAS DE QUANTITATIVE FINANCE:
- [Beginner’s Guide to Quantitative Trading I: Useful skills and where to find them](https://medium.com/auquan/a-beginners-guide-to-quantitative-trading-e6ed5d6b1c0d)
- [Beginner's Guide to Quantitative Trading](https://www.quantstart.com/articles/Beginners-Guide-to-Quantitative-Trading)
- [Python for Finance, Part 2: Intro to Quantitative Trading Strategies](https://www.learndatasci.com/tutorials/python-finance-part-2-intro-quantitative-trading-strategies/)
- [Quantitative Finance Books](https://www.wallstreetmojo.com/top-best-quantitative-finance-books)

REFERENCIAS APEX:
- [Curso de "learning path" en mylearn de oracle.](https://mylearn.oracle.com/ou/learning-path/oracle-apex-foundations/112444)
- [Laboratorios prácticos de Oracle sobre el uso de APEX](https://apex.oracle.com/es/learn/tutorials/)
- [Guia introducción al uso de aplicaciones de Oracle APEX](https://docs.oracle.com/en/database/oracle/apex/22.2/aeeug/index.html)
- [Libros articulos referenciados por Oracle de terceros](https://apex.oracle.com/es/learn/books/)
- [Creating charts (App builder User Guide)](https://docs.oracle.com/en/database/oracle/apex/22.2/htmdb/creating-charts.html/)
- [Sample charts (App builder User Guide)](https://apex.oracle.com/pls/apex/r/apex_pm/sample-charts/home)
</details>
