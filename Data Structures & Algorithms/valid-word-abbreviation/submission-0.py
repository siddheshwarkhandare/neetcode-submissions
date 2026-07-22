class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j=0,0
        while i< len(word) and j< len(abbr): # this check if till the string end
            if word[i] == abbr[j]:# if i and j is same increment
                i+=1
                j+=1
            elif abbr[j].isalpha() or abbr[j]=="0": # is j isalpha  return False and it is 0 return False
                return False
            else:
                le=0
                while j< len(abbr) and not abbr[j].isalpha(): # here we are checking if given
                    le=le*10 + int(abbr[j])                   # lests supose the first is 4 
                    j+=1                                      # multipy with 10 = 40 and adding j(5) = 45
                i+=le

        return i==len(word) and j==len(abbr) #true if both len same
        #  to check the given abbr no we use isalpha() function 
        #