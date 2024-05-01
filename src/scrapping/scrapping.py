from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException



options = webdriver.FirefoxOptions()
options.add_argument('--no-sandbox') 
# options.add_argument("--headless")
driver =  webdriver.Firefox(options=options)
driver.get("https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros")
driver.implicitly_wait(time_to_wait=10)


kindOfDemand = ""
if kindOfDemand == "":
    element = driver.find_element(by=By.ID, value="mat-input-1")
else:
    element = driver.find_element(by=By.ID, value="mat-input-3")

element.clear()
element.send_keys("1791251237001")

searchButton = driver.find_element(by=By.CLASS_NAME, value="boton-buscar")
driver.implicitly_wait(5)
searchButton.click()

# busqueda de procesos
processes = driver.find_elements(By.CLASS_NAME, "causa-individual")


for process in processes:
    process_text = process.text.splitlines()
    print("Número:", process_text[0])
    print("Fecha:", process_text[1])
    print("Código:", process_text[2])
    print("Descripción:", process_text[3])
    print("Icono:", process_text[4])
    print() 
    
    icon_detail = process.find_element(By.CLASS_NAME, "search-icon")
    if icon_detail:
        try:
            icon_detail.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-icon")))

            general_info_elements = driver.find_elements(By.XPATH, "//section[@class='filtros-busqueda']//*")
            general_info = {}

            for element in general_info_elements:
                if element.text.strip():
                    if element.tag_name == "strong":
                        key = element.text.strip()
                    elif element.tag_name == "span":
                        value = element.text.strip()
                        general_info[key] = value
        
            print(general_info)
            print()
        except StaleElementReferenceException:
            # Si se produce la excepción StaleElementReferenceException, volvemos a encontrar el icono de detalle
            icon_detail = process.find_element(By.CLASS_NAME, "search-icon")
            icon_detail.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-icon")))
            # Luego continuamos con el proceso de obtención de información
            general_info_elements = driver.find_elements(By.XPATH, "//section[@class='filtros-busqueda']//*")
            general_info = {}

            for element in general_info_elements:
                if element.text.strip():
                    if element.tag_name == "strong":
                        key = element.text.strip()
                    elif element.tag_name == "span":
                        value = element.text.strip()
                        general_info[key] = value
        
            print(general_info)
            print()







            
    #     processes_detail = driver.find_elements(By.CLASS_NAME, "movimiento-individual")

    #     processes_detail_list = []
    #     for detail in processes_detail:
            
    #         incident_number = detail.find_element(By.CLASS_NAME, "numero-incidente").text.strip()
    #         date = detail.find_element(By.CLASS_NAME, "fecha-ingreso").text.strip()
    #         actors = detail.find_element(By.CLASS_NAME, "lista-actores").text.strip()
    #         defendants = detail.find_element(By.CLASS_NAME, "lista-demandados").text.strip()

    #         proceess_details_dict = {
    #             "no": incident_number,
    #             "date": date,
    #             "actors": actors,
    #             "defendants": defendants
    #         }
    #         processes_detail_list.append(proceess_details_dict)
    #         try:
    #             icon_judicial_act = detail.find_element(By.CLASS_NAME, "search-icon")
    #             icon_judicial_act.click()
    #             WebDriverWait(driver, 10).until(EC.url_contains("/actuaciones"))
    #             panels = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "mat-expansion-panel")))

    #             for panel in panels:
    #                 process_panel = panel.text.splitlines()
    #                 print("init_date:", process_panel[0])
    #                 print("detail:", process_panel[1])
    #                 print("content:", process_panel[2])
    #                 # No se especifica que hacer con el folder
    #             driver.back()

                
    #         except NoSuchElementException as error:
    #             print("log error")

        
    #     driver.find_element(by=By.CLASS_NAME, value="btn-regresar")
        
    #     driver.implicitly_wait(2)
        