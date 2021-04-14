#You have been recruited by your friend, a linguistics enthusiast, to create a utility tool that can perform analysis on a given piece of text. Complete the class 'analysedText' with the following methods -

#Constructor - Takes argument 'text',makes it lower case and removes all punctuation. Assume only the following punctuation is used - period (.), exclamation mark (!), comma (,) and question mark (?). Store the argument in "fmtText"
#freqAll - returns a dictionary of all unique words in the text along with the number of their occurences.
#freqOf - returns the frequency of the word passed in argument.

class analysedText(object):
    
    def __init__ (self, text):
        self.text = text
        text = text.lower()
        fmtText = ''
        for i, elem in enumerate(text):
            if elem in ['.', '!', ',', '?']:
                text = text.replace(elem,'')
            fmtText = text
        print(fmtText)
            
                
    
    def freqAll(self):        
        D = {}
        L = self.text.split(' ')
        for i, elem in enumerate(L):
            nr_ap = L.count(elem)
            D[elem] = nr_ap
        return(D)
    
    def freqOf(self,word):
        freqDict = self.freqAll()
        if word in freqDict:
            return word
        else:
            return None
