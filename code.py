import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL of the webpage with the table
url = "https://educationdata.org/college-enrollment-statistics"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')


# Find the first table (you can fine-tune the selection)
table = soup.find('table', {'class': 'table-responsive-mobile'})

# Extract the table headers
headers = [th.text.strip() for th in table.find_all('th')]

# Extract the table rows (skipping the header)
rows = []
# Skip the header row
for row in table.find_all('tr')[1:]: 
    cells = [cell.text.strip() for cell in row.find_all('td')]
    rows.append(cells)

# Create the DataFrame
df = pd.DataFrame(rows, columns=headers)

print(df)
