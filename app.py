from flask import Flask, request, jsonify, render_template
import cohere

app = Flask(__name__)
co = cohere.Client("1MKARbZfa1UhWBbJJs6q3WuGpdjS2E42q9HpsQrz") 

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Chat API
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('prompt')
    try:
        response = co.chat(
            model="command-r-plus",
            message=user_input,
        )
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
