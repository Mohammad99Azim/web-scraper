from random import randint
import requests
from bs4 import BeautifulSoup
import time


def get_citations_needed_report():
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    all_paragraph = soup.find_all('p')

    all_ready_to_print = ""
    for paragraph in all_paragraph:
        whole_p = ""
        for x in paragraph:
            the_text = x.get_text().strip()
            whole_p += the_text
        if "[citation needed]" in whole_p:
            all_ready_to_print += whole_p
            all_ready_to_print += "\n" + ("*" * 50) + "\n"
        time.sleep(randint(1, 3))  # You Can Remove it to make the process faster
    return all_ready_to_print


def get_citations_needed_count():
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    all_paragraph = soup.find_all('p')
    count = 0
    for paragraph in all_paragraph:
        if "citation needed" in str(paragraph):
            count += 1
        time.sleep(randint(1, 3))  # You Can Remove it to make the process faster
    return count


print(get_citations_needed_report())

print(get_citations_needed_count())


# with open('paragraphs.txt', 'w') as file:
#     file.write(get_citations_needed_report())
