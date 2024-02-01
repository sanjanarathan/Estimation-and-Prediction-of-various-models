

import requests

def check_website_security(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            if response.url.startswith("https://"):
                return f"The website '(url)' is using a secure HTTPS connection."
            elif response.url.startswith("http://"):
                return f"WARNING The website '(url)' is using insecure http connection"
            else:
                return "The website protocol is not recognised."

        else:
            return f"FAiled to access the website.Status code:(response.status_code)"
    except requests.exceptions.RequestException as e:
        return f"An error occured :(e)"

if __name__=='__main__':
    website_url=input("Enter the url of the website u want to check")
    result=check_website_security(website_url)
    print(result)
        
                
