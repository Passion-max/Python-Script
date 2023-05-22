import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse

# Define the URL of the directory listing
url = 'https://labartisan.net/anfizreactdarkone/'

# Define the destination folder where the files will be saved
dest_folder = r'C:\Users\user\Downloads\NFT FILE'

# Create the destination folder if it doesn't exist
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# Define the file extensions to download
extensions = ['.css', '.zip', '.html', '.js', '.json']

# Define a function to recursively download the contents of subdirectories using Selenium
def download_url_recursive(url, folder, driver):
    driver.get(url)
    html = driver.page_source
    for line in html.split('\n'):
        if line.startswith('<a href="'):
            filename = line[9:line.index('"', 9)]
            full_url = f'http://{hostname}{urlparse(url).path}/{filename}'
            if filename.endswith('/'):
                subfolder = os.path.join(folder, filename[:-1])
                os.makedirs(subfolder, exist_ok=True)
                print(f'Downloading contents of {full_url} to {subfolder}')
                download_url_recursive(full_url, subfolder, driver)
            else:
                ext = os.path.splitext(filename)[1]
                if ext in extensions:
                    print(f'Downloading {full_url} to {folder}')
                    driver.get(full_url)
                    file_path = os.path.join(folder, filename)
                    with open(file_path, 'wb') as f:
                        f.write(driver.page_source.encode())
                    print(f'Downloaded {full_url} to {file_path}')

# Set up the Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument('--headless') # run Chrome in headless mode
driver = webdriver.Chrome(options=chrome_options)

# Parse the URL to get the hostname and path
parsed_url = urlparse(url)
hostname = parsed_url.hostname
path = parsed_url.path

# Download the contents of the root folder
download_url_recursive(url, dest_folder, driver)

# Close the Selenium WebDriver
driver.quit()
