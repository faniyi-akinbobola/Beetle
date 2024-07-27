# UltraChatBot: A Python Wrapper for UltraMSG API
This is the README file for UltraChatBot, a Python class that allows you to interact with the UltraMSG API and send messages, images, videos, and other media to WhatsApp chats.

## Features
Sends text messages to WhatsApp chats.
Sends images, videos, audio files, voice notes, and contacts.
Retrieves the current server time.
Welcomes users with a customizable message.
Processes incoming messages and responds based on user commands.

## Requirements
Python 3.x
Libraries:
- requests
- datetime

## Installation
Make sure you have Python 3 and the required libraries installed. You can install them using pip:

1. Bash
`pip install requests`
Use code with caution.

2. Replace the placeholder values in the code:

'sv5jrvomb98t73i3' with your UltraMSG API token. You can obtain a token by creating an account on UltraMSG.
Update the example URLs for media content (image, video, audio, voice) with your own media files hosted publicly.

3.Save the code as ultraChatBot.py.

## Usage
Import the ultraChatBot class in your Python script:

1. Python
`from ultraChatBot import ultraChatBot`
Use code with caution.

2. Load your initial data (optional) in JSON format and pass it to the class constructor:

Python
## Example JSON data with a sample message
`data = {'data': [{'fromMe': False, 'from': '123456789012@c.us', 'body': 'Hi!'}]}`
Use code with caution.

Python
## Initialize the chatbot instance
`chatbot = ultraChatBot(data)`
Use code with caution.

Use the available methods to interact with the UltraMSG API:

- send_message(chatID, text): Sends a text message to a specific chat (identified by its chat ID).
- send_image(chatID): Sends an image from a provided URL (replace the example URL).
- send_video(chatID): Sends a video from a provided URL (replace the example URL).
- send_audio(chatID): Sends an audio file from a provided URL (replace the example URL).
- send_voice(chatID): Sends a voice note from a provided URL (replace the example URL).
- send_contact(chatID): Sends a contact from a provided phone number (replace with a valid number).
- time(chatID): Retrieves the current server time and sends it to a chat.
- welcome(chatID, noWelcome=False): Sends a welcome message to a chat, with an option to display a list of available commands upon receiving an unrecognized command.

## Processing Incoming Messages
The Processingـincomingـmessages method demonstrates a basic example of processing incoming messages based on user commands. It parses the message text, identifies the chat ID, and responds accordingly. You can modify and extend this logic to implement more complex message handling functionalities.

## License
This project is provided without an explicit license. Please use it responsibly and consider obtaining the necessary permissions for commercial use.

## Note
Be aware of usage limits and costs associated with the UltraMSG API. Refer to their documentation for details.
The provided example URLs for media content are placeholders. Replace them with your own publicly accessible media files.
