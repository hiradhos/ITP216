# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# HW 9
# Description:
# Describe what this program does in your own words such as:
'''
This program integrates our learnings about web scraping via the BeatifulSoup library in order to print out the events at two different local venues
in chronological order. For extra credit, this program also prints out all events in chronological order (regardless of venue), and prints the performers
at each event along wtih the corresponding venue.
'''

import os
import ssl
import urllib.request
from bs4 import BeautifulSoup as bs
def get_security_context():
    # Ignore certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

def store_webpage(url, ctx, fn):
    page = urllib.request.urlopen(url, context=ctx)
    soup = bs(page.read(), 'html.parser')
    f = open(fn, 'w', encoding='utf-8')
    print(soup, file=f)
    f.close()

def load_webpage(url, ctx):
    page = urllib.request.urlopen(url, context=ctx)
    return bs(page.read(), 'html.parser')


def main():
    months_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    #months_dict allows you to convert three-letter month code to corresponding month number
    os.chdir(os.getcwd() + '/sites')
    ctx = get_security_context()
    url_list = ['https://www.lodgeroomhlp.com/','https://www.theroxy.com/events'] #contains sites to be scraped
    all_events_dict = {} #stores key:value pairs of date corresponding to event
    for url in url_list: #parses through all url's to be scraped
        web_url = url
        name = url.split("/")[2] #file name will only contain site name (i.e. theroxy.com)
        file_name = f'{name}_main.html'
        if not os.path.exists(file_name) or os.path.getsize(file_name) == 0: #downloads webpage if not already in sites directory
            store_webpage(web_url, ctx, file_name)
        file_url = 'file:///' + os.path.abspath(file_name)
        soup = load_webpage(file_url, ctx) #loads existing file to prevent security concerns on client end
        if url == url_list[0]: #If url corresponds to Lodge Room
            print("Concerts coming up at Lodge Room:")
            performance_cards = soup.find_all('div', class_ = 'tessera-show-card')
            for performance in performance_cards:
                date = performance.find('div', class_ = 'tessera-date').text.strip()
                event = performance.h4.text.strip()
                print('\t' + date)
                print('\t\t' + event)
                mon_day = date.split(',')[1].strip() #Obtains only month & day elements of date string
                date_seg  = mon_day.split(' ') #splits segment into month and day components
                month = months_dict[date_seg[0]]
                day = date_seg[1]
                if month not in ['10', '11', '12']: #assigns year depending on the event date (we can ascertain year since we are scraping the
                    #website in Oct 2023)
                    year = '2024'
                else:
                    year = '2023'
                date_value = int(year + month + day) #constructs an integer representation of the date
                date_tuple = (date, date_value) #stores both the string and integer representations of the date
                all_events_dict[date_tuple] = event + ' (Lodge Room)' #appends values to dict
            print()
        if url == url_list[1]: #If url corresponds to Roxy Theatre
            print("Concerts coming up at The Roxy Theatre:")
            event_info_block = soup.find_all('div', class_ = 'info')
            for info in event_info_block:
                date = info.find('span', class_ = 'date').text.strip()
                event = info.a.text.strip()
                print('\t' + date)
                print('\t\t' + event)
                mon_day = date.split(',')[1].strip() #Obtains only month & day elements of date string
                year = date.split(',')[2].strip() #since Roxy Theatre provides year, we can directly extract the value as well
                date_seg  = mon_day.split(' ')
                month = months_dict[date_seg[0]]
                day = date_seg[1]
                date_value = int(year + month + day)
                date_tuple = (date, date_value)
                all_events_dict[date_tuple] = event + ' (The Roxy Theatre)'
        print("All events sorted:")
        sorted_dates = sorted(all_events_dict.keys(), key = lambda date_tuple: date_tuple[1]) #sorts dict by integer represenations of dates
        for date in sorted_dates: #prints out all events in chronological order (regardless of venue)
            print('\t' + date[0])
            print('\t\t' + all_events_dict[date])

if __name__ == '__main__':
    main()
