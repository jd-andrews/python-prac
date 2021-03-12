import random
from tkinter import *

root = Tk()
root.title('Navajo Code Translator')
root.geometry("450x200")

#Define navajo code dictionary
navajo_alphabet = {
    'a': ['wol-la-chee', 'be-la-sana', 'tse-nill'],
    'b': ['na-hash-chid', 'shush', 'toish-jeh'],
    'c': ['moasi', 'tla-gin', 'ba-goshi'],
    'd': ['be', 'chindi', 'lha-cha-eh'],
    'e': ['ah-jah', 'dzeh', 'ah-nah'],
    'f': ['chuo', 'tsa-e-donin-ee', 'ma-e'],
    'g': ['ah-tad', 'klizzie', 'jeha'],
    'h': ['tse-gah', 'cha', 'lin'],
    'i': ['tkin', 'yeh-hes', 'a-chi'],
    'j': ['tkele-cho-g', 'ah-ya-tsinne', 'yil-doi'],
    'k': ['jad-ho-loni', 'ba-ah-ne-di-tinin', 'klizzie-yazzie'],
    'l': ['dibeh-yazzie', 'ah-jad', 'nash-doie-tso'],
    'm': ['tsin-tliti', 'be-tas-tni', 'na-as-tso-si'],
    'n': ['tsah', 'a-chin', 'nesh-chee'], # site i referenced only had two words... separate site had 'nesh-chee'
    'o': ['a-kha', 'tlo-chin', 'ne-ahs-jah'],
    'p': ['cla-gi-aih', 'bi-so-dih', 'ne-zhoni'],
    'q': ['ca-yeilth'], # site I referenced only had one word
    'r': ['gah', 'dah-nes-tsa', 'ah-losz'],
    's': ['dibeh', 'klesh'], # site i referenced only had two words
    't': ['d-ah', 'a-woh', 'than-zie'],
    'u': ['shi-da', 'no-da-ih'], # site i referenced only had two words
    'v': ['a-keh-di-glini'], # site I referenced only had one word
    'w': ['gloe-ih'], # site I referenced only had one word
    'x': ['al-na-as-dzoh'], # site I referenced only had one word
    'y': ['tsah-as-zih'], # site I referenced only had one word
    'z': ['besh-do-tliz'] # site I referenced only had one word
}

#Initialize communication list
communication = []

#Function for converting user input to navajo code
def user_submission():
    word = word_entry.get()
    for letter in word:
        if letter in navajo_alphabet.keys():
            n_letter = navajo_alphabet[letter]
            communication.append(random.choice(n_letter))
        else:
            print("We do not store that letter.")
            break
    comm_disp = Label(root, text="The message to transmit is " + ' '.join(communication), font="Times")
    comm_disp.pack()

#Information for user input
word_request = Label(root, text="Enter the word that you would like encrypted")
word_request.pack(pady=10)

#Request for user input
word_entry = Entry(root, width=20, cursor="mouse")
word_entry.pack(pady=10, anchor=CENTER)

enter_button = Button(root, text="Submit", command=user_submission, cursor="spraycan")
enter_button.pack(pady=10)

#Binding Enter key to the Button
root.bind('<Return>', lambda event=None: enter_button.invoke())

root.mainloop()