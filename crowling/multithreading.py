import requests 
from concurrent.futures import ThreadPoolExecutor 
 
def get_url(url): 
    return requests.get(url) 
      
with ThreadPoolExecutor(max_workers=50) as pool: 
    sites = ["https://sajacosmetics.com/roqvel/barbe/rasage/"]*10000 
    print(list(pool.map(get_url,sites))) 
