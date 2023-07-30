import pyautogui
import webbrowser
import sys
import time


def main(title, url):
    for window in pyautogui.getAllWindows():
        print(window.title)
        if title in window.title and "Chrome" in window.title:
            print("Found window")
            window.activate()
            window.maximize()
            break
    else:
        # chrome.exe의 실제 경로로 변경해야 합니다.
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        chrome_browser = webbrowser.get(chrome_path)
        chrome_browser.open(url)
        # webbrowser.open(url)


if __name__ == "__main__":
    title = "ChatGPT - Chrome"
    url = "https://chat.openai.com/?model=gpt-4"

    if len(sys.argv) >= 2:
        title = sys.argv[1]
    if len(sys.argv) >= 3:
        url = sys.argv[2]

    main(title, url)
