from multiprocessing import Pool, cpu_count 
import time 
import requests 
 
def make_request(url): 
    """Makes a web request and prints the URL and response code.""" 
    resp = requests.get(url) 
    print("Url: {}".format(url)) 
    print("Response code: {}\n".format(resp.status_code)) 
 
if __name__ == '__main__': 
    urls = ["https://sajacosmetics.com"] * 9999 
    start = time.time() 
 
    # Creates a process pool with n processes, where 
    # n is the number returned by cpu_count 
    with Pool(cpu_count()) as p: 
 
        # Spawns a process for each URL 
        p.map(make_request, urls) 
    print("Execution time = {0:.5f}".format(time.time() - start)) 
