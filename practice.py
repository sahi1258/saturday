# Import the Selenium WebDriver module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create a WebDriver instance (in this case, for Chrome)
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.w3schools.com/")

# Wait for a few seconds (useful for letting the page load)
driver.implicitly_wait(5)


# Close the browser
driver.quit()

  
