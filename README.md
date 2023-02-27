# Proyecto de Ingeniería - Grupo2

[ENLACE COMPETICIÓN](https://nuwe.io/dev/competitions/reto-ensena-oracle-espana)

En 2024, NUWE unirá tecnología y restauración lanzando en España la cadena de restaurantes del futuro: “NUWE EVA”. En “NUWE EVA" podrás elegir de entre un gran abanico de deliciosos platos que a simple vista parecerán la típica comida fast food, pero que estarán elaborados con los mejores ingredientes para que puedas disfrutar del mejor sabor y de la mejor calidad. Estarás comiendo en el restaurante healthy del momento. Y eso no es todo. Nuestro robot y talentoso camarero, “EVA”, os atenderá con gusto para ofreceros la mejor experiencia. (Caso ficticio)

## 🎯 Objetivo:
Crea una clasificación de alimentos que estén o estarán presentes en nuestra carta, para que nuestro robot “EVA” pueda detectar lo que pedirán los comensales. Aquí tienes el data set para el desarrollo de tu reto.

## 💯 Evaluación:
La evaluación y puntuación de este primer reto se evaluará con el criterio de F1-score macro.

La limitación que existe en este reto son las tecnicas de Transfer Learning, se tiene que programar la red neuronal y entrenar de forma manual. Además, de que el uso de datos externos también se verá penalizado incluso desqualifiado para la competición.

## ✅ Formato de entrega
Para el archivo que tiene que enviar le presentamos una plantilla de ejemplo de cómo tiene que ser el JSON:

JSON template: https://storage.googleapis.com/challenges_events/01_2023/Vueling/Data/Vueling_F1/template.json

En este fichero JSON es muy importante aclarar lo siguiente: Debes indicar la clave objetivo de cómo se visualiza; el valor será el JSON de los resultados del modelo de predicción. En estas predicciones la clave corresponderá a la fila con el idx_test y el valor será la predicción realizada por tu modelo.
