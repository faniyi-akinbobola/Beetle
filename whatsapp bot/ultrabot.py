import json
import requests
import datetime

"""
This class defines an UltraMsg chatbot that can send messages, images, videos, audio,
    voice notes, and contacts through the UltraMsg API.
"""
class ultraChatBot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['data']
        self.ultraAPIUrl = "https://api.ultramsg.com/instance89980/"
        self.token = 'qdsptrbmkpn4edp3'

    #Sends a POST request to the UltraMsg API with the specified type and data.
    def send_requests(self, type, data):
        url = f"{self.ultraAPIUrl}{type}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    #Sends a text message to the specified chat ID.
    def send_message(self, chatID, text):
        data = {"to" : chatID,
                "body" : text}  
        answer = self.send_requests('messages/chat', data)
        return answer

    #Sends an image to the specified chat ID using a provided URL.
    def send_image(self, chatID):
        data = {"to" : chatID,
                "image" : "https://file-example.s3-accelerate.amazonaws.com/images/test.jpeg"}  
        answer = self.send_requests('messages/image', data)
        return answer

    #Sends a video to the specified chat ID using a provided URL.
    def send_video(self, chatID):
        data = {"to" : chatID,
                "video" : "https://file-example.s3-accelerate.amazonaws.com/video/test.mp4"}  
        answer = self.send_requests('messages/video', data)
        return answer
    
    #Sends an audio file to the specified chat ID using a provided URL.
    def send_audio(self, chatID):
        data = {"to" : chatID,
                "audio" : "https://file-example.s3-accelerate.amazonaws.com/audio/2.mp3"}  
        answer = self.send_requests('messages/audio', data)
        return answer

    #Sends a voice note to the specified chat ID using a provided URL.
    def send_voice(self, chatID):
        data = {"to" : chatID,
                "audio" : "https://file-example.s3-accelerate.amazonaws.com/voice/oog_example.ogg"}  
        answer = self.send_requests('messages/voice', data)
        return answer

    #Sends a predefined contact information to the chat.
    def send_contact(self, chatID):
        data = {"to" : chatID,
                "contact" : "+(234)20961839.ng"}  
        answer = self.send_requests('messages/contact', data)
        return answer

    #Gets the current date and time and sends it as a message to the chat.
    def time(self, chatID):
        t = datetime.datetime.now()
        time = t.strftime('%Y-%m-%d %H:%M:%S')
        return self.send_message(chatID, time)

    #Sends a welcome message or a list of available commands to the chat.
    def welcome(self,chatID, noWelcome = False):
        welcome_string = ''
        if (noWelcome == False):
            welcome_string = "Hi , welcome to my first WhatsApp chatbot using Python\n"
        else:
            welcome_string = """wrong command
Please type one of these commands:
*hi* : Saluting
*time* : show server time
*image* : I will send you a picture
*video* : I will send you a Video
*audio* : I will send you a audio file
*voice* : I will send you a ppt audio recording
*contact* : I will send you a contact
"""
        return self.send_message(chatID, welcome_string)


    #Processes incoming messages from the chat.
    #If there are no messages, the function returns the string 'NoCommand'.
    def Processingـincomingـmessages(self):
        if self.dict_messages != []:
            message =self.dict_messages
            text = message['body'].split()
            if not message['fromMe']:
                chatID  = message['from'] 
                if text[0].lower() == 'hi':
                    return self.welcome(chatID)
                elif text[0].lower() == 'time':
                    return self.time(chatID)
                elif text[0].lower() == 'image':
                    return self.send_image(chatID)
                elif text[0].lower() == 'video':
                    return self.send_video(chatID)
                elif text[0].lower() == 'audio':
                    return self.send_audio(chatID)
                elif text[0].lower() == 'voice':
                    return self.send_voice(chatID)
                elif text[0].lower() == 'contact':
                    return self.send_contact(chatID)
                else:
                    return self.welcome(chatID, True)
            else: return 'NoCommand'
