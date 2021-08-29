# template for "Stopwatch: The Game"

import simplegui

# define global variables
interval = 100
displayed_time = 0
wins = 0
tries = 0
result = '0/0'
timer_bool = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
#A, C & D -> 0-9 range
#B -> 0-5 range
def format(t):
    global displayed_time
    
    A = displayed_time // 600
    B = (displayed_time // 100) % 6
    C = (displayed_time // 10) % 10
    D = displayed_time % 10
    
    displayed_time_str = str(A) + ':' + str(B) + str(C) + '.' + str(D)
    
    if displayed_time == 6000:
        timer.stop()
    
    return displayed_time_str
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer_bool
    if not timer.is_running():
        timer.start()
    timer_bool = True
    return timer_bool

def stop():
    global wins
    global tries
    global result
    global timer_bool
    
    if timer.is_running():
        timer.stop()
    
    #0:00.0 -> stop at full second
    if displayed_time % 10 != 0 and timer_bool == True:
        tries += 1
    elif displayed_time % 10 == 0 and timer_bool == True:
        wins += 1
        tries += 1
    
    timer_bool = False
    
    result = str(wins)+'/'+str(tries)
    return result, timer_bool

def reset():
    global displayed_time 
    global wins
    global tries
    global timer_bool
    global result
    
    timer.stop()
    displayed_time = 0
    wins = 0
    tries = 0
    timer_bool = False
    result = '0/0'
    
    return displayed_time, wins, tries, timer_bool

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global displayed_time
    displayed_time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(result, [230, 50], 30, "orange")
    canvas.draw_text(format(displayed_time), [100, 150], 40, "yellow")
    
# create frame
frame = simplegui.create_frame("Timer", 300, 300)

# register event handlers
#buttons
frame.add_button("Start the timer", start, 200)
frame.add_button("Stop the timer", stop, 200)
frame.add_button("Reset the timer", reset, 200)

#canvas handlers
frame.set_draw_handler(draw)

#timer
timer = simplegui.create_timer(interval, timer_handler)

#label - first try... note to self -> how do I add enters? The text
#appears right below the buttons... for now, adding empty labels to
#move it down
label1 = frame.add_label("")
label2 = frame.add_label("")
label3 = frame.add_label("To win, stop the timer")
label4 = frame.add_label("on a whole second.")
label5 = frame.add_label("")
label6 = frame.add_label("")
label7 = frame.add_label("The timer will stop")
label8 = frame.add_label("after reaching 10 minutes.")

# start frame
frame.start()

# Please remember to review the grading rubric
