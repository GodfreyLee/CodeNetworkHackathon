from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from openai import OpenAI
from chat_response import response
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key, organization="org-cly0EyGAP6X8i6pFqGqL5bN0")

recipient = 'Bae'
recipient_number = '+61493969310'
talking_style="You are talking to with your girlfriend, and just reply a single sentence each time"

# Initialize the Chrome driver
driver = webdriver.Chrome()  # or specify the path: webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Wait for the user to scan the QR code
print("Please scan the QR code to log in.")
time.sleep(20)  # Adjust this as necessary

# Function to retrieve messages from a specific chat
def get_messages(chat_name):
    # Search for the chat by name
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.send_keys(Keys.COMMAND, 'a')  # For macOS
    search_box.send_keys(Keys.DELETE)
    search_box.send_keys(chat_name)
    time.sleep(2)  # Wait for the search results to appear

    # Click on the chat
    chat = driver.find_element(By.XPATH, f'//span[@title="{chat_name}"]')
    chat.click()

    # Wait for the chat to load
    time.sleep(2)

    # Retrieve messages
    messages = driver.find_elements(By.XPATH, '//span[@class="_ao3e selectable-text copyable-text"]')
    new_messages = []
    for message in messages:
        new_messages.append(message.text)

    return new_messages

# Example usage: Retrieve messages from a chat named 
original_messages = get_messages(recipient)

#ChatGPT Prompt messages
chat_messages = [
                    {"role": "system", "content": talking_style},
                ]

while True:
    time.sleep(5)
    current_messages = get_messages(recipient)

    # Check for new messages
    if current_messages and current_messages[-1] != original_messages[-1]:
        if current_messages[-1] != response.choices[0].message.content:
            # Generate Message from ChatGPT
            print(current_messages[-1])
            chat_messages.append({"role": "user", "content": current_messages[-1]})
            print(chat_messages)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=chat_messages
            )
            print(response)
            chat_messages.append({"role": "assistant", "content": response.choices[0].message.content})
            # Send the response
            message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@class="x1hx0egp x6ikm8r x1odjw0f x1k6rcq7 x6prxxf"]')
            message_box.click()
            print(response.choices[0].message.content)
            message_box.send_keys(response.choices[0].message.content)
            message_box.send_keys(Keys.ENTER)
              
    original_messages = current_messages
