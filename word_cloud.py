# import wordcloud and matplotlib libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Intialize the Paragraph
text = '''Hi, I am a student of Computer Science and Engineering.
          My name is Vishwas.
          How are you feeling today?
          I hope you are having a good day.
          '''

# Create a WordCloud object
wordcloud = WordCloud().generate(text)

# Display the word cloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()