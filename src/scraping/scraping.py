from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import json

processes_list = []
def individual_process(process, window_id, driver): 
    
    processes_detail_list = []
    performances_list = []
    
    process_text = process.text.splitlines()
    
    icon_detail = process.find_element(By.CLASS_NAME, "search-icon")
    if icon_detail:
        
        ActionChains(driver).key_down(Keys.CONTROL).click(icon_detail).key_up(Keys.CONTROL).perform()
        
        new_window = [window for window in driver.window_handles if window != window_id][0]
        driver.switch_to.window(new_window)

        general_info_elements = driver.find_elements(By.XPATH, "//section[@class='filtros-busqueda']//*")
        general_info = {}

        for element in general_info_elements:
            if element.text.strip():
                if element.tag_name == "strong":
                    key = element.text.strip()
                elif element.tag_name == "span":
                    value = element.text.strip()
                    general_info[key] = value
    
        
        processes_detail = driver.find_elements(By.CLASS_NAME, "movimiento-individual")
        
        for detail in processes_detail:
            process_details_dict = {}
            
            try:
                incident_number = detail.find_element(By.CLASS_NAME, "numero-incidente").text.strip()
                date = detail.find_element(By.CLASS_NAME, "fecha-ingreso").text.strip()
                actors = detail.find_element(By.CLASS_NAME, "lista-actores").text.strip()
                defendants = detail.find_element(By.CLASS_NAME, "lista-demandados").text.strip()
                
                icon_judicial_act = detail.find_element(By.CLASS_NAME, "search-icon")
                icon_judicial_act.click()

                WebDriverWait(driver, 10).until(EC.url_contains("/actuaciones"))
                panels = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "mat-expansion-panel")))
                performance = {}
                for panel in panels:
                    process_panel = panel.text.splitlines()
                    
                    performance = {
                        "init_date": process_panel[0],
                        "detail": process_panel[1],
                        "content": "..."
                    }
                    #TODO: No aniadi el folder por un poquito de optimizacion
                    performances_list.append(performance)
                    
                process_details_dict = {
                    "no": incident_number,
                    "date": date,
                    "actors": actors,
                    "defendants": defendants,
                    "performance_judicial": performances_list,
                }
                processes_detail_list.append(process_details_dict)
                driver.back()

            except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as error:
                # print("log: reading process", error)
                print("log: reading process")
                continue 
        
        driver.find_element(by=By.CLASS_NAME, value="btn-regresar")
        
        driver.close()
        driver.switch_to.window(window_id)
        
        detail = {
        "No": process_text[0],
        "Date:": process_text[1],
        "Code:": process_text[2],
        "Description:": process_text[3],
        "detail": {
            "general_detail" : general_info,
            "specify_details": processes_detail_list,
           }
        }
        
        return detail

def save_json(txt, filename, isNotLocal):
    path = "../json/"
    if isNotLocal:
        path = "./src/json/"
    
    with open(path+filename, "w") as json_file:
        json.dump(txt, json_file)
        json_file.close()
        

def get_page_info(id: str, url: str, IsActor: bool, driver_path: str, isLocal=None):
    
    service = Service(r"{}".format(driver_path))

    service.start()

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox') 
    options.add_argument('--headless') # TODO: Comentar para visualizar
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(time_to_wait=10)

    driver.get(url)
    filename_diff = "actor"
    if IsActor:
        element = driver.find_element(by=By.ID, value="mat-input-1")
    else:
        filename_diff = "infractor"
        element = driver.find_element(by=By.ID, value="mat-input-3")

    element.clear()
    element.send_keys(id)

    searchButton = driver.find_element(by=By.CLASS_NAME, value="boton-buscar")
    driver.implicitly_wait(5)
    searchButton.click()


    processes = driver.find_elements(By.CLASS_NAME, "causa-individual")

    current_window_id = driver.current_window_handle

    all_process_details = []

    for process in processes:
        detail = individual_process(process, current_window_id, driver)
        all_process_details.append(detail)
    
    save_json(all_process_details, id + "_" + filename_diff + ".json", isLocal)
    return True



# get_page_info("1791251237001", "https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros", True, "/home/juno/Downloads/chrome-2/chromedriver-linux64/chromedriver")
