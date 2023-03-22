from transformers import PegasusForConditionalGeneration, PegasusTokenizer 
from googletrans import Translator  

tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

def to_eng(rawdocs, lang):
    translator = Translator()
    if lang=="Hindi":
        desttxt= 'hi'
    if lang == "English":
        desttxt= 'en'
    if lang == "Telugu":
        desttxt ='te'
    if lang == 'Tamil':
        desttxt = 'ta'
    if lang == 'Bengali':
        desttxt = 'bn'
    if lang == "Arabic":
        desttxt = 'ar'
    if lang == 'Chinese':
        desttxt = 'zh-TW'
    if lang == 'French':
        desttxt = 'fr'
    if lang == 'German':
        desttxt = 'de'
    output_text = translator.translate(rawdocs, src=desttxt, dest='en')

    return output_text.text
        
def text_translate(rawdocs, lang):
    translator = Translator()
    if lang=="Hindi":
        desttxt= 'hi'
    if lang == "English":
        desttxt= 'en'
    if lang == "Telugu":
        desttxt ='te'
    if lang == 'Tamil':
        desttxt = 'ta'
    if lang == 'Bengali':
        desttxt = 'bn'
    if lang == "Arabic":
        desttxt = 'ar'
    if lang == 'Chinese':
        desttxt = 'zh-TW'
    if lang == 'French':
        desttxt = 'fr'
    if lang == 'German':
        desttxt = 'de'
    output_text = translator.translate(rawdocs, src='en', dest=desttxt)

    return output_text.text



def summarizer(rawdocs):


    tokens = tokenizer(rawdocs, truncation=True, padding="longest", return_tensors="pt")
    #print(tokens)
    summary = model.generate(**tokens)
    #print(summary)
    res=tokenizer.decode(summary[0])
    res=res[5:-4]
    cnt=0
    for i in res:
        if i !=" ":
            cnt+=1
    return res,rawdocs,len(rawdocs.split(' ')),cnt     

