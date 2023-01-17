print(
"Hello my fellow _nology bakers! Today We shall embark on a journey filled with cinnamon and sugar. We will be making cinnamon rolls! By the end of this journey you will have all the ingredients and skills to make the best cinnamon roll you ever had. Now, Lets get rolling"

)

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
  flour_amount = input("How much flour do you need to get?")
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
  else:
    silk_amt()


  

    
 

launch() 

# print("We will be needing flour, sugar, eggs, yeast, brown sugar, milk, butter, cream cheese, and of course, cinnamon. How much? That is for you to decide, just know i will be here to make sure you use the right amount.")


# def start():
#   ready_up = 