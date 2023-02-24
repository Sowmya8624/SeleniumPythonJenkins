import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class MyTestCase(unittest.TestCase):

    def test01(self):

        filePath = "C:\\Users\\SOAELE\\PycharmProjects\\SeleniumPythonProject\\drivers\\chromedriver.exe"
        url = "https://parabank.parasoft.com/parabank/index.htm"

        driver = webdriver.Chrome(filePath)

        time.sleep(1)
        driver.get(url)

        time.sleep(1)

        # Page text
        footerTextElement = driver.find_element(By.CLASS_NAME, "copyright")

        footerTextValue = footerTextElement.text

        print(footerTextValue)
        time.sleep(1)


        # Page text with tag
        textElement = driver.find_element(By.TAG_NAME, "h2")

        textElementValue = textElement.text

        print(textElementValue)
        time.sleep(1)

        # User entered tag
        # GetAttribute(value)

        usernameTextBox = driver.find_element(By.NAME, "username")

        usernameTextBox.send_keys("John")

        enteredText = usernameTextBox.get_attribute("value")

        print(enteredText)
        time.sleep(1)

        # Link text
        textLink = driver.find_element(By.LINK_TEXT, "Forgot login info?")

        textLinkValue = textLink.text

        print(textLinkValue)
        time.sleep(1)

        # All links text
        linkList = driver.find_elements(By.TAG_NAME, "a")

        for i in linkList:
            print(i.text)

        print("****************************************")
        time.sleep(1)

        # GetAttribute(href)
        for i in linkList:
            print(i.get_attribute("href"))
        print("****************************************")
        time.sleep(1)

        driver.get("https://www.facebook.com/")
        time.sleep(1)

        # GetAttribute(placeholder)
        email = driver.find_element(By.NAME, "email")

        placeHolderText = email.get_attribute("placeholder")

        print(placeHolderText)

        time.sleep(1)
        driver.quit()
if __name__ == '__main__':
    unittest.main()