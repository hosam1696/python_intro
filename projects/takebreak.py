import webbrowser
import time

total_breaks = 3
break_count = 0

while total_breaks<break_count:
    time.sleep(10)
    # Read a blog
    webbrowser.open('https://study.com/academy/lesson/what-is-random-access-memory-ram-definition-history-quiz.html')
    break_count+=1
