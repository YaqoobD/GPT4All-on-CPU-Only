from pygpt4all.models.gpt4all import GPT4All

def new_text_callback(text):
    print(text, end="")

model = GPT4All(r'C:\Users\YaqoobDavid\OneDrive - WOW Tech Europe GmbH\Desktop\GPT4ALL_David\GPT4All-on-CPU-Only\models\gpt4all-converted.bin')
model.generate("Shawaiz is a good person, but ", n_predict=55, new_text_callback=new_text_callback)

