# API de Gestión de Películas

Esta aplicación Flask proporciona una API simple para gestionar una base de datos de películas. La API permite agregar nuevas películas, obtener todas las películas por género y actualizar la información de una película existente.

## Configuración

Asegúrate de tener Python y Flask instalados en tu entorno. Puedes instalar Flask ejecutando el siguiente comando:

```bash
pip install flask
```

## Ejecución de la Aplicación

1. Guarda el código proporcionado en un archivo, por ejemplo, `app.py`.
2. Ejecuta la aplicación usando el siguiente comando:

```bash
python app.py
```

La aplicación se ejecutará en modo de depuración (`debug=True`) en el puerto `5000`.

## Endpoints

### 1. Agregar una Nueva Película

**Endpoint:** `/api/new-movie` (Método POST)

Este endpoint permite agregar una nueva película a la base de datos.

**Ejemplo de Solicitud:**
```json
{
    "movieId": 1,
    "name": "Titanic",
    "genre": "Romance"
}
```

### 2. Obtener Todas las Películas por Género

**Endpoint:** `/api/all-movies-by-genre/<string:genre>` (Método GET)

Este endpoint devuelve todas las películas que pertenecen al género especificado.

**Ejemplo de Solicitud:**
```
GET /api/all-movies-by-genre/Romance
```

**Respuesta:**
```json
[
    {
        "name": "Titanic",
        "genre": "Romance"
    },
    {
        "name": "The Notebook",
        "genre": "Romance"
    }
]
```

### 3. Actualizar una Película Existente

**Endpoint:** `/api/update-movie` (Método PUT)

Este endpoint permite actualizar la información de una película existente.

**Ejemplo de Solicitud:**
```json
{
    "movieId": 1,
    "name": "Titanic: Edición Especial",
    "genre": "Romance/Drama"
}
```

## Respuestas Comunes

- **Éxito (Código 200):** La solicitud se procesó con éxito.
- **Éxito al Agregar (Código 201):** La película se agregó correctamente.
- **Error de Solicitud (Código 400):** La solicitud no contiene los datos necesarios.
- **No Encontrado (Código 404):** No se encontró una película con el ID especificado.


---

Este README proporciona una descripción de la API, instrucciones para configurar y ejecutar la aplicación, así como detalles sobre los endpoints disponibles.
