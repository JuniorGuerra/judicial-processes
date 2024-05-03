# judicial-processes
API rest para scraping a una pagina web hecha con python

- Python
- Selenium
- Flask
- chrome-driver

## Importante
el programa puede ser ejecutado completamente, esto quiere decir que desde la api se puede hacer el scraping sin necesidad de tener que hacer el scraping por separado, claro esto tuvo que sacrificar algo de la prueba pero tome el riesgo, de igual forma se puede ejecutar de forma independiente el scraping para hacer su testing como se encuentra en el archivo scrapping_test.py en la ruta ./src/scrapping/ 
Si el usuario quiere ver en tiempo real lo que hace el scraping puede comentar la linea 120 del archivo ./src/scrapping/scraping.py

### Ejecucion
para ejecutar el programa completo solo es poner variables en .env y :
```sh
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