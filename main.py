#required module  - pip install textblob
from textblob import TextBlob

#text that's spelling you want to  Correct 
text = " Progamminggg withh priyansh "

#Textblob function Saprate  the words from spaces,special symbol
correct = TextBlob(text)

#Correct method make the sentence correct
Correct = correct.correct()

#printing the correct sentence
print(Correct)