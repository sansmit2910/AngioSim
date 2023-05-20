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
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
if not camera.isOpened():                      # if webcam cannot be accessed
   raise IOError("Webcam cannot be opened! Change index!")
ret, live=camera.read()
gray=cv2.cvtColor(live,cv2.COLOR_BGR2GRAY)
# Set a flag to indicate if the 'r' key is pressed or not
show_video = False
start_time = time.time()
ESCAPE_KEY=27
key_pressed=False
Recording=False #flag for recording
show_video1 = False #flag for displaying recorded video
flag=False #flag to decide mode
DSA=1 #variable for DSA mode
Roadmap=2 #variable for roadmap mode
path = r'C:/Users/Smit/Desktop/Dsa Simulator' #change directory
os.chdir(path) #change to above path to save file
# initialize pygame
# initialize pygame
# initialize pygame
pygame.init()

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# set the screen size
screen_size = (1920, 1080)

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
    window.title("Notification")
    label = tk.Label(window, text=text)
    label.pack(padx=100, pady=100)
    window.after(3000, window.destroy)
    window.mainloop()

# To show a notification, call the function with the desired text
show_notification("Native mode. Press R to view default view")
key=cv2.waitKey(1)

#main program loop
while True:
        # Read a frame from the video capture object
    ret, live = camera.read()  #read live feed
    gray = cv2.cvtColor(live, cv2.COLOR_BGR2GRAY)
    key=cv2.waitKey(1) & 0xFF
    #bg=None
    # If the frame was successfully read
    if ret:
        # Display the frame if the 'r' key is pressed
        key=cv2.waitKey(10)  & 0xFF #to run live feed smoothly
        if key == ord('7'):
            exit()
        if key==ord('1'):
          show_notification("Native mode")  
        if show_video:
          cv2.imshow('angio sim', gray)  #create a blank window
        
          # Wait for a key press and check if the 'r' key is pressed
          key=cv2.waitKey(1)  & 0xFF #for making the live feed run smoothly
        if key == ord('r'): #if condition for keypress r
          show_video = True  #change value of flag          
        elif not keyboard.is_pressed('r'):
          show_video = False
          key=cv2.waitKey(1)
        if key==ord('s'):
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
                 #image.show()
                 filename1 = 'Screenshot_' + dt_string  +'.jpg'
                 image=image.save(filename1)
                 show_notification("Screenshot saved, please view in folder Dsa Simulator")
                 # Get the handle of the window by its title
                 key=cv2.waitKey(1)
        if key==ord('2'):
                  # To show a notification, call the function with the desired text
                  show_notification("Roadmap Mode. Press r until satisfactory background picture is formed, then d for starting the subtraction and actual roadmap.")
                  flag=Roadmap
                  key=cv2.waitKey(1)
                  # initialize a frame counter
                  count = 1
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        acc = gray.astype('float')  
                # Loop through the frames in the video              
        while flag==Roadmap:
                
                key=cv2.waitKey(1)
                # Read the next frame
                ret, frame = camera.read()
                if not ret:
                    break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                #acc = gray.astype('float')  
                # Check for user input
                key=cv2.waitKey(1)
                if key == ord('1'):  # Escape key
                    show_notification("back to Native mode!")
                    flag=False
                if key==ord('7'):
                    exit()    
                if key == ord('r'):
                 
                 # Compute the minimum blend of the current frame and the accumulator
                 acc = np.minimum(acc, gray.astype('float'))

                 # Increment the frame counter
                 count += 1

                 # Convert the blended frame to an unsigned 8-bit integer
                 blended = acc.astype('uint8')

                 # Display the blended frame
                 cv2.imshow("angio sim", blended)
                 #key=cv2.waitKey(1)
                if key == ord('d'):
                 # Compute the difference between the current frame and the blended frame
                 result = cv2.subtract(gray, blended)
                 # Set the result to white
                 result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
                 result[np.where((result == [255, 255, 255]).all(axis=2))] = [0, 0, 255]
                 # Set the background to light gray
                 background = np.zeros_like(result)
                 background.fill(192)
                 # Combine the background and the result
                 output = cv2.addWeighted(background, 0.5, result, 0.5, 0.0)
                 # Display the difference frame
                 cv2.imshow("angio sim", output)
                if key==ord('2'):
                 show_notification("Roadmap mode reset")
                 blended=None
                 continue  # jump back to the beginning of the while loop    
                else: 
                 key=cv2.waitKey(1)
                
                 
                if key==ord('3'):
                 show_notification("DSA mode")
                 flag=DSA
                 #key=cv2.waitKey(1)
        if key==ord('3'):
                 show_notification("DSA mode")
                 flag=DSA
                 ret, live = camera.read()  #read live feed
                 gray = cv2.cvtColor(live, cv2.COLOR_BGR2GRAY)
                 #key=cv2.waitKey(1) & 0xFF
        #for recording video of aufnahme
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        filename2 = 'output_{}.avi'.format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
        # Set the screen size
        screen_size = (1920, 1080)
        fps = 2
        
        # Create a video writer object
        video_writer = cv2.VideoWriter(filename2, fourcc, fps, screen_size)
        
        while flag==DSA:
                 flag2=False           
                 ret, live = camera.read()  #read live feed
                 gray = cv2.cvtColor(live, cv2.COLOR_BGR2GRAY)
                 key=cv2.waitKey(1) & 0xFF
                 Name_DSA=filename2
                  # Get the current screen frame
                 screen_frame = pyautogui.screenshot()
                 

                 # Convert the screen frame to a numpy array
                 screen_frame_np = cv2.cvtColor(np.array(screen_frame), cv2.COLOR_RGB2BGR)

                 if ret:
                     # Display the frame if the 'r' key is pressed
                     #key=cv2.waitKey(1)  & 0xFF #to run live feed smoothly
                     if key ==ord('7'):
                      exit()
                     if key==ord('1'):  
                         show_notification("Native mode ")
                         flag=False
                         key=cv2.waitKey(1)
                     if key==ord('s'):
                          path = r'C:/Users/Smit/Desktop/Dsa Simulator'
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
                          #image.show()
                          filename1 = 'Screenshot_DSA_' + dt_string  +'.jpg'
                          image=image.save(filename1)
                          show_notification("Screenshot saved, please view in folder Dsa Simulator")                        
            
                     if show_video:
                         cv2.imshow('angio sim', gray)  #create a blank window
                         #key=cv2.waitKey(1)
                         # Wait for a key press and check if the 'r' key is pressed
                         key=cv2.waitKey(15)  & 0xFF #for making the live feed run smoothly
                     if key == ord('r'): #if condition for keypress r
                         show_video = True  #change value of flag
                         bg=None
                         key_pressed=True
                         now = datetime.now() #get current date and time
                         dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
                         filename = 'Backgroundat1fps_'+ dt_string +'.jpg'
                         #key=cv2.waitKey(1)           
                     if key_pressed and  not keyboard.is_pressed('r'):
                         bg=gray
                         #print(bg.shape)
                         font = cv2.FONT_HERSHEY_PLAIN
                         now_without_ms= now.strftime('%Y-%m-%d %H:%M:%S')

                         cv2.putText(bg, str(now_without_ms), (20, 40), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
                         maske=live
                         gray_mask=cv2.cvtColor(live, cv2.COLOR_BGR2GRAY)
                         key_pressed=False# to freeze live feed
                     if key==ord('3'):
                         show_notification("Already in DSA mode, background reset successfully, please take new Background.")  
                         flag=DSA                              
                     if key==ord('2'):
                         show_notification("Roadmap mode")
                         flag =Roadmap
                     elif not keyboard.is_pressed('r'):
                         show_video = False
                     if key == ord('d'):
                         flag2=True
                         diff = cv2.absdiff(gray, bg)
                         inverted_diff = cv2.bitwise_not(diff)
                         diff_colormap = cv2.applyColorMap(diff, cv2.COLORMAP_BONE)
    
                         # create a light gray background image with the same shape as inverted_diff
                         background = np.full(inverted_diff.shape, 0, dtype=np.uint8)
    
                         # blend the inverted_diff and background images
                         alpha = 0.8
                         blended_image = cv2.addWeighted(inverted_diff, alpha, background, 1-alpha, 0)
    
                         cv2.imshow('angio sim', blended_image)
                         # Write the current screen frame to the output video
                         screen_frame = pyautogui.screenshot()

                         # Convert the screen frame to a numpy array
                         screen_frame_np = cv2.cvtColor(np.array(screen_frame), cv2.COLOR_RGB2BGR)

                         video_writer.write(screen_frame_np)
                     if flag2 and not key==ord('d'):
                         video_writer.release()

                     if key == ord('8'):
                            # Open the saved video file
                            saved_video = cv2.VideoCapture(filename2)
                            saved_video.set(cv2.CAP_PROP_FPS, fps)
                            frame_count = 0


                            while True:
                                # Read the next frame from the saved video file
                                ret, frame5 = saved_video.read()
                                if not ret:
                                    break

                                cv2.imshow('angio sim', frame5)

                                # Wait for a short time between frames
                                key = cv2.waitKey(250)
                                if key == 27:
                                  exit()

                            frame_count += 1

                            # End of video file
                            saved_video.release()
                            print("End of video file ({} frames)".format(frame_count))

                            print('L_released')
                     else:
                      key=cv2.waitKey(1) 