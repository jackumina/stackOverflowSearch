import requests
import json

import ipywidgets as widgets

# gets the request from the stackexchange server
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# Create an output widget to display the result
output = widgets.Output()

# Create a text widget for the search bar
search_bar = widgets.Text(
    value='',
    placeholder='Ask a question',
    description='Search:',
    disabled=False
)

# Define a function to handle the search input
# change is the dictionary passed, containing details about the change event.
def handle_search(change):
    with output:
        output.clear_output()
        # change['new'] accesses the value associated with the key 'new' in the change dictionary 
        # This key holds the value attribute of the search_bar widget
        search_value = change['new']
        
        # loop through json data and print the link if the text to a question
        # entered in the search bar matches text in a question
        for data in response.json()['items']:
          # if text in bar is a substring of a question
          # print question and link to answer
          if search_value.upper() in data['title'].upper():
            print(data['title'])
            print(data['link'])
            print()

# Whenever the value in the search bar changes call the handle_search function
# Register a callback function to be executed whenever value is changed (typing occurs)
search_bar.observe(handle_search, names='value')

# Display the widgets
display(search_bar, output)