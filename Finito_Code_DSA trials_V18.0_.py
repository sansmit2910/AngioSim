import pygame
import cv2
from datetime import datetime
import pyautogui
#import matplotlib
import os
import time
import keyboard
import tkinter as tk
#matplotlib.use("TkAgg")
import os
import numpy as np
from datetime import datetime
camera = cv2.VideoCapture(0)                   # Initialize the video capture object to access the default camera, if not accessible change index
# Set the frame size of the camera capture object to 1280x720
# camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1880)
# camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1050)
# camera.set(cv2.CAP_PROP_FPS, 10)

if not camera.isOpened():                      # if webcam cannot be accessed
   raise IOError("Webcam cannot be opened! Change index!")
ret, live=camera.read()
gray=cv2.cvtColor(live,cv2.COLOR_BGR2GRAY)
# Set a flag to indicate if the 'r' key is pressed or not
show_video = False #flag
start_time = time.time()
key_pressed=False
Recording=False #flag for recording
show_video1 = False #flag for displaying recorded video
flag=False #flag to decide mode
DSA=1 #variable for DSA mode
Roadmap=2 #variable for roadmap mode
path = r'C:/Users/skhandelwal/Desktop/Dsa Simulator' #change directory
os.chdir(path) #change to above path to save file

# pyautogui.PAUSE = 0.01
#for recording video of aufnahme
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#filename2 = 'output_{}.avi'.format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
# Set the screen size
#screen_size = (1920, 1080)
#fps = 2
        
# Create a video writer object
#video_writer = cv2.VideoWriter(filename2, fourcc, fps, screen_size)
        
# initialize pygame
# initialize pygame
# initialize pygame
pygame.init()

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set the screen size
screen_size = (800, 600)

# create the screen
screen = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)

# set the window title
pygame.display.set_caption("Title Slide")

# load font and set font size
font = pygame.font.SysFont(None, 100)

# render the title text
title_text = font.render("DSA Simulator", True, BLACK)

# get the size of the title text
title_rect = title_text.get_rect()

# center the title text
title_rect.center = screen.get_rect().center

# render the instructions text
font = pygame.font.SysFont(None, 50)
instructions_text = font.render("Welcome to DSA Simulator", True, BLACK)

# get the size of the instructions text
instructions_rect = instructions_text.get_rect()

# position the instructions text below the title text
instructions_rect.center = (title_rect.centerx, title_rect.bottom + 50)

# set up the buttons
button_width = 200
button_height = 50
button_margin = 20
button_y = screen_size[1] - button_height - button_margin
next_button_x = button_margin
close_button_x = screen_size[0] - button_width - button_margin
next_button = pygame.Rect(next_button_x, button_y, button_width, button_height)
close_button = pygame.Rect(close_button_x, button_y, button_width, button_height)

# render the text for the buttons
font = pygame.font.SysFont(None, 30)
next_text = font.render("Next", True, WHITE)
close_text = font.render("Close", True, WHITE)

# flag to track whether the program should start
start_program = False

# flag to track whether the program is running
running = True

# main event loop
while running:

    # fill the screen with white
    screen.fill(WHITE)

    # draw the title, instructions, and buttons
    screen.blit(title_text, title_rect)
    screen.blit(instructions_text, instructions_rect)
    pygame.draw.rect(screen, BLACK, next_button)
    pygame.draw.rect(screen, BLACK, close_button)
    screen.blit(next_text, next_button)
    screen.blit(close_text, close_button)

    # update the screen
    pygame.display.update()

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # quit if the close button is clicked
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if the next or close button is clicked
          if next_button.collidepoint(event.pos):
                # set the flag to start the program
                start_program = True
                # exit the event loop
                running = False
          elif close_button.collidepoint(event.pos):
                # exit the event loop
                running = False
        elif event.type == pygame.KEYDOWN:
            # check if the 'r' or 'd' key is pressed
         if event.key == pygame.K_r:
                # set the flag to start the program
                start_program = True
                # exit the event loop
                running = False
         elif event.key == pygame.K_d:
                # exit the event loop
                running = False

# close the pygame window
pygame.quit()

# create the opencv window
cv2.namedWindow("angio sim", cv2.WND_PROP_FULLSCREEN)
cv2.namedWindow('angio sim', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('angio sim', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# Function to display the message box
# Function to display the message box
# Create a Tkinter window as notification for start
def show_notification(text):
    window = tk.Tk()
    window.overrideredirect(True)
    window.geometry("400x100+1000+600")
    window.wait_visibility(window)
    window.attributes('-alpha', 0.7)
    label = tk.Label(window, text=text, bg='black', fg='white')
    label.pack(fill='both', expand=True, padx=100, pady=50)
    window.after(3000, window.destroy)
    window.mainloop()


# To show a notification, call the function with the desired text
show_notification("Native mode. Press R to view default view")
key=cv2.waitKey(1)

while True:
    #bg=None
    # Read a frame from the video capture object
    ret, live = camera.read()  #read live feed
    gray = cv2.cvtColor(live, cv2.COLOR_BGR2GRAY)
    key=cv2.waitKey(1) & 0xFF
    #bg=None
    # If the frame was successfully read
    if ret:
        
        # Display the frame if the 'r' key is pressed
        key=cv2.waitKey(1)  & 0xFF #to run live feed smoothly
        if key == 27:
            exit()    
        elif key==ord('m'):
           flag=True
           while flag==True:
            exit
        elif show_video:
            cv2.imshow('angio sim', gray)  #create a blank window
            key=cv2.waitKey(1)
         # Wait for a key press and check if the 'r' key is pressed
        key=cv2.waitKey(1)  & 0xFF #for making the live feed run smoothly
        if key == ord('r'): #if condition for keypress r
         show_video = True  #change value of flag
         bg=None
         key_pressed=True  
        #  elapsed_time = time.time() - start_time
        #        # check if time difference is greater than 1/fps seconds
        #  if elapsed_time >=1:
        #    start_time=time.time()
        #    #create file name with date and time
        #    font = cv2.FONT_HERSHEY_PLAIN
        #    cv2.putText(live, str(datetime.now()), (20, 40), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        now = datetime.now() #get current date and time
        dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
        filename = 'Backgroundat1fps_'+ dt_string +'.jpg'
        #    cv2.imwrite(filename, live)
         
        if key_pressed and  not keyboard.is_pressed('r'):
             bg=gray
             #print(bg.shape)
             font = cv2.FONT_HERSHEY_PLAIN
             now_without_ms= now.strftime('%Y-%m-%d %H:%M:%S')

             cv2.putText(bg, str(now_without_ms), (20, 40), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
             now = datetime.now() #get current date and time
             cv2.imwrite(filename,bg)
             maske=live
             gray_mask=cv2.cvtColor(live, cv2.COLOR_BGR2GRAY)
             key_pressed=False
             def create_popup_message(message, timeout):
              popup = tk.Tk()
              popup.title("Message")
              label = tk.Label(popup, text=message)
              label.pack(padx=10, pady=10)
              popup.after(timeout, popup.destroy)
              popup.bind("<Key>", lambda event: popup.destroy())
              popup.mainloop()

              # Example usage
              create_popup_message("Mask Saved!", 5000)      
        if key==27:
           exit() 
        elif not keyboard.is_pressed('r'):
          show_video = False  # to freeze live feed

        if key == ord('d'):
            #print(bg.shape) 
            #  font = cv2.FONT_HERSHEY_PLAIN
            #  cv2.putText(bg, str(datetime.now()), (20, 40), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
            #  now = datetime.now() #get current date and time
            #  dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
            #  filename = 'Backgroundtobesubtracted_'+ dt_string +'.jpg'
            #cv2.namedWindow(window_name_bg, cv2.WINDOW_NORMAL)
            #cv2.imshow(window_name_bg,bg)
            key=cv2.waitKey(1)
         #cv2.imwrite(filename, bg)
        #if 'bg' in dir():
            #liveDsa=cv2.subtract(bg,live)
            #liveDsa=cv2.cvtColor(liveDsa, cv2.COLOR_BGR2GRAY)   #https://www.geeksforgeeks.org/python-opencv-cv2-cvtcolor-method/
            #liveDsa=cv2.resize(liveDsa, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
            #cv2.namedWindow(window_name_liveDSA, cv2.WINDOW_NORMAL)  
              
            #min_val, max_val, _, _ = cv2.minMaxLoc(liveDsa)
            #cv2.convertScaleAbs(liveDsa, 1.5, -120) #for changing image parameters like contrast and brightness  
            #cv2.imshow(window_name_liveDSA, ~liveDsa)
            #min_val, max_val, _, _ = cv2.minMaxLoc(liveDsa)
            #stretched = cv2.convertScaleAbs(liveDsa, alpha=255.0/(max_val-min_val), beta=-255.0*min_val/(max_val-min_val))
            #Display the stretched grayscale image
            #cv2.namedWindow('stretched', cv2.WINDOW_NORMAL)
            #cv2.imshow('stretched', stretched)
            diff = cv2.absdiff(gray, bg)
            inverted_diff= cv2.bitwise_not(diff)
            # Threshold the diff image to create a binary mask
            #mask = cv2.threshold(diff, thresh=10, maxval=255, type=cv2.THRESH_BINARY)
            # Threshold the diff image to create a binary mask
            #mask = cv2.threshold(diff, thresh=10, maxval=255, type=cv2.THRESH_BINARY)

    # Invert color of mask
            #inverted_mask = cv2.bitwise_not(mask)
            #mask = cv2.threshold(diff, thresh=10, maxval=255, type=cv2.THRESH_BINARY)

           # Invert the color of the mask
            #inverted_mask = cv2.bitwise_not(mask)
# Invert the color of the mask
            #inverted_mask = cv2.bitwise_not(mask)
            #including trial to improve quality v18.0
            diff_colormap = cv2.applyColorMap(diff, cv2.COLORMAP_BONE)
            #out.write(diff_colormap)
            #cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
            cv2.imshow('angio sim', inverted_diff)  
            #normalized = cv2.normalize(liveDsa, None, 0, 255, cv2.NORM_MINMAX)

              # Apply histogram equalization to maximize the contrast
            #equalized = cv2.equalizeHist(normalized)

              # Display the resulting image
            #cv2.namedWindow(window_name_maxcontrast, cv2.WINDOW_NORMAL)  
             
            #cv2.imshow(window_name_maxcontrast, equalized)
            key=cv2.waitKey(1)
              # Apply histogram equalization to the difference image
            #gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            #equalized = cv2.equalizeHist(gray)

              # Show the resulting image
            #cv2.namedWindow('Contrast Enhanced Image', cv2.WINDOW_NORMAL)
            #cv2.imshow('Contrast Enhanced Image', equalized)
              #ctypes.windll.user32.MessageBoxW(0,"Frame captured successfully!",1)
        if key==ord('s'):
          path = r'C:/Users/skhandelwal/Desktop/Dsa Simulator'
          os.chdir(path)
          target = pyautogui.getActiveWindow()
          location = (
          target.left,
          target.top,
          target.width,
          target.height
          )
          image = pyautogui.screenshot(region=location)
          now = datetime.now() #get current date and time
          dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
          image.show()
          filename1 = 'Screenshot_' + dt_string  +'.jpg'
          image=image.save(filename1)
          # Get the handle of the window by its title
          
    else:
            
        c=cv2.waitKey(1) 
                   # wait for keypress