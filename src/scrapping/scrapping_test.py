import unittest
import scrapping

class concurrency_test(unittest.TestCase):
    print("init test")
    
class continuos_test():
    
    print("continuos test")
    scrapping.get_page_info("0968599020001", "https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros", True, "/home/juno/Downloads/chrome-2/chromedriver-linux64/chromedriver")
    scrapping.get_page_info("1791251237001", "https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros", True, "/home/juno/Downloads/chrome-2/chromedriver-linux64/chromedriver")
    scrapping.get_page_info("0968599020001", "https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros", False, "/home/juno/Downloads/chrome-2/chromedriver-linux64/chromedriver")
    scrapping.get_page_info("0992339411001", "https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros", False, "/home/juno/Downloads/chrome-2/chromedriver-linux64/chromedriver")
    
    
# Si este script se ejecuta como un programa principal, ejecuta las pruebas
if __name__ == '__main__':
    unittest.main()
