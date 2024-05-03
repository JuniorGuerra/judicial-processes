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

En rules esta las bases que use durante el analisis del programa
```json
[
	{
		No: int,
     	fechaIngreso: date, 
     	No.Proceso: double,
     	EsDemandado: boolean,
     	Accion: string,
     	detail: {
			general_detail: {},
			specifi_details: [
	     		{   	
    				No: int,
    				Fecha: date,
    				Actores: string,
    				demandados: string,
					actuacionesJudiciales: [
	    				{
	    					fecha: date,
	    					detalle: string,
	    					info: string
	    				}
    				] 		
    	 		}
     		]
		}
	},
	{...},
	{...},	
]
```
