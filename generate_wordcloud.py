from wordcloud import WordCloud
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import numpy as np

stp = stopwords.words('english')
lem = WordNetLemmatizer()
wcloud = WordCloud(background_color='white',width=640, height=480)


# function to generate wordcloud
def generate_cloud(text):
    # remove characters which are not alphanumeric
    text = re.sub(r'[^\w\s]+', ' ', text)

    # remove stopwords
    text = ' '.join([word.lower() for word in text.split() if word not in stp])

    # lemmatize
    text = ' '.join([lem.lemmatize(word) for word in text.split()])

    # generate wordcloud
    wc = wcloud.generate(text)

    # Save wordcloud
    random_int = np.random.randint(500000)
    path = r'static/img/{}.jpg'.format(random_int)
    wc.to_file(path)
    #print("wordcloud.png saved successfully")
    return path


if __name__ == '__main__':
    text = '''This ain't a song for the broken-hearted
No silent prayer for the faith-departed
I ain't gonna be just a face in the crowd
You're gonna hear my voice
When I shout it out loud
It's my life
It's now or never
I ain't gonna live forever
I just want to live while I'm alive
(It's my life)
My heart is like an open highway
Like Frankie said
I did it my way
I just want to live while I'm alive
It's my life
This is for the ones who stood their ground
It's for Tommy and Gina who never backed down
Tomorrow's getting harder, make no mistake
Luck ain't enough
You've got to make your own breaks
It's my life
And it's now or never
I ain't gonna live forever
I just want to live while I'm alive
(It's my life)
My heart is like an open highway
Like Frankie said
I did it my way
I just want to live while I'm alive
It's my life
You better stand tall when they're calling you out
Don't bend, don't break, baby, don't back down
It's my life
And it's now or never
I ain't gonna live forever
I just want to live while I'm alive
(It's my life)
My heart is like an open highway
Like Frankie said
I did it my way
I just want to live while I'm alive
(It's my life)'''
    generate_cloud(text)