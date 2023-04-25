import webbrowser
import time

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Roll URL
n = 30

while True:
    for i in range(n):
        webbrowser.open_new_tab(url)
    time.sleep(60)  # wait for 1 minute before restarting the loop
