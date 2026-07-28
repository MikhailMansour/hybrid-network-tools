import urllib.request
from bs4 import BeautifulSoup

def analyze_http(url):
    try:
  
        url = url.strip().replace("[", "").replace("]", "")
        if not url.startswith("http"):
            url = "https://" + url

        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            soup = BeautifulSoup(data, 'html.parser')
            
           
            status = resp.status
            server = resp.getheader('Server')
            title = soup.title.string if soup.title else "No Title"

           
            res_text = f"Status Code: {status}\nServer: {server}\nTitle: {title}"
            return res_text

    except Exception as e:
        return f"Error in HTTP analysis: {e}"