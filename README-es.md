# Cadena-de-Densidad

Este proyecto implementa el enfoque de resumen de texto de cadena de densidad del artículo ["From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting"](https://arxiv.org/pdf/2309.04269.pdf) realizado por investigadores de Salesforce, MIT, Columbia y otros.

La summarización de cadena de densidad es una técnica nueva que crea resúmenes altamente condensados pero ricos en información a partir de texto extenso. Funciona extrayendo de manera iterativa entidades esenciales del texto fuente y reescribiendo el resumen para incorporar más entidades cada vez (sin perder las entidades anteriores), lo que resulta en una "cadena" de resúmenes cada vez más densos.

Esta implementación toma una entrada de texto largo (por ejemplo, artículos, blogs, documentos técnicos, documentos) y la ejecuta a través de múltiples ciclos de extracción de entidades y reescritura de resúmenes para producir un resumen final y denso que contiene solo la información crítica del origen.

Beneficios clave del enfoque de cadena de densidad incluyen:

- Producción de resúmenes altamente comprimidos pero fieles
- Captura de detalles clave y conceptos de texto complejo y extenso
- Destilación iterativa de la densidad de la información
- Aprovechamiento de las capacidades de modelos de lenguaje grandes para la summarización

Este repositorio proporciona código para aplicar la summarización de cadena de densidad a entradas de texto arbitrarias utilizando la API de OpenAI. Extrae entidades, construye prompts de cadena de pensamiento, consulta la API y produce resúmenes condensados.

## Uso

Para ejecutar el resumidor:

1. Instalar dependencias:

```
poetry install 
```

2. Crear un archivo .env y establecer tu clave de API de OpenAI:

```
OPENAI_API_KEY=<tu-clave>
```

3. Actualizar config.ini con la ruta del archivo de texto de entrada y la ubicación de salida.

4. Ejecutar el resumidor: 

```
poetry run cod
```

Esto cargará el texto de entrada, ejecutará la summarización de cadena de densidad y guardará el resultado en el archivo configurado.

## Implementación

La lógica principal se encuentra en main.py. Realiza las siguientes acciones:

- Carga el texto de entrada
- Obtiene la clave de API de OpenAI del archivo .env  
- Envía un prompt a la API de OpenAI con el texto
- Recibe una cadena de 5 resúmenes cada vez más densos
- Exporta el resultado al .txt

El prompt sigue en gran medida la metodología descrita en el artículo, con ajustes menores.

Las opciones de configuración como las rutas de entrada/salida se almacenan en config.ini.

## POR HACER

- Analizar la salida como JSON
- Recopilar la lista de entidades y entidades adicionales faltantes
- Permitir la fusión y summarización secuencial de múltiples entradas
- Agregar una crítica del enfoque de cadena de densidad para la summarización (pros y contras)

## Referencias

- ["From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting"](https://arxiv.org/pdf/2309.04269.pdf)
- ["Annotated + Unannotated CoD Summaries on Hugging Face"](https://huggingface.co/datasets/griffin/chain_of_density/)
- Generación de requirements.txt `poetry export --without-hashes -f requirements.txt --output requirements.txt`
