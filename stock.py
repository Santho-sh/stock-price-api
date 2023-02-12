import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

app = FastAPI()

# To run : uvicorn stock:app --reload

@app.get("/{symbol}")
def get_price(symbol: str):
    
    url = f'https://finance.yahoo.com/quote/{symbol}'

    r = requests.get(url)
        
    soup = BeautifulSoup(r.content, 'html5lib')
    try:
        price = soup.find('fin-streamer', attrs={'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
        name = soup.find('h1', attrs={'class':'D(ib) Fz(18px)'}).text

        name, _ = name.split('.')
        
        details = {}
        details['name'] = name
        details['price'] = price
        
        return details
    
    except:
        return None
    
if __name__ == "__main__":
    app()
