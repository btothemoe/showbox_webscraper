import requests
from bs4 import BeautifulSoup

URL = "https://www.showboxpresents.com/events/all"
page = requests.get(URL)

## Initialize beautiful Soup
soup = BeautifulSoup(page.content, "html.parser")

## Only grab the eventsList div
results = soup.find(id="eventsList")

## From there, find all individual event divs
event_entries = results.find_all("div", class_="entry")

# Iterate through each individual event
for event_entry in event_entries:

    #Get Artist Name
    artist = event_entry.find('h3', class_="carousel_item_title_small").text.strip()
    print(artist)

    #Get Opening Artist Name
    opener = event_entry.find('h4', class_="animated").text.strip()
    print(opener)

    #Get Venue Name
    venue = event_entry.find('span', class_="venue").text.strip()[2:]
    print(venue)

    #Get Show Date
    date = event_entry.find('span', class_="date").text.strip()
    print(date)

    #Get Show Time
    time = event_entry.find('span', class_="time").text.strip()
    print(time)

    #Get Show link
    link = event_entry.find('a')['href']
    print(link)

    #Get Ticket Link
    tickets = event_entry.find('')

    #Seperate on print
    print("\n")
    

