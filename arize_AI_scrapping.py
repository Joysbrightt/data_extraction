import requests as requests

import requests
from bs4 import BeautifulSoup


# Function to scrape information from a Slack web page
def scrape_slack_info(url):
    # Send a GET request to the Slack web page
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the web page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the elements containing the information you want to scrape
        # Replace these with the actual HTML tags and attributes you want to scrape
        # For example, to get the text of all <p> tags with class="slack-info"
        info_elements = soup.find_all('p', class_='slack-info')

        # Extract the information from the elements
        info_list = [info.text for info in info_elements]

        return info_list
    else:
        print("Failed to retrieve data from Slack")
        return None


# Replace 'slack_url' with the URL of the Slack web page you want to scrape
slack_url = 'https://app.slack.com/client/T0175GWSS8N/people'
scraped_info = scrape_slack_info(slack_url)

if scraped_info:
    for info in scraped_info:
        print(info)
