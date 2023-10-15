import requests
from bs4 import BeautifulSoup
import time
import datetime


current_time = datetime.datetime.now()

# List of URLs to check
urls_to_check = [
    "https://paytm.com/movies/chennai/pvr-sathyam-royapettah-c/1007120",
    "https://paytm.com/movies/chennai/cinepolis-bsr-mall-omr-thoraipakkam-c/9505",
    "https://paytm.com/movies/chennai/inox-the-marina-mall-omr-egatoor-c/7589",
    "https://paytm.com/movies/chennai/inox-phoenix-market-city-velachery-formerly-jazz-cinemas-c/51767",
    "https://paytm.com/movies/chennai/pvr-theyagaraja-thiruvanmiyur-chennai-c/1007119"
]


# Function to send an email
# Function to send message 
def send_message(user_id, text): 
    
    bf_token = '6557014891:AAFY1cTyFBl1DqJJ4IRKo1Ci81l2si0owqg' # from BotFather  
    url = f'https://api.telegram.org/bot{bf_token}/sendMessage' 
    params = { 
      "chat_id": user_id, 
      "text": text, 
    } 
    response = requests.get(url, params=params) 

# Function to search for a specific text in the content of a URL
def search_text_in_url(url, text_to_search):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find and extract all text from the webpage
        all_text = soup.get_text()
        
        # Check if the specified text is in the extracted text
        if text_to_search in all_text:
            print(f"Movie Booking on '{text_to_search}' is opened on theatre {url}.")
            message = f"Movie Booking on '{text_to_search}' is opened on theatre {url}."
            send_message('-1001985872411', message) # user_id from userinfobot
        else:
            print(f"Movie Booking on '{text_to_search}' is not opened on theatre {url}.")
    else:
        print(f"Failed to retrieve {url}. Status code:", response.status_code)

# Search for the specified text in each URL
text_to_search = "Thu19"  # Change this to the text you want to search for

while True:
    for url in urls_to_check:
        search_text_in_url(url, text_to_search)
    print("Current time:", current_time)    
    time.sleep(300)  # Delay for 100 seconds before the next iteration
