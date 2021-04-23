from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Initiate the browser and go to LinkedIn

options = Options();
options.add_argument("--incognito");

browser  = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options);
browser.get('https://www.linkedin.com/');

# Implicitly wait for up to 20 seconds for each element
browser.implicitly_wait(20);

# Retrieve log in info from text file
file = open('private.txt', 'r');
lines = file.readlines();
email = lines[0];
password = lines[1];

if email[-1] == '\n':
    email = email[0:-1];
    
if password[-1] == '\n':
    password = password[0:-1];

# Fill credentials
browser.find_element_by_name('session_key').send_keys(email);
browser.find_element_by_name('session_password').send_keys(password);

# Click Log In
browser.find_element_by_class_name('sign-in-form__submit-button').click();

# # Remember Me? -> Click Not Now
# rmbr = browser.find_element_by_xpath('//*[@id="remember-me-prompt__form-secondary"]/button');
# if(rmbr):
#     rmbr.click();

# Click Jobs
browser.find_element_by_xpath('//*[@id="primary-navigation"]/ul/li[3]').click();

# Quit
browser.quit();