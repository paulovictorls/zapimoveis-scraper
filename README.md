# Zap Imoveis Scraper
============

zapimoveis-scraper is a Python package that works as a crawler and scraper using beautifulsoup4 to get data from [zap imóveis](https://zapimoveis.com.br).



### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install zapimoveis-scraper.
```bash
    pip install zapimoveis_scraper
```

### Usage 

```python
import zapimoveis_scraper as zap

  zap.search(localization="go+goiania++setor-oeste", num_pages=5) # returns a list with objects containing scraped data
```

#### Available search parameters:
* Localization (string): location in which the search will be performed
  * default: 'go+goiania++setor-marista'
* num\_pages (int): Number of pages to scrape
  * default: 1
* acao (string): type of contract. Possible values: 'venda', 'aluguel', 'lancamentos'
  * default: 'aluguel'
* tipo (string): type of property. Possible values: 'imoveis', 'apartamentos', 'casas'
  * default: 'casas'
* dictionaty\_out (boolean): Specifies the method output (list of objects or dictionary)
  * default: False
