import requests
from bs4 import BeautifulSoup
import csv

# Create a CSV file to save the results
csv_file = open('trustedshops_companies.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company Name', 'URL', 'Logo URL', 'Description', 'Category'])

# Loop through multiple pages to scrape all companies
page_num = 1
while True:
    url = f'https://www.trustedshops.de/bewertung/info_X{page_num}.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    companies = soup.find_all('div', class_='tsRating__company')
    if not companies:
        break

    for company in companies:
        company_name = company.find('h2').text.strip()
        url = company.find('a')['href']
        logo_url = company.find('img')['src']
        description = company.find('p').text.strip()
        category = company.find('span', class_='tsRating__company-category').text.strip()

        csv_writer.writerow([company_name, url, logo_url, description, category])

    page_num += 1

csv_file.close()
