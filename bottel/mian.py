import requests
import random
import time
from datetime import datetime

# Set your bot token and chat ID
bot_token = 'your_bot_token'
chat_id = 'your_chat_id'

# Define the time range for sending messages (in 24-hour format)
start_time = '05:00'
end_time = '22:00'

# List of random messages
messages = [
    'Hello there!',
    'How are you today?',
    'Just sending a random message.',
    'Hope you have a great day!',
    'Random message of the day.'
]

# List of voice messages
voice_messages = [
    'voice1.ogg',
    'voice2.ogg',
    'voice3.ogg'
]

# List of photo file paths
photos = [
    'photo1.jpg',
    'photo2.jpg',
    'photo3.jpg'
]

# Function to send a text message
def send_text_message(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, json=params)
    if response.status_code == 200:
        print('Text message sent successfully.')
    else:
        print(f'Failed to send text message. Error: {response.status_code} - {response.text}')

# Function to send a voice message
def send_voice_message(voice_file):
    url = f'https://api.telegram.org/bot{bot_token}/sendVoice'
    params = {
        'chat_id': chat_id
    }
    files = {
        'voice': open(voice_file, 'rb')
    }
    response = requests.post(url, params=params, files=files)
    if response.status_code == 200:
        print('Voice message sent successfully.')
    else:
        print(f'Failed to send voice message. Error: {response.status_code} - {response.text}')

# Function to send a photo
def send_photo(photo_file):
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    params = {
        'chat_id': chat_id
    }
    files = {
        'photo': open(photo_file, 'rb')
    }
    response = requests.post(url, params=params, files=files)
    if response.status_code == 200:
        print('Photo sent successfully.')
    else:
        print(f'Failed to send photo. Error: {response.status_code} - {response.text}')

# Function to check if the current time is within the specified range
def is_within_time_range(start, end):
    current_time = datetime.now().strftime('%H:%M')
    return start <= current_time <= end

# Main function to run the bot
def run_bot():
    while True:
        if is_within_time_range(start_time, end_time):
            # Randomly select a message type to send
            message_type = random.choice(['text', 'voice', 'photo'])
            
            if message_type == 'text':
                # Send a random text message
                message = random.choice(messages)
                send_text_message(message)
            elif message_type == 'voice':
                # Send a random voice message
                voice_file = random.choice(voice_messages)
                send_voice_message(voice_file)
            elif message_type == 'photo':
                # Send a random photo
                photo_file = random.choice(photos)
                send_photo(photo_file)

        # Delay for 1 minute before checking the time again
        time.sleep(60)

# Run the bot
run_bot()
