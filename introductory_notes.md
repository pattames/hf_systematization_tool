# Análisis de Datos Sobre Florecimiento Humano

## Contexto General

- Investigación para recaudar datos de florecimiento humano en América Latina
- Temas de felicidad y bienestar, justicia, derechos humanos, salud y sostenibilidad
- Dificultad y utilidad del estudio: el término florecimiento humano se usa muy poco en latam pero los temas que abarca sí son muy estudiados
- Conceptos nacidos en la región y que se parecen a FH: Buen Vivir, Sumak Kasay.

## Estudio

- Dos partes o secciones.

### Estudio Bibliométrico/ Análisis de Big Data

- Input: base de datos de más de 300,000 documentos y publicaciones científicas de los últimos 20 años sobre temas de autores latinoamericanos.
- R y Shinnyapps para que cualquier investigador pueda visualizar los resultados. [Aquí la app](https://florecimientohumanotec.shinyapps.io/latinamericanMappingApp/)

### Exploración Cualitativa: Entrevistas a Más de 80 Expertos de la Región

- *Aquí es donde necesitan mi ayuda y para lo que voy a desarrollar la herramienta*
- Entrevistas a profundidad sobre el "estado del arte" de la investigación de FH en latam.
- A ojos de ellos, cómo está la investigación mediante las siguientes variables:
  - Actors: Who are the main actors in human flourishing research in the region? (Individuals, universities, civil organizations, research centers, government entities, and sponsors).
  - Areas: What are the topics and areas of knowledge? Which topics respond most clearly to the unique characteristics of this region?
  - Paths: How have studies on human flourishing evolved over time? What are the current research trends?
  - Collaboration: What are the networks and modes of collaboration in research? Which are the communication channels and meeting points?
  - Limitations: What are the main limitations of research in this region?
- Todas las entrevistas las tienen grabadas (casi todas en español, algunas en portugués de Brasil).
- Tarea: hacer trabajo de sistematización de la información con herramienta de IA generativa actual.

## Propuesta

- Utilizando llamada a API de Claude con output estructurado
- Enseñar como el generador de simuladores produce árboles de decisión
- Hacer énfasis en que primero hay que definir la estructura del output json (cómo se va a ordenar/ clasificar la información dentro del árbol)
