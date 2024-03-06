nums=[3,2,3]
class Solution:
    def majorityElement():
        occurences={}
        for element in nums:
            if element in occurences:
                occurences[element] +=1
            else:
                occurences[element] =1
        maj_element=max(occurences, key=occurences.get)
        return maj_element
    
''' I approached the solution without thinking about the n/2 condition
But still this solution using my hash map technique has a time complexity of O(n)'''