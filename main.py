from thinker import *

window = Tk()
window.title('THinker sample window')
window geometry('300x300')

greeting = label(text="Hello users", fg='black', bg='white')
button = Button(text="click me",bg='black', fg='white')
entry = Entry()