from flask import Flask, request, render_template
import subprocess
import os

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET', 'POST'])
def index():
    print(os.listdir())
    if request.method == 'POST':
        input_text = request.form['input_text']
        
        # Call chain-of-density code
        result = subprocess.run(['python', 'main.py', input_text], 
                                stdout=subprocess.PIPE).stdout
        
        output = result.decode('utf-8')
        
        return render_template('index.html', input_text=input_text, output=output)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()