import pandas as pd

# Read the Excel file
df = pd.read_excel('Test.xlsx')

# List all column names
print("Column names:", df.columns)

# Select the appropriate column containing the URLs
# url2_list = df['Column_Name_Containing_URLs'].tolist()  # Replace 'Column_Name_Containing_URLs' with the actual column name

# # Now you can iterate through url2_list and scrape data for each URL
# for url2 in url2_list:
#     # Your scraping code here, using 'url2'
#     print(url2)
