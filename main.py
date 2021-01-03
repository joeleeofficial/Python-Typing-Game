from getch import getch
import time
import random
import os
from colorama import Fore, Style, Back
level1 = ['This Is An Apple. ', 'But How Do I Spell Apple ? ', 'Its APPLE !']
level2 = ['Jhon Said I Don't Know How To Type. ', 'But Now I Am Going To Show Him. ', 'I tried This Typing Game So I Can Prove How Good I am To Jhon! ']
level3 = ['Jhon Is My Frinend ! ', 'But Now He Is Not !', 'He Is Bad Because He Call Me To Type 12345 and 67890. ! say cheese !', 'I groce communication']
level4 = ['Joe Sad Sad ', 'But Now He Is Not !', 'He Is Bad Because He Call Me To Type 12345 and 67890. ! I say cheese !', 'I groce communication', 'now i lean math', 'math is bad']

def split(x):
    return [char for char in x]
def get_list(x, count):
    try:
        value = ''
        for i in x:
            i = Style.BRIGHT + Fore.WHITE + i + Style.RESET_ALL
        v = x[count]
        x[count] = Style.BRIGHT + Fore.BLACK + Back.GREEN + v + Style.RESET_ALL 
        for i in x:
            value += i
        return value
    except:
        return ("All Done!")
playing = True
while playing == True:
    print(Fore.GREEN+"Get Ready to type!"+Style.RESET_ALL)
    time.sleep(1)
    start = time.time()
    sentence = random.choice(level1) + random.choice(level2) + random.choice(level3)
    win = False
    out = ''
    os.system('clear')
    count = 0
    while win != True:
        ls = split(sentence)
        length = len(ls)
        os.system('clear')
        copy = ls
        out_s = get_list(split(sentence), count)
        print(Fore.CYAN + Style.BRIGHT + 'Type this sentence: ' + Fore.WHITE + Back.BLACK + out_s)
        print(Style.RESET_ALL + Fore.CYAN+"                >>> " + Style.RESET_ALL + Fore.GREEN+out)
        key = False
        while key != True:
            try:
                key_needed = ls[count]
                print("Key needed is: " + key_needed)
                try:
                    get_key = getch()
                    if get_key == key_needed:
                        out += get_key
                        count += 1
                        key = True
                    else:
                        print(Fore.RED + 'Wrong key! You pressed ' + get_key)
                except:
                    print("Error! Try again")
            except:
                if length == count:
                    print("Great job!")
                    win = True
                    playing = False
                    key = True
                    # here is how the score is calculated
                    end = time.time()
                    time_taken = end - start
                    score = int(100 - time_taken)
                    print(Fore.GREEN+" SCORE: " + str(score))
                else:
                    print("Error!")
