import ctypes
import time
import sys

def show_reminder():
    # MessageBoxW: (hwnd, text, caption, utype)
    # utype values: 
    # 0x40 (MB_ICONINFORMATION) - Shows the information bubble icon.
    # 0x40000 (MB_TOPMOST) - Forces the window to display on top of all other windows.
    ctypes.windll.user32.MessageBoxW(
        0, 
        "Time to stand up, stretch, and look away from the screen! 🚶‍♂️✨", 
        "Stretch & Stand Reminder", 
        0x40 | 0x40000
    )

if __name__ == "__main__":
    print("Stretch Reminder application started successfully!")
    print("Press Ctrl+C in the terminal to exit the script.")
    
    # 5-second delay for testing, so the popup is seen immediately during testing
    print("\n[TEST MODE] Displaying the first reminder in 5 seconds...")
    time.sleep(5)
    show_reminder()
    print("[TEST MODE] First reminder completed. Entering 30-minute interval loop...")
    
    # 30-minute loop interval (30 minutes * 60 seconds = 1800 seconds)
    interval = 1800 
    
    try:
        while True:
            time.sleep(interval)
            show_reminder()
    except KeyboardInterrupt:
        print("\nExiting Stretch Reminder. Stay healthy!")
        sys.exit(0)
