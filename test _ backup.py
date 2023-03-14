import pyfiglet, random

print("------------------------------------------------------------------------------------------------")
# Generate ASCII art for "HANGMAN" using the Pyfiglet module
heading = pyfiglet.figlet_format("HANGMAN", font="standard")

# Print the heading
print(heading)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# musical instrument related list

MUSIC = ['GUITAR', 'PIANO', 'VIOLIN', 'DRUMS', 'TABLA', 'FLUTE']

# SPORTS list

SPORTS = ['FOOTBALL', 'BASKETBALL', 'BASEBALL', 'TENNIS', 'GOLF', 'HOCKEY', 'VOLLEYBALL', 'CRICKET', 'BOXING',
          'WRESTLING', 'BADMINTON', 'SWIMMING']

# fruit list

FRUITS = ['APPLE', 'BANANA', 'ORANGE', 'GRAPE', 'STRAWBERRY', 'MANGO', 'PINEAPPLE', 'WATERMELON', 'PAPAYA', 'CHERRY',
          'BLUEBERRY']

# bollywood celebrity

CELIBRITY = ['SHARUKHKHAN', 'AKSHAYKUMAR', 'RANBIRKAPOOR']
# topic for heading


# selecting random toipcs list

topic = random.choice([MUSIC, FRUITS, CELIBRITY, SPORTS])
# Print the selected topic
if topic == MUSIC:
    print("----------------------------------------------⚫MUSIC----------------------------------------------")
elif topic == SPORTS:
    print("----------------------------------------------⚫SPORTS----------------------------------------------")

elif topic == FRUITS:
    print("----------------------------------------------⚫FRUITS----------------------------------------------")
elif topic == CELIBRITY:
    print("----------------------------------------------⚫CELIBRITY----------------------------------------------")
# choosing a random word
word = random.choice(topic)

# looping to find total numer of word in that list
word_number = len(word)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# printing blanks
print("")
str1 = "WORD =  "
str2 = "━ " * word_number
blanks = str1+str2
print(blanks)
dash_symbol = "━"


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
anonyms_word = word
# defining a function of random word list containing a  random word

def word_options():
    word_list = list(word)
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    random.shuffle(word_list)
    end_range = 16 - word_number
    for i in range(1, end_range):
        a = random.choice(all_letters)
        word_list.append(a)

    for row in range(3):
        i = row * 5
        while i < (row + 1) * 5:
            j = word_list[i]
            print('┌───┐', end=' ')
            i += 1
        print()

        i = row * 5
        while i < (row + 1) * 5:
            j = word_list[i]
            print('│ {} │'.format(j), end=' ')
            i += 1
        print()

        i = row * 5
        while i < (row + 1) * 5:
            j = word_list[i]
            print('└───┘', end=' ')
            i += 1
        print()


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# calling function and then creating keyboard
word_options()






















print(word)




# if word_number >= 5:
#     word_list = list(word)
#     guess1 = input("GUESS THE LETTER ? = ")
#
# # creating a list that contain the index of matching word
#     index_list = []
#     i = 0
#     while i < word_number:
#         if word_list[i] == guess1:
#             i = i+1
#             index_list.append(i)
#             print("GUESS THE RIGHT LETTER !")
#             total_index = len(blanks)
#             n = len(index_list)
#             j = 0
#             while j < n:
#                 blanks.append(index_list[j],str2[j])
#                 j = j+1
#                 print(blanks)
#     i = i + 1
#
#
#
#
#
#



if word_number <= 5:
    index_list1 = []
    word_index = list(word)
    try:
        guess1 = input("GUESS THE LETTER = ?")
        if len(guess1) > 1 or not guess1.isalpha():
            print("ENTER A VALID CHARACTER !")
    except:
        print("ENTER A VALID LETTER")




    # # creating a loop that check every element of word index whether it matches with guess1 entered character
    # i = 0
    # while i < word_number:
    #     if word_index[i] == guess1:
    #         index_list1.append(i)
    #     i = i + 1
    #
    # print(index_list1)