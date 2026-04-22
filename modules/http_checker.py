import requests

def check_http(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("the website data has been fetched successfully....")
        return True

    else:
        print("failed to fetch the data ....")
        return False