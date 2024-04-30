from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()  # Or use any other WebDriver like Firefox WebDriver

df = pd.read_excel('Test.xlsx')  # Replace 'your_excel_file.xlsx' with the path to your Excel file
url2_list = df['DemoURL'].tolist()

# Load the login page
url = "https://admin.mymedisage.com/"
driver.get(url)

# Wait for the page to load
time.sleep(2)  # Adjust the sleep time as needed

# Find the email and password input fields and fill them with your credentials
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "userpassword")

# Replace 'your_email' and 'your_password' with your actual email and password
email_input.send_keys("lp2204")
password_input.send_keys("Lp@2204")

# Submit the form (you may need to locate the submit button and click it)
password_input.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(5)  # Adjust the sleep time as needed

data_list = []
# Now you can navigate to the desired page and scrape the content
# For example:

for url2 in url2_list:
    # Navigate to the dynamic URL
    driver.get(url2)
    
    time.sleep(1)  # Wait for the page to load

    # Get the page source after JavaScript execution
    html_content = driver.page_source

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Now you can access the body content
    body_content = soup.body

    # Define CSS selectors for the desired <td> tags
    selectors = [
        'td[aria-colindex="1"][role="cell"]',
        'span.email-word-break',
        'td[aria-colindex="3"][role="cell"].w-300',
        'td[aria-colindex="4"][role="cell"]',
        'td[aria-colindex="5"][role="cell"]',
        'td[aria-colindex="6"][role="cell"]',
        'td[aria-colindex="7"][role="cell"]'
    ]
    row_data = []


    # Select and print the text content of each <td> tag
    for selector in selectors:
        td_tags = soup.select(selector)
        if td_tags:
            for td_tag in td_tags:
                print(td_tag.text.strip())
                row_data.append(td_tag.text.strip())
        # else:
        #     print(f"No matching elements found for selector: {selector}")
    data_list.append(row_data)

headers = ["ID", "Name", "Designation", "Phone", "Email", "City", "Country"]
df = pd.DataFrame(data_list, columns=headers)

# Export DataFrame to Excel file
df.to_csv("scraped_data.csv", index=False)

# Don't forget to close the WebDriver when you're done
driver.quit()