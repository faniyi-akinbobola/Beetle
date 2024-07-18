from flask import Flask, request, jsonify  # Import Flask for web app development
from ultrabot import ultraChatBot  # Import the ultraChatBot class from another module

# Initialize a Flask application instance
app = Flask(__name__)

@app.route('/', methods=['POST'])  # Define a route for the root path '/' that accepts POST requests
def home():
    if request.method == 'POST':  # Check if the request method is POST
        try:
            # Parse the JSON data from the request body
            data = request.json

            # Create an instance of the ultraChatBot class with the parsed JSON data
            bot = ultraChatBot(data)

            # Process incoming messages using the bot's Processing_incoming_messages function
            response = bot.Processing_incoming_messages()

            # Return the response from the bot as JSON data
            return jsonify(response)
        except Exception as e:  # Handle any exceptions during processing
            print(f"An error occurred: {e}")
            return jsonify({'error': 'Something went wrong'}), 500  # Return an error response

if __name__ == '__main__':
    # Run the Flask development server
    app.run()
