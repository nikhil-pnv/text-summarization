from flask import Flask, jsonify,  render_template, request
import json   
from textsum import summarizer, to_eng, text_translate
import openai
import gradio as gr
import re
from gtts import gTTS
import os



app = Flask(__name__)
sum = '' 
destlang= ''
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/analyze", methods=['GET','POST'])
def analyze():
    global sum
    global destlang
    if request.method == 'POST':
        rawtext = request.form['rawtext'] 
        srclang = request.form['sourcelang']
        destlang = request.form['Translateinto']
        rawtext = to_eng(rawtext, srclang)
        sum,txt,txt_len,sum_len=summarizer(rawtext)
        txt=  text_translate(txt,srclang)
        sum= text_translate(sum,destlang)
        txt_len= len(txt)
        sum_len=len(sum)
    else:
        txt = ''
        txt_len = 0   
        sum_len = 0
    return render_template('summary.html', summary=sum,original_txt= txt, text_length=txt_len,summary_length= sum_len, lang = destlang)
 
@app.route('/speak', methods=['POST'])
def speak():
    global sum
    global destlang
    desttxt = None
    print(destlang)
    if destlang=="Hindi":
        desttxt= 'hi'
    if destlang == "English":
        desttxt= 'en'
    if destlang == "Telugu":
        desttxt ='te'
    if destlang == 'Tamil':
        desttxt = 'ta'
    if destlang == 'Bengali':
        desttxt = 'bn'
    if destlang == "Arabic":
        desttxt = 'ar'
    if destlang == 'Chinese':
        desttxt = 'zh-TW'
    if destlang == 'French':
        desttxt = 'fr'
    if destlang == 'German':
        desttxt = 'de'
    
    text_to_speech = gTTS(text=sum, lang=desttxt, slow=False)
    text_to_speech.save('test.mp3')
    os.system('test.mp3')
    return ''

openai.api_key = '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'

def generate_message(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1025,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n", "Human:", "AI:"]
    )
    message = response.choices[0].text.strip()
    return message

@app.route("/chatbot", methods=['GET','POST'])
def chatbot():
    return render_template('chatbot.html')


@app.route('/api/chatbot', methods=['POST'])
def chatbot_api():
    data = json.loads(request.data)
    prompt = data['message']
    message = generate_message(prompt)
    print(message)
    return jsonify({'message': message})



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

                        
