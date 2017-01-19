import sys

'''

 _       __ _       __   __  __          _____  ______   ______
| |     / /| |     / /  / / / /         / ___/ /_  __/  / ____/
| | /| / / | | /| / /  / / / /          \__ \   / /    / /     
| |/ |/ /  | |/ |/ /  / /_/ /          ___/ /  / /    / /___   
|__/|__/   |__/|__/   \____/          /____/  /_/     \____/   
                                                              

Christian Brintnall

MIT License

Copyright (c) 2017

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

By the end of this workshop, you should have a basic understanding of
what the workshop is, and how Raspberry Pi's and the Python programming 
language works. 

Python is what is known as a "high level programming language." This essentially means
that Python isn't very "close" to the computer. Is this an issue? Outside of the computer
science world (and most the time inside), not really. The language was created to promote
readability, which in turn makes it more accessible. Blocks of code are delimited by
whitespace as opposed to the typical brackets {} used by languages such as Java, C#, and C.

An example of this would be these two different statements (no need to know what this code does,
just how it differs). As far as functionality, these two if statements are the exact same thing.

Java (the if statement)~~

if (number == 1)
{
    return number
}
else
{
    return 0
}

Python (the if statement)~~

if (number == 1):
    return number
else:
    return 0

Interesting how different they can look yet maintain the same functionality. As we go through this
workshop you'll learn different ways to manipulate data in Python and create our own (very small)
text adventure game. We will then apply this knowledge to the Raspberry Pi.

THIS GUIDE FOLLOWS PEP 8 CONVENTIONS. FOR MORE INFO GO TO https://www.python.org/dev/peps/pep-0008/
(^ Just says I like to keep the code here pretty and readable, if you want to do more Python,
                                            I suggest reading the above link, it's pretty neat.)



'''

STC_TEMPLATE_DISCLAIMER = "This is a template file made for the purpose of showing how this workshop will work.\n-------------------------------------------------------------------------------------\n\n"

print(STC_TEMPLATE_DISCLAIMER)

'''

Part 1: Player info (variables)

We're going to need more player info probably. Lets assign some variables.

'''

health = 5
attack = 2
defense = 2

'''

Part 2: Player name 

Every player needs a name, silent protagonists tend to feel one dimensional.
So how are we going to name our player? Simple, we ask them. We can ask them, 
and store it somewhere for using later. Doing something like this is called assigning
a value to a variable. Variables are used to store data for later use, and as we learn
can be various different things. We can store data in multiple ways, but for now
we will do it in the most simple.

'''

#Below we can see that I prompt the user for their name, and 
#whatever they type is what player_name is equal to.
player_name = input("Hey, what is your name? ")
print("Wow, hey {name} nice to meet you!".format(name = player_name))

'''

Whoa, A LOT just happened. We grabbed the players name using input. So what
exactly is input? Well simply put, input is a function made by the people who made 
Python. You can tell something is a function because it'll say something like
hello(). Where the format is [function-name](). Why the ()? More on that later.
For now we can assume whatever we put into input, it'll prompt the user with.
Can you spot where else I used a function above? Hint, theres actually two.
To pass into the next part, pass the next simple test! Run the script and you can get
passed it. These tests aren't required, and you can simply hit enter to skip them.

'''

print("\n\n\nQUIZ!")
test_answer_one = input("What variable is the player's name assigned to? (Remember this can be skipped by pressing enter) ")
if (test_answer_one == "player_name" or test_answer_one == ""):
    print("Good job, keep going!\n\n\n")
else:
    sys.exit(0)

'''

Part 3: Choices (if statements)

I just did something above, I checked what you entered, and depending on what
you put in, different outcomes were done. Hopefully you chose the correct one!
Lets try out own.

'''

if (player_name == "Christian"):
    print("Hey you wrote this")
else:
    print("You're an imposter!")

'''

Above we can see that if the player's name is Christian, well thats me, and it
tells us that. If you're not Christian, you're an imposter! Play around with
if statements, they're fun. But, what if we want to check if something else was
assigned as the player, maybe your friend?

'''

if (player_name == "Christian"):
    print("Hey it's Christian again!\nHave some health!")
    health = health + 20
#Hey this is new! We're just doing another if essentially!    
elif (player_name == "STC"):
    health = health + 3
else:
    health = health + 2

'''

So now we can check other things, but something else was just done.. We added something
to another variable! Is this possible? Obviously cause the code ran this far it is.
What does health print out now? Probably something different, as every outcome adds to it.
There are various operators as you'd expect. + - / * and also %. Wait what? Thats never mentioned
in math. 

ACTUALLY, it is. Remember in fourth grade when you did long division and you had the remainder
of a number? Yeah %, titled "modulo," gives you that. So 8 % 5 gives us three!

'''

print("\n\n\nQUIZ!")
test_answer_two = input("What is player_name + 'David' (Remember this can be skipped by pressing enter) ")
if (test_answer_two == player_name + "David" or test_answer_two == ""):
    print("Good job, keep going!\n\n\n")
else:
    sys.exit(0)
