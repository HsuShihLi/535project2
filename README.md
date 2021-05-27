# 535project2
 This project is to extract the cumulative frequency of similar words for the use of sentiment analysis of reviews or text summarization.

ClassNumber:

535-01

Team members:

Jing Feng: jingfeng@csu.fullerton.edu

Hsushi Li: hsushihli@csu.fullerton.edu

Jingzhi Su: Jingzhi_Su@csu.fullerton.edu
Description of the project:

Given a text S of length n, we can easily calculate the frequency of each word in S usin a linear time o(n) algorithm. But words can be similar, ex: "foot" and "feet", "day" and "days". In this project, we need to extract the cumulative frequency of similar words instead of individual words. This is useful for sentiment analysis of reviews (movies, products, services,etc.) and text summarization (blogs, text files, web articles, etc.).

The problem can be formulated as follows: Given two lists, one list includes words and their frequencies, and the other list includes all pairs of similar words. Design an algorithm to print out a new list of the cumulative frequency of each sets of similar words. Note that similar words are transitive and symmetric. For example, if “long” and “big” are similar, and “big” and “large” are similar, then “long” and “large” are similar. In the final list, choosing the words that are the earliest in the alphabet is recommended.

Example:

Down below include three examples of the inputs and outputs.

Example 1

Input:

Words_Frequencies: WF[] = { (“foot”, 5), (“feet”, 12), (“day”, 3), (“days”, 8), (“fear”, 2), (“scared”, 1), (“long”, 12), (“large”, 5), (“big”,5), (“was”, 4), (“is”, 4), (“are”, 15)} of size 12

Synonyms: SYN[] = { (“foot”, “feet”), (“day”,“days”), (“fear”, “scared”), (“long” ,“big”), (“big” , “large”), (“is”, “are”), (“is”, “was”) } of size 7

Output:

CF[] = { (“feet”, 17), (“day”, 11), (“fear”,3), (“big”, 22), (“are”, 23) } of size 5

Example 2

Input:

Words_Frequencies: WF[] = { (“tons of”, 2), (“large number of ”, 12), (“mystical”, 13), (“magical”, 28), (“magic”, 5), (“unexplained”, 11), (“huge”, 2), (“large”, 51), (“horses”, 25), (“horse, 24), (“large mammal”, 24), (“herbivore”, 5)} of size 12

Synonyms: SYN[] = { (“herbivore”, “horses”), (“horse”,“large mammal”), (“horses”, “large mammal”), (“large number of” ,“huge”), (“tons of” , “large”), (“huge”, “large”), (“mystical”, “magical”) , (“magical”,”unexplained”), (“magic”, “magical”)} of size 9

Output:

CF[] = { (“herbivore”, 78), (“huge”, 67), (“magic”,57)} of size 3

Example 3

Input:

Words_Frequencies: WF[] = { (“tons of”, 2), (“large number of ”, 12), (“mystical”, 13), (“magical”, 28), (“magic”, 5), (“unexplained”, 11), (“huge”, 2), (“large”, 51), (“horses”, 25), (“horse, 24), (“large mammal”, 24), (“herbivore”, 5), (“large number of”,12)} of size 13

Synonyms: SYN[] = { (“herbivore”, “horses”), (“horse”,“large mammal”), (“horses”, “large mammal”), (“large number of” ,“huge”), (“tons of” , “large”), (“huge”, “large”), (“mystical”, “magical”) , (“magical”,”unexplained”), (“magic”, “magical”), (“horse”,”large mammal”)} of size 10

Output:

CF[] = { (“herbivore”, 78), (“huge”, 67), (“magic”,57)} of size 3

Features:

Python3; Synonyms Cumulative Frequencies.
