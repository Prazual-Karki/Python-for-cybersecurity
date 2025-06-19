# spider_url.py
# This script is a simple web crawler that searches for URLs containing a specific keyword.
# It uses the requests library to fetch web pages and BeautifulSoup to parse HTML.
# It starts from a given URL, collects all links on the page, and recursively visits each link.
# If a link contains the specified keyword, it prints the link and continues to crawl from there.
# The script maintains a set of visited URLs to avoid revisiting them.
# It is intended for educational purposes only and should not be used for malicious purposes.
# Make sure to install the required libraries using pip install requests beautifulsoup4



from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


visited_urls = set()
count = 1


# Function to crawl URLs and search for a keyword
# It takes a URL and a keyword as input
# It fetches the page content, parses it, and finds all anchor tags
# It extracts the href attribute from each anchor tag
# If the href is not None or empty, it adds it to a list of URLs
# It then checks each URL to see if it has been visited before
# If not, it joins the URL with the base URL, checks if it contains the keyword
# If it does, it prints the URL and increments a counter
# It then recursively calls the function on the new URL
# If the URL has already been visited, it skips it
# If the request fails, it prints an error message
# The function continues until all reachable URLs have been visited or the script is stopped
def spider_urls(url, keyword):
    global count
    try:
        response = requests.get(url)
    except:
        print(f"Error: request failed for {url}")
        return
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        a_tag = soup.find_all("a")
        urls =[]
        
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        
        for urls2 in urls:
            if urls2 not in visited_urls:
                visited_urls.add(urls2)
                url_join = urljoin(url,urls2)
                if keyword in url_join:
                    print(f"{count}: {url_join} \n")
                    count+=1
                    spider_urls(url_join, keyword)
            
            else:
                pass
            
        
   
print("")        
url = input("Enter the url you want to scrap: ")
keyword = input("Enter the keyword to search in the url provided: ")
print(f"\nStarting url spider for {url} with keyword={keyword} \n")
spider_urls(url,keyword)
        
        
        
