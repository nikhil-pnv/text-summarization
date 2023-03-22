from flask import Flask,  render_template, request 
from textsum import summarizer, to_eng, text_translate
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
    x=destlang 
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


if __name__ == "__main__":
    app.run(debug=True)

                        