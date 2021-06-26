"""
File: marketcap_ext.py
Name: Cage

This project is to retrieve the 100 largest companies from the world first and present their market cap each year.
Users can search companies name in entry to find their stock tickers.
Then use the stock ticker to find the market cap of each year.
Because it crawl through 100 pages, it would take 3~4 minutes to get all data...
# if adjust the url, this code can be used to get all revenue and earnings data as well.
"""


import requests
from bs4 import BeautifulSoup

name_list = []
ticker_list = []
link_list = []
# eg. {'AAPL':{'2021': 2000}}
cap_d = {}
# eg. {'Apple':'AAPL'}
code_d = {}


def main():
    get_cap()


def get_cap():
    # retrieve the 100 largest companies list (by market capitalization(Billion))
    url = 'https://companiesmarketcap.com/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html)
    items = soup.find_all('td', {'class': 'name-td'})
    for item in items:
        company_link = item.a['href']
        company_name = item.a.text.replace(' ', '-').split()[0].replace('-', ' ')
        company_name = company_name[1:].replace(' ', '')
        company_ticker = item.a.text.replace(' ', '-').split()[1]
        name_list.append(company_name)
        ticker_list.append(company_ticker)
        link_list.append(company_link)
        cap_d[company_ticker] = {}
        code_d[company_name] = company_ticker
    # Go to each company's page to get its data.
    for i in range(len(link_list)):
        cap_url = 'https://companiesmarketcap.com' + link_list[i]
        cap_response = requests.get(cap_url)
        cap_html = cap_response.text
        cap_soup = BeautifulSoup(cap_html)
        data = cap_soup.find_all('td', {'class': ''})
        year = []
        cap = []
        for j in range(len(data)):
            # process data from pages
            data[j] = str(data[j]).replace(' ', '')
            data[j] = data[j].replace('<td>', '')
            data[j] = data[j].replace('</td>', '')
            data[j] = data[j].replace('$', '')
            # remove Trillion and Billion
            if 'T' in data[j]:
                data[j] = float(data[j].replace('T', '')) * 1000
            elif 'B' in data[j]:
                data[j] = float(data[j].replace('B', ''))

            if type(data[j]) == str and data[j] != '':
                year.append(data[j])
            elif type(data[j]) == float and data[j] != '':
                cap.append(data[j])
        # Append data to the dictionary
        for n in range(len(year)):
            cap_d[ticker_list[i]][year[n]] = cap[n]
    return cap_d, code_d


def search_names(target, ticker_data):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        ticker_data (dict): a dict containing company tickers data organized by company name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    name_l = target.lower()
    tickers = []
    for name in ticker_data:
        if name_l in name.lower():
            tickers.append(ticker_data[name])
    return tickers


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


if __name__ == '__main__':
    main()
