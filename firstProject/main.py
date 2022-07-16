#SYNTAX ERROR HIAYA HEHEHEHA SYNTAX ERROR SYNTAX ERROR
import requests
import turtle
import random
import matplotlib.pyplot as plt
import colors as col

words = []
xpoint = []
ypoint = []
xpoint1 = []
ypoint2 = []
print('Welcome to ther useless service machine.')
#Variables used by wordz 'words, yorn, x, a, y'
def wordz():
  
  print(f"{col.Green}Welcome to the one time library! after you terminate the program the words will disappear. The program will auto terminate if you do not enter any words.")
  
  while True:
    
    yorn = input(f"{col.Green}Would you like to add another a word to the list {col.White}[{col.Green}y{col.White}/{col.Red}n{col.White}]?\n{col.White}>>> ")
    
    if yorn == "y":
      
      x = input(f'{col.Green}Please enter the word that you would like to add.\n{col.White}>>> ')
      words.append(x)
    
    if yorn == "n":
     
      break  
  
  a = len(words)
  
  if a > 0:
    
    while True:
     
      
      x = int(input(f'{col.Green}Please enter a number from {col.bright_green}1{col.Green} to {col.bright_green}{a}{col.Green} to view a word from the collection. Entering a number higher than {col.bright_green}{a}{col.Green} will terminate the program. Entering {col.bright_green}0{col.Green} will print the entire list. \n{col.White}>>> '))
      print('')
      y = x-1
     
      if 1 <= x <= a:
       
        print(words[y],'\n')
      
      if x == 0:
        
        while x < a:
          
          print(words[x])
          x = x+1    
      
      if x > a:
       
        break
def spirograph():
  
  print(f'{col.Red}Do not Minimize.')
  # Set the background color as black,
  # pensize as 2 and speed of drawing
  # curve as 10(relative)
  turtle.bgcolor('black')
  turtle.pensize(2)
  turtle.speed(10) 
  # Iterate six times in total 
  for i in range(8):
        # Choose your color combination
      for color in ['red', 'magenta', 'blue',
                    'cyan', 'green', 'white',
                    'yellow', 'orange', 'purple']:
          turtle.color(color)
          
          # Draw a circle of chosen size, 100 here
          turtle.circle(100)
           
          # Move 10 pixels left to draw another circle
          turtle.left(5)

          
       
      # Hide the cursor(or turtle) which drew the circle
      turtle.hideturtle()
      
      

def scraper():
#variables used "URL, page"  
  
  URL = input("Please enter a valid URL. Please do NOT prefix with 'https://'. \n>>> ")

  URL = 'https://' + URL
  
  page = requests.get(URL)
  print(page.text)
  
  main()
def impossible():
  
  input(f'{col.Green}In this game you will have a {col.Red}1 in 1.0e+18 chance to survive. {col.Green}If you enter anything else you will be brought to the main menu. press {col.Blue}"Enter"{col.Green}.\n')   
      

  randint = random.randint(1,1000000000)
  alsorandint = random.randint(1,1000000000)
      
  if randint == alsorandint == 69420:
        
    while True:
        
      noway = input(f"{col.Red}YOU WON!!!!!!!!!!!! YOU ACTUALLY DID IT!!!!!!!!! BOTH RANDOM NUMBERS EQUALED 69420!!!!!!!! YOU HAD A 1.0e+18 CHANCE OF GETTING THIS MESSAGE!!!!!!!!!!!!!!!!!!!!!!!(i think lol) TAKE A SCREENSHOT OR SOMETHING IDK BUT YOU DID IT!!!!!!!!!!!!!!!!!!!!! Enter 'I'm done' to go back to main menu\n >>> ")
      if noway == "I'm done":
          
        break
    
  else:
      
    print(f'{col.Red}You Died.\n{col.Green}Your numbers were {randint} and {alsorandint}.\n')
  

def grapher():
  while True: 
    legrandtitle = ''
    labelx = ''
    labely = ''
    
    oneortwo = input(f'{col.Green}Welcome to the primitive grapher!\nEnter 1 for one line.\nEnter 2 for two lines.\n{col.White}>>>')
    if oneortwo == '1': 
      while True:
            
        yesorno = input(f'{col.Green}Would you like to add a plot point to the graph[y/n]?\n{col.White}>>>')
            
        if legrandtitle == '':
            
          legrandtitle = input(f"{col.Green}What would you like to name your graph?\n{col.White}>>> ")
      
        if labelx == '':
      
          labelx = input(f'{col.Green}Please enter what you would like to lablel the "X" axis.\n{col.White}>>> ')
            
        if labely == '':
      
          labely = input('Please input what you would like to label the "Y" axis.\n>>>')
              
        if yesorno == 'y':
              
          xp = input('Please enter a valid float for your "X" variable.\n>>> ')
          xp = float(xp)
          xpoint.append(xp)
              
          yp = input('Please enter a valid floar fot your "Y" variable.\n>>> ')
          yp = float(yp)
          ypoint.append(yp)
      
          print(xpoint)
          print(ypoint)
        if yesorno == 'n':
      
          # plotting the points
          plt.plot(xpoint, ypoint)
                 
          # naming the x axis
          plt.xlabel(labelx)
          # naming the y axis
          plt.ylabel(labely)
                 
          # giving a title to my graph
          plt.title(legrandtitle)
                
          # function to show the plot
          plt.show()
          break
  
    if oneortwo == "2":
      while True:
        print("work in progress.")
        break
def main():  
  while True:
    #main menu, variables used 'game, really'
    game = input(f'{col.Green}Please Choose a service to use:\nEnter {col.Red}"exit"{col.Green} to wipe all data.\nEnter {col.bright_cyan}"w"{col.Green} for the word collection.\nEnter {col.bright_cyan}"c"{col.Green} for the website source code.\nEnter {col.bright_cyan}"s"{col.Green} for spirograph.\nEnter {col.bright_cyan}"i"{col.Green} for impossible game.\nEnter {col.bright_cyan}"g"{col.Green}for grapher.{col.White}\n>>> ')
  
    if game == 'g':
  
      grapher()
    
    if game == 'w':
      
      wordz()
    
    if game == 'c':
      
      scraper()
    
    if game == 's':
      
      print(f'{col.Green}please wait...')
      spirograph()
      print(f'{col.Green}finished.')
    
    if game == 'i':
      
      impossible()
   
    if game == 'exit':
      
      really = input(f'\n{col.Red}Are you sure you want to wipe ALL DATA. {col.bold}THIS CANNOT BE UNDONE[y/n]\n>>> ')
      
      if really == 'y':
        
        break
main()
print('All data has been wiped and program is terminating. Goodbye!')
