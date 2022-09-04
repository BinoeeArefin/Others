from cgitb import text
from pydoc import pager
import pyttsx3
import PyPDF2
book = open('Harry Potter.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
current = 12
print('what page do you want to start from?')
speaker = pyttsx3.init()
for num in range(current,pages):
    page = pdfReader.getPage(current)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    current +=1