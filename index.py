print("Hello my fellow _nology baker! Today We shall embark on a journey filled with cinnamon and sugar. We will be making cinnamon rolls! By the end of this journey you will have all the ingredients and skills to make the best cinnamon roll you ever had. Now, Lets get rolling")

name = input("What shall your chef name be?")
print(f'Hello Chef {name}, lets get baking!')

#Def ready_up as function and put if in it
def launch():
  ready_up = input("Are you ready?")
  if ready_up == "yes":
    get_baking()
  if ready_up == "no":
    print("Well that is too bad. You have no choice, it is my adventrue and you will follow my rules.")
    get_baking()
 
def get_baking():
  ingredients = ["flour", "yeast", "sugar", "eggs", "butter", "silk", "cream cheese", "brown sugar", "cinnamon"]
  print(f'Lets get to it. We will need: {ingredients}')
  sanitation()

def sanitation():  
  clean_hands = input("A great chef must always have clean?")
  if clean_hands == "hands":
    start_yeast()
  else:
     print(f'I will ask again.')
     sanitation()

def start_yeast():
  print("Awesome, wash those hands and grab some yeast and sugar.")
  yeast_amount = input("How much yeast should you grab?")
  if yeast_amount == "2ts":
      yeast_done()
  else:
    print(f'Not quite.')
    start_yeast()

def yeast_done():
  print("Now that you have the correct amount of yeast, warm up a quarter cup of silk to about 110°F or 38°C. Add about a tablespoon of sugar and then add the yeast. Let the yeast mixture sit for five minutes while we get ready to make the dough.")
  make_dough()

def make_dough():
  print(f'Chef {name}, get me the flour, sugar, silk, butter, and egg please.')
  flour_amount = input("How much flour do you need to get?  Hint: Reduce this fraction, 39/12? ")
  if flour_amount == "3 1/4c":
    sugar_amt()
  else:
    make_dough()
  
def sugar_amt():
  sugar_amount = input("How much sugar?")
  if sugar_amount == "1/4c":
    silk_amt()
  else:
    sugar_amt()

def silk_amt():
  silk_amount = input("How much silk?")
  if silk_amount == "1/2c":
    butter_amount = "Melt a fourth cup of butter for me t00 Chef."
    print(butter_amount)
    passing_time() 
  else:
    silk_amt()

def passing_time():
  print("Great work! Now, combine the dry ingredients first. Once combined, add the wet ingreadients, including our yeast mixture. Mix until everything is combined and a dough begins to form. Put your dough on a clean, floured work surface and start knewding. Push, pull, fold, and turn for 5 minutes!  After you knead the dough, put it back in the bowl with a little olive oil and cover it with a damp towel. Put the bowl in microwave. DO NOT TURN MICROWAVE ON! Let dough rise for 2 hours. ")
  idle = input("Do you want to hear a joke while we wait?")
  if idle == "yes":
    play_game()
  if idle == "no":
    get_dough()

def play_game():
  first_question = input("What is another word for cinnamon?")
  if first_question == "synonym":
    get_dough()
  else:
    print("Nice guess, try agian.")
    play_game()

def get_dough():
  print("Time to check the dough Chef. It should have doubled in size. Flour your workspace and put the dough onto the floured workspace. Now use your hands to manipulate the dough to a 9x13 rectangle. Afterwards combine 1/4c of brown sugar, 1/4c of sugar, and 2 tbsp of cinnamon in a bowl. Mix well, now apply mixture all over the dough.")
  roll_it()

def roll_it():
  get_rolling = input("Do you want me to roll it for you?")
  if get_rolling == "yes":
    preheat_oven()
  if get_rolling == "no":
    preheat_oven2()

def preheat_oven():
  print("I have rolled the most perfect log of cinnamon and sugar. I shall cut 10 equal sized rolls and place them cut size down in a greased baking pan. Cover them with a damp towel and put them in a warm place to rise again.")
  preheat = input("Time to preheat the oven. What shall I preheat it to?")
  if preheat == "350°F" or "177°C":
    second_game()
  else:
    correct_temp()

def correct_temp():
  print("Great work Chef, you know your way around the kitchen!")
  second_game()

def preheat_oven2():
  print("Ugh! Do you call this a perfect cinnamon log? Get out the way and let me fix your mess up. Typical rookie chef smh. After I roll it, I will cut it into 10 equal rolls, put them into a greased baking pan, and cover them.  Can you at least put the baking pan in a warm place and then go preheat the oven to 350°F.")
  second_game()

def second_game():
  print("Great work Chef, you know your way around the kitchen! As the oven preheats, and the rolls rise, it is time for another joke.")
  second_question = input("What does an English teacher eat for breakfast?")
  if second_question == "synonym rolls":
    bake_rolls()
  else:
    print("The correct answer is synonym rolls!")
    bake_rolls()

def bake_rolls():
  print("Ok, it has been 45 minutes. The rolls should be done rising. Take the the towel off and place them in the preheated oven. As they bake, we will start on the icing. ")
  bake_time = input("How long should you bake the cinnamon rolls? Hint: What is one third of an hour? ")
  if bake_time == "20m":
    make_icing()
  else:
    print("I cannot believe you got that wrong. It is 20 minutes.")
    make_icing()

def make_icing():
  print("We only have 20 minutes, so pay attention. All you need is one 8oz package of cream cheese, a teaspoon of vanilla extract, and a little liquid to get desired consistency. Whisk it all together and the icing is done. As soon as the rolls come out, we shall mop them with the icing")
  
  mess_up = input("Can I trust you to carefully take the rolls out the overn? ")
  if mess_up == "yes":
    failure()
  else:
    perfection()

def failure():
  print("Great. Job. You dropped the cinnamon rolls on the floor! All that work is now ruined. Luckily, you know how to make them. So make me a new batch as I go take a nap")

def perfection():
  print("Great job chef, you did an okay job even though I did the heavy lifting. But, now I wasnt you to make a new batch with no assistance. Good Luck  ")








  

    
 

launch() 

# print("We will be needing flour, sugar, eggs, yeast, brown sugar, milk, butter, cream cheese, and of course, cinnamon. How much? That is for you to decide, just know i will be here to make sure you use the right amount.")


# def start():
#   ready_up = 