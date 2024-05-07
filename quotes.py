import time
from bs4 import BeautifulSoup
import requests

def scrape_quotes():
    html_text = requests.get('https://www.passiton.com/inspirational-quotes').text
    soup = BeautifulSoup(html_text, 'lxml')
    quotes = soup.find_all('div', class_="col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top")

    with open('quotes.txt', 'a') as f: # Open the file in append
        for index, quote in enumerate(quotes):
            main_quote_alt = quote.find('img', class_='margin-10px-bottom shadow')['alt']
            main_quote = main_quote_alt.split('.')[0] # Extract text until the first full stop

            f.write(f"Quote {index + 1}: {main_quote.strip()} \n\n") # Write the quote to the file with a newline character
        print(f"File Saved: {index}")

    # Add an additional newline character for spacing between quotes

# Timer to scrape every 10 minutes
if __name__ == '__main__':
    while True:
         scrape_quotes()
         time_wait = 10
         print(f"Waiting {time_wait} minutes...")
         time.sleep(time_wait * 60)
