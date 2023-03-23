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
