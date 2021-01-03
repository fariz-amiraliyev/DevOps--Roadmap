Parse HTML Code With Beautiful Soup

import requests
from bs4 import BeautifulSoup
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

Find Elements by ID

results = soup.find(id='ResultsContainer')
print(results.prettify())

Find Elements by HTML Class Name:

job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    print(job_elem, end='\n'*2)


for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(title_elem)
    print(company_elem)
    print(location_elem)
    print()


Extract Text From HTML Elements:

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    print(title_elem.text)
    print(company_elem.text)
    print(location_elem.text)
    print()

Find Elements by Class Name and Text Content:
python_jobs = results.find_all('h2', string='Python Developer')



python_jobs = results.find_all('h2',
                               string=lambda text: "python" in text.lower())

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")
