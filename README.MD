# Judicial Processes API

Esta API REST proporciona funcionalidades para realizar web scraping en una página web utilizando Python.

## Tecnologías Utilizadas

- Python
- Selenium
- Flask
- Chrome Driver

## Descripción

La API puede ser ejecutada completamente, lo que significa que se puede realizar el web scraping desde la propia API sin necesidad de ejecutar el scraping por separado. Sin embargo, para aquellos interesados en realizar pruebas independientes, se proporciona la opción de ejecutar el scraping por separado, como se muestra en el archivo `scrapping_test.py` en la ruta `./src/scrapping/`.

Si deseas ver en tiempo real lo que hace el scraping, puedes comentar la línea 120 del archivo `./src/scrapping/scraping.py`.

## Ejecución

Para ejecutar el programa completo, solo necesitas configurar las variables en el archivo `.env` y luego ejecutar:

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
### pruebas
para las pruebas hay un archivo postman.collection.json para nada mas ser utilizado.

para testear la app tiene 4 test que cubren basicamente todo
```sh
python app_test.py
```

solo el scraping es usar su funcion en el archivo o mas facil descomentar la funcion que esta en la linea 155:
```sh
python src/scraping/scraping.py
```

Para testear solo es correr el archivo de test:
esta prueba cuenta con una concurrencia que tiene 5 workers para no sobrecargar el app
```sh
python src/scraping/scraping_test.py
```

### Contacto
Si queda alguna duda con la prueba no dude en contactarme y notificarme lo sucedido.

## Desarrollo

## Campos

- `No`: Número de identificación del proceso (entero).
- `fechaIngreso`: Fecha de ingreso del proceso (formato de fecha).
- `No.Proceso`: Número de proceso (doble).
- `EsDemandado`: Indicador booleano que especifica si el proceso tiene demandados.
- `Accion`: Acción relacionada con el proceso (cadena de texto).
- `detail`: Detalles adicionales del proceso.
  - `general_detail`: Detalles generales del proceso.
  - `specifi_details`: Detalles específicos del proceso, incluyendo múltiples registros.
    - `No`: Número de identificación del detalle específico (entero).
    - `Fecha`: Fecha asociada al detalle específico (formato de fecha).
    - `Actores`: Lista de actores involucrados en el proceso (cadena de texto).
    - `demandados`: Lista de demandados en el proceso (cadena de texto).
    - `actuacionesJudiciales`: Lista de actuaciones judiciales realizadas, incluyendo múltiples registros.
      - `fecha`: Fecha de la actuación judicial (formato de fecha).
      - `detalle`: Detalle de la actuación judicial (cadena de texto).
      - `info`: Información adicional sobre la actuación judicial (cadena de texto).

## Ejemplo de Uso

```json
[
	{
		"No": 12981312781923,
		"fechaIngreso": "2024-01-01",
		"No.Proceso": 123123,
		"EsDemandado": true,
		"Accion": "Descripción de la acción",
		"detail": {
			"general_detail": {},
			"specifi_details": [
				{
					"No": 1,
					"Fecha": "2024-02-01",
					"Actores": "Lista de actores",
					"demandados": "Lista de demandados",
					"actuacionesJudiciales": [
						{
							"fecha": "2024-02-15",
							"detalle": "Detalle de la actuación judicial",
							"info": "Información adicional"
						}
					]
				}
			]
		}
	},
	{},
	{}
]