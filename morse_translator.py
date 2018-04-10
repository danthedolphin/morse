alphabet = [chr(x) for x in range(97,123)] #put a-z in a list
code = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
morse = dict(zip(alphabet,code)) #map the two lists into a dictionary

while True:

    msg = str(raw_input('What is your message?\n'))
    msg = msg.replace(' ','').replace('.','').replace('-','').replace(';','').replace('?','').lower() #get rid of the commas periods and make everything lowercase
    key = ''

    for x in msg:
        key = key + morse[x] + '/'
    print key
    repeat = raw_input("Do you have another message? y/n\n")

    if repeat == 'n':
        break
    else:
        continue
