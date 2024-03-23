import pyautogui
import time
def automate():
    time.sleep(3)

    browser = "./pic/browser.png"
    # browsericn = pyautogui.locateOnScreen(browser)
    pyautogui.click()
    # pyautogui.click(browsericn, interval=2)

    for i in range(45):
        playbtnimg = "./pic/play.png"
        playbtn = pyautogui.locateOnScreen(playbtnimg)
        pyautogui.click(playbtn, interval=2)

        nextvidbtnimg = "./pic/nextvid.png"
        nextvidbtn = pyautogui.locateOnScreen(nextvidbtnimg, minSearchTime=25)
        pyautogui.click(nextvidbtn, interval=2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    automate()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
