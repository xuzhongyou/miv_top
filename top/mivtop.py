import sys,os
import curses
from .nvi import nv_info

header = [
    '╒═════════════════════════════════════════════════════════════════════════════╕',
    '│ Processes:                                                                  │',
    '│ GPU  PID  USER   G_MEM  %CPU  %MEM     S_TIME   R_TIME      COMMAND         │',
    '╞═════════════════════════════════════════════════════════════════════════════╡',
]
line1 = '├─────────────────────────────────────────────────────────────────────────────┤'
line2 = '|_____________________________________________________________________________|' 
line3 = '╞═════════════════════════════════════════════════════════════════════════════╡'
info = nv_info()
def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        # width 120, height 30
        height, width = stdscr.getmaxyx()
        # height,width = 6,79

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        title = "GPU Resources Usage "[:width-1]
        subtitle = "Written by Xiaoke Hu"[:width-1]
        keystr = "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        # start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        # start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_x_content = int((width // 2)- (len(header[0])//2)-len(header[0])%2)
        # start_y = int((height // 2) - 2)
        start_y = 5
        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        # stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)
        stdscr.addstr(int(0.8*height), int(0.8*width), subtitle)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text

        dis_pos = 0
        for i,item in enumerate(header):
            stdscr.addstr(int(0.3*height)+i, start_x_content, item)
            dis_pos = int(0.3*height)+i
        dis_pos +=1
        for i,item in enumerate(info.keys()):
            pid = item
            item = info[item]
            stdscr.addstr(dis_pos, start_x_content+2,
                str(item[0])+"  "+str(pid)+"  "+str(item[1])+"  "+str(item[2])+"MiB  "+str(item[3])+"  "+str(format(item[4],'.2f'))+"  "+str(item[5])[:10] +"  "+ str(format(item[-2]/60,'.1f'))+"     "+ str(item[-1][:15]))
            dis_pos +=1
            stdscr.addstr(dis_pos, start_x_content,line3)
            dis_pos +=1
        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()
        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()