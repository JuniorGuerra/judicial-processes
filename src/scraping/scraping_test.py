import unittest
import scraping
import concurrent.futures

class TestScraping(unittest.TestCase):
    def test_scraping_with_concurrency(self):
        urls = ["https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros"] * 15 
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_url = {executor.submit(scraping.get_page_info, "0968599020001", url, True, "/home/juno/Downloads/chrome-2/chromedriver-linux64/chromedriver"): url for url in urls}
            for future in concurrent.futures.as_completed(future_to_url):
                self.assertTrue(future.done())

    

if __name__ == '__main__':
    unittest.main()
