from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

# Set your OpenAI GPT-3 API key
api_key = "my key"
client = OpenAI(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_response', methods=['POST'])
def generate_response():
    prompt = request.form['prompt']
    response = client.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        n=1
    )
    generated_text = response.choices[0].text.strip()
    return render_template('index.html', prompt=prompt, generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)


