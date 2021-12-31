from flask import Flask, render_template
import platform, os

# Note: This app is using for demonstration purpose
#       And all configuration are set as Development
#       Please do not use it for Production env
app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def main():
    greeting_quote = os.getenv('GREETING_QUOTE', 'Not my words, baby!')
    machine_name = platform.node()
    return render_template('hello.html', machine_name=machine_name, greeting_quote=greeting_quote)

@app.route('/ping', methods=['GET'])
def health_check():
    return "pong!"

if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'  # HARD CODE since default is production
    app.run(host='0.0.0.0', port=105, debug=True)
