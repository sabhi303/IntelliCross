# import pygame package 
import pygame
import sys
import time
import easygui
# initializing imported module 
pygame.init() 

# displaying a window of height 
window = (1358, 730)
screen = pygame.display.set_mode(window) 
line_color = (255, 0, 0)
white=(255,255,255)
font= pygame.font.SysFont('Arial', 29)
msg1=" "
msg2=" "

#  get the size
x, y = screen.get_size()
filename = "assets/Base2.1.jpg"

image = pygame.image.load(filename).convert()
pygame.display.flip()
screenUpdate = pygame.transform.smoothscale(image, (x, y))	

# Load the button image
#button1
button1 = pygame.image.load("assets/buttons/button1.png") 
button_width, button_height = button1.get_size()
button1 = pygame.transform.smoothscale(button1, (button_width/55, button_height/55))
#position 
button1_rect = button1.get_rect(topright=(1300, 10))

#button2
button2 = pygame.image.load("assets/buttons/scenario 2.png") 
button_width2, button_height2 = button2.get_size()
button2 = pygame.transform.smoothscale(button2, (button_width2/5, button_height2/5))
#position 
rect2 = button2.get_rect(topright=(1300, 100))

#button3
button3 = pygame.image.load("assets/buttons/scenario 3.png")  
button_width3, button_height3 = button3.get_size()
button3 = pygame.transform.smoothscale(button3, (button_width3/5, button_height3/5))
#position 
rect3 = button3.get_rect(topright=(1300, 200))
done = False
display_popup= False

while not done:
   for event in pygame.event.get():
      screen.blit(screenUpdate, (0,0))
      screen.blit(button1, button1_rect)
      screen.blit(button2, rect2)
      screen.blit(button3, rect3)

   if event.type == pygame.QUIT:
         done = True
   if event.type == pygame.MOUSEBUTTONDOWN:
      if button1_rect.collidepoint(event.pos):
            msg1 = "Normal Traffic"
            msg2 = "Conditions"
      if rect2.collidepoint(event.pos):
            msg1 = "Peak Traffic"
            msg2 = "Hours"
      if rect3.collidepoint(event.pos):
         msg1 = "Dynamic Traffic"
         msg2 = "Patterns"
         display_popup = True
   #Display text 1 
   img1=font.render(msg1,False, white)
   #Display text 1 
   img2=font.render(msg2,False, white)
   imgrect1=img1.get_rect()
   imgrect1.center = (1200 , 320 )
   imgrect2=img2.get_rect()
   imgrect2.center = (1200 , 360 )

   screen.blit(img1, imgrect1)
   screen.blit(img2, imgrect2) 
   pygame.display.update()

   if display_popup:
         defvalue= 0
       # Display Pop-up for dynamic vehicle count entry
         messag = "Enter Number of Vehicles for Different Lanes"
         title = "Dynamic Vehicle Count"
         fieldNames = [" North "," South "," East "," West "]
         fieldValues = [ 2,2,2,2]  # we start with blanks for the values
         fieldValues = easygui.multenterbox(messag,title,fieldNames,fieldValues)
         print(fieldValues)
         display_popup=False
#        # None of the fields should be empty
         while 1:
            if fieldValues == None: break
            errmsg = ""
            for i in range(len(fieldNames)):
              if fieldValues[i].strip() == "":
                  errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])                 
              elif  0 > int(fieldValues[i].strip()) or int(fieldValues[i].strip())> 10 :                
                  errmsg = errmsg + ('"%s" vehicle count cannot  be less than 0 and more than 10.\n\n' % fieldNames[i])
            if errmsg == "": break # no problems found
            fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
           # print("Reply was:", fieldValues)
   pygame.display.update()


