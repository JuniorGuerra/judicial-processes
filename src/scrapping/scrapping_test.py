import unittest
import scrapping
import concurrent.futures


class TestScraping(unittest.TestCase):
    def test_scraping_with_concurrency(self):
        urls = ["https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros"] * 15  # Se repite la misma URL 15 veces
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_url = {executor.submit(scrapping.get_page_info,"0968599020001", url, True, "/home/juno/Downloads/chrome-2/chromedriver-linux64/chromedriver"): url for url in urls}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data = future.result()
                    self.assertIsNotNone(data)  # Verifica que los datos no sean None
                    self.assertTrue(len(data) > 0)  # Verifica que los datos no estén vacíos
                except Exception as exc:
                    self.fail('%r generó una excepción: %s' % (url, exc))
                else:
                    print('%r página tiene %d bytes' % (url, len(data)))

    
# Si este script se ejecuta como un programa principal, ejecuta las pruebas
if __name__ == '__main__':
    unittest.main()
