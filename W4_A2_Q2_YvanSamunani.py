
#  A list with all the answers that the program uses to check the validity of the provided answers
answers = ["2015",['Fred Swaniker', 'swaniker fred', 'fred'], "Rwanda and Mauritius", "2", "Hardji Ghandi", "Sila Ogidi", "Fab Lab", "120", "8", "Mauritius"]

# score variable used to count how many questions a user gets correct
score = 0
# wrong_answers variable used to count the number of questions a user gets wrong
wrong_answers = 0
# count_loses variable used to count the number of loses a user gets before ending the game
count_loses = 0
# count_wins variable used to count the number of wins before deciding to end the game
count_wins = 0

# question_1 () function handling the first question question
def question_1():
    # made score, wrong_answers, count_wins, and count_loses global variables so that they can be accessed everywhere in the program and
    # be updated all the time
    global score
    global wrong_answers
    global count_wins
    global count_loses

    # receiving answer for question 1
    ans_1 = input("Q1) When was ALU founded?:")

    # Checking whether the answer for question 1 is among the answers in answers list
    if ans_1 == answers[0]:

        # If the answer is in the answers list, score increments by one and informs the user their score /10
        score += 1
        print("Correct!", score, "/10")

    # If the answer is not in the answers list, wrong_answers increments by 1
    else:
        print("wrong", score, "/10", "\n", "You're a hanging man")
        wrong_answers += 1

    # Calling question_2() function for the user to continue to question 2
    question_2()


def question_2():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    # Using if condition to check whether wrong_answers are less than 6 for the user to continue playing
    if wrong_answers <6:

        # receiving answer for question 2
        ans_2= input("Q2) Who is the CEO of ALU? :")

        # Checking whether the answer for question 2 is among the answers in answers list
        if ans_2.lower() == answers[1][0].lower() or ans_2.lower() == answers[1][1].lower() or ans_2.lower() == answers[1][2].lower():
            score+= 1
            print("Correct!", score,"/10")

        # If the answer is not in the answers list, wrong_answers increments by 1
        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1

        # Calling question_3() function for the user to continue to question 3
        question_3()

    # If wrong_answers is greater than 6 the hang man dies and count_loses increments by 1
    else:
        print("The man dies!")
        count_loses += 1

        # Asking the user if the want to play again
        play_again = input("Do you want to play again [y/n]?:")

        # If yes, the program restarts by calling question_1() and sets score and wrong_answers to 0
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()

        # If they don't want to play again, the program tells them the total wins and loses.
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_3():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    # Using if condition to check whether wrong_answers are less than 6 for the user to continue playing
    if wrong_answers <6:

        # receiving answer for question 3
        ans_3 = input("Q3) Where are ALU campuses : ")
        if ans_3.lower() == answers[2].lower():

            # Checking whether the answer for question 3 is among the answers in answers list
            score += 1
            print("Correct!", score,"/10")

        # If the answer is not in the answers list, wrong_answers increments by 1
        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1

        # Calling question_4() function for the user to continue to question 4
        question_4()

    # If wrong_answers is greater than 6 the hang man dies and count_loses increments by 1
    else:
        print("The man dies!")
        count_loses += 1

        # Asking the user if the want to play again
        play_again = input("Do you want to play again [y/n]?:")

        # If yes, the program restarts by calling question_1() and sets score and wrong_answers to 0
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()

        # If not, the game ends and the program tells the user the total number of wins and loses
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_4():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    # Using if condition to check whether wrong_answers are less than 6 for the user to continue playing
    if wrong_answers <6:

        # receiving answer for question 4
        ans_4 = input("Q4) How many campuses does ALU have : ")

        # Checking whether the answer for question 4 is among the answers in answers list
        if ans_4 == answers[3]:
            score += 1
            print("Correct!", score,"/10")

        # If the answer is not in the answers list, wrong_answers increments by 1
        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1

        # Calling question_5() function for the user to continue to question 5
        question_5()

    # If wrong_answers is greater than 6 the hang man dies and count_loses increments by 1
    else:
        print("The man dies!")
        count_loses += 1

        # Asking the user if the want to play again
        play_again = input("Do you want to play again [y/n]?:")

        # If yes, the program restarts by calling question_1() and sets score and wrong_answers to 0
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()

        # If not, the game ends and the program tells the user the total number of wins and loses
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_5():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    # Using if condition to check whether wrong_answers are less than 6 for the user to continue playing
    if wrong_answers <6:

        # receiving answer for question 5
        ans_5 = input("Q5) What is the name of ALU Rwanda???s Dean : ")

        # Checking whether the answer for question 5 is among the answers in answers list
        if ans_5.lower() == answers[4].lower():
            score += 1
            print("Correct!", score,"/10")

        # If the answer is not in the answers list, wrong_answers increments by 1
        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1

        # Calling question_6() function for the user to continue to question 6
        question_6()

    # If wrong_answers is greater than 6 the hang man dies and count_loses increments by 1
    else:
        print("The man dies!")
        count_loses +=1

        # Asking the user if the want to play again
        play_again = input("Do you want to play again [y/n]?:")

        # If yes, the program restarts by calling question_1() and sets score and wrong_answers to 0
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()

        # If not, the game ends and the program tells the user the total number of wins and loses
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_6():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    # Using if condition to check whether wrong_answers are less than 6 for the user to continue playing
    if wrong_answers <6:

        # receiving answer for question 6
        ans_6 = input("Q6) Who is in charge of Student Life : ")

        # Checking whether the answer for question 6 is among the answers in answers list
        if ans_6.lower() == answers[5].lower():
            score += 1
            print("Correct!", score,"/10")

        # If the answer is not in the answers list, wrong_answers increments by 1
        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1

        # Calling question_7() function for the user to continue to question 7
        question_7()

    # If wrong_answers is greater than 6 the hang man dies and count_loses increments by 1
    else:
        print("The man dies!")
        count_loses += 1

        # Asking the user if the want to play again
        play_again = input("Do you want to play again [y/n]?:")

        # If yes, the program restarts by calling question_1() and sets score and wrong_answers to 0
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()

        # If not, the game ends and the program tells the user the total number of wins and loses
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_7():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    # Using if condition to check whether wrong_answers are less than 6 for the user to continue playing
    if wrong_answers <6:

        # receiving answer for question 7
        ans_7 = input("Q7) What is the name of our Lab? : ")

        # Checking whether the answer for question 7 is among the answers in answers list
        if ans_7.lower() == answers[6].lower():
            score += 1
            print("Correct!", score,"/10")

        # If the answer is not in the answers list, wrong_answers increments by 1
        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1

        # Calling question_8() function for the user to continue to question 8
        question_8()

    # If wrong_answers is greater than 6 the hang man dies and count_loses increments by 1
    else:
        print("The man dies!")
        count_loses += 1

        # Asking the user if the want to play again
        play_again = input("Do you want to play again [y/n]?:")

        # If yes, the program restarts by calling question_1() and sets score and wrong_answers to 0
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()

        # If not, the game ends and the program tells the user the total number of wins and loses
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_8():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    # Using if condition to check whether wrong_answers are less than 6 for the user to continue playing
    if wrong_answers <6:

        # receiving answer for question 8
        ans_8 = input("Q8) How many students do we have in Year 2 CS? : ")

        # Checking whether the answer for question 8 is among the answers in answers list
        if ans_8 == answers[7].lower():
            score += 1
            print("Correct!", score,"/10")

        # If the answer is not in the answers list, wrong_answers increments by 1
        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1

        # Calling question_9() function for the user to continue to question 9
        question_9()

    # If wrong_answers is greater than 6 the hang man dies and count_loses increments by 1
    else:
        print("The man dies!")
        count_loses += 1

        # Asking the user if the want to play again
        play_again = input("Do you want to play again [y/n]?:")

        # If yes, the program restarts by calling question_1() and sets score and wrong_answers to 0
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()

        # If not, the game ends and the program tells the user the total number of wins and loses
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_9():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    # Using if condition to check whether wrong_answers are less than 6 for the user to continue playing
    if wrong_answers <6:

        # receiving answer for question 9
        ans_9 = input("Q9) How many degrees does ALU offer? : ")

        # Checking whether the answer for question 9 is among the answers in answers list
        if ans_9 == answers[8]:
            score += 1
            print("Correct!", score,"/10")

        # If the answer is not in the answers list, wrong_answers increments by 1
        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1

        # Calling question_10() function for the user to continue to question 10
        question_10()

    # If wrong_answers is greater than 6 the hang man dies and count_loses increments by 1
    else:
        print("The man dies!")
        count_loses += 1

        # Asking the user if the want to play again
        play_again = input("Do you want to play again [y/n]?:")

        # If yes, the program restarts by calling question_1() and sets score and wrong_answers to 0
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()

        # If not, the game ends and the program tells the user the total number of wins and loses
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")


def question_10():
    global score
    global wrong_answers
    global count_wins
    global count_loses

    # Using if condition to check whether wrong_answers are less than 6 for the user to continue playing
    if count_loses <6:

        # receiving answer for question 10
        ans_10 = input("Q10) Where are the headquarters of ALU : ")

        # Checking whether the answer for question 10 is among the answers in answers list
        if ans_10.lower() == answers[9].lower():
            score += 1
            print("Correct!", score,"/10")

        # If the answer is not in the answers list, wrong_answers increments by 1
        else:
            print("wrong", score, "/10", "\n", "You're a hanging man")
            wrong_answers += 1

            # Asking the user if the want to play again
            play_again= input("Do you want to play again [y/n]?:")

            # If yes, the game restarts by calling question_1() function and setting score and wrong_answers to 0
            if play_again.lower() == "y":
                score = 0
                wrong_answers = 0
                print("\n")
                question_1()
            # If not, the game ends and the program tells the user the total number of wins and loses
            else:
                count_wins +=1
                print("\n")
                print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")

    # If wrong_answers is greater than 6 the hang man dies and count_loses increments by 1
    else:
        print("The man dies!")
        count_loses += 1

        # Asking the user if the want to play again
        play_again = input("Do you want to play again [y/n]?:")

        # If yes, the game restarts by calling question_1() function and setting score and wrong_answers to 0
        if play_again.lower() == "y":
            score = 0
            wrong_answers = 0
            print("\n")
            question_1()

        # If not, the game ends and the program tells the user the total number of wins and loses
        else:
            print("you won", count_wins, "time(s) and lost", count_loses, "time(s)")

# Calling question_1() function and it is where the program starts.
question_1()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
