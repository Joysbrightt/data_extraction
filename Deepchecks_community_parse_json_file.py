# import json
#
#
# # Example function to parse JSON data from a file
# def parse_data_from_file(filename):
#     with open(filename, 'r') as file:
#         data = json.load(file)
#     return data
#
#
# # Example function to parse JSON data from a string (e.g., API response)
# def parse_data_from_string(data_string):
#     data = json.loads(data_string)
#     return data
#
#
# # Replace 'your_data_file.json' with the path to your actual data file
# data_from_file = parse_data_from_file('your_data_file.json')
# print(data_from_file)
#
# # Assuming 'api_response' is a string containing JSON data from an API
# api_response = '{"name": "John", "age": 30, "city": "New York"}'
# data_from_string = parse_data_from_string(api_response)
# print(data_from_string)
#
#
# import json
#
# # Load JSON data from file
# with open('Arize_AI_json_result.json', 'r') as file:
#     data = json.load(file)
#
# # Extract relevant information from each item
# for item in data['items']:
#     profile = item['profile']
#     firstname = profile.get('first_name', '')  # Get firstname if available, otherwise set to empty string
#     lastname = profile.get('last_name', '')  # Get lastname if available, otherwise set to empty string
#     email = profile.get('email', '')  # Get email if available, otherwise set to empty string
#     company_name = profile.get('company', '')  # Get company name if available, otherwise set to empty string
#
#     # Print or use extracted information as needed
#     print(f"Firstname: {firstname}, Lastname: {lastname}, Email: {email}, Company: {company_name}")


# import json
# import pandas as pd
#
# # Load JSON data from file
# with open('Arize_AI_json_result.json', 'r') as file:
#     data = json.load(file)
#
# # Create lists to store extracted information
# firstnames = []
# lastnames = []
# emails = []
# company_names = []
#
# # Extract relevant information from each item
# for item in data['items']:
#     profile = item['profile']
#     firstnames.append(profile.get('first_name', ''))  # Get firstname if available, otherwise set to empty string
#     lastnames.append(profile.get('last_name', ''))  # Get lastname if available, otherwise set to empty string
#     emails.append(profile.get('email', ''))  # Get email if available, otherwise set to empty string
#     company_names.append(profile.get('company', ''))  # Get company name if available, otherwise set to empty string
#
# # Create a DataFrame using the extracted information
# df = pd.DataFrame({
#     'Firstname': firstnames,
#     'Lastname': lastnames,
#     'Email': emails,
#     'Company': company_names
# })
#
# # Save the DataFrame to a CSV file
# df.to_csv('profile_info.csv', index=False)
#
# print("Data saved to profile_info.csv")


import json
import pandas as pd

# Load JSON data from file
with open('Arize_AI_json_result.json', 'r') as file:
    data = json.load(file)

# Create lists to store extracted information
firstnames = []
lastnames = []
emails = []
company_names = []

# Extract relevant information from each item
for item in data['items']:
    profile = item['profile']
    firstnames.append(profile.get('first_name', ''))  # Get firstname if available, otherwise set to empty string
    lastnames.append(profile.get('last_name', ''))  # Get lastname if available, otherwise set to empty string
    emails.append(profile.get('email', ''))  # Get email if available, otherwise set to empty string
    company_names.append(profile.get('company', ''))  # Get company name if available, otherwise set to empty string

# Create a DataFrame using the extracted information
df = pd.DataFrame({
    'Firstname': firstnames,
    'Lastname': lastnames,
    'Email': emails,
    'Company': company_names
})

# Save the DataFrame to a CSV file
df.to_csv('profile_info2.csv', index=False)

print("Data saved to profile_info2.csv")
