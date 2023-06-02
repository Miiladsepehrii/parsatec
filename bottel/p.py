from telethon.sync import TelegramClient

api_id = '26616577'
api_hash = 'b84c63aa98e2c8ee0ee09494f694382b'
phone_number = '+989389232279'
message = 'Hello, this is a test message.'

with TelegramClient('session_name', api_id, api_hash) as client:
    client.send_message(phone_number, message)
