###############################################################################
# Name        : check_palindrome.cpp
# Author      : VEF Academy
# Version     :
# Copyright   : Your copyright notice
# Description : Check if a string is a permutation of a palindrome, Ansi-style
###############################################################################

# Constant strings
EMPTY_STRING = "String is empty!"
INVALID_CHARS = "Invalid characters!"
STRING_TOO_LONG = "String is too long!"
YES = "Yes"
NO = "No"

class Problem5():
  # Method to be implemented
  def checkPalindrome(self, s):
    # Your implementation goes here
    pass

  # Method to score
  def score(self):
    # vector of scores for all the tests
    scoreList = list()
    
    # test cases
    testCase = {
                # Test 1 -- Empty string
                ""        : EMPTY_STRING,  \
                # Test 2 -- Invalid characters
                "$mm"     : INVALID_CHARS, \
                # Test 3 -- String is too long
                "The quick brown fox jumps over the lazy dog": STRING_TOO_LONG,\
                # Test 4 -- a palindrome, all lower case
                "racecar" : YES,\
                # Test 5 -- a palindrome, mixed cases
                "raCecar" : YES,\
                # Test 6 -- permutation of a palindrome, all lower case
                "raccear" : YES,\
                # Test 7 -- permutation of a palindrome, mixed cases
                "ARCecar" : YES,\
                # Test 8 -- Not a permutation of any palindrome
                "class": NO}

    for testInput, testOutput in testCase.items():
      scoreList.append(self.checkPalindrome(testInput) == testOutput)
    return sum(scoreList)

def main():
  print('Palindrome Permutation')
  pb5 = Problem5()
  print('Total score = ' + str(pb5.score()))


# Run the main() function
if __name__ == '__main__':
  main()
