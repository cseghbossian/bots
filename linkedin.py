from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Initiate the browser and go to LinkedIn
browser  = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.linkedin.com/')

# Retrieve log in info from text file
file = open('private.txt', 'r')
lines = file.readlines()
email = lines[0]
password = lines[1][0:-1]

if email[-1] == '\n':
    email = email[0:-1]
    
if password[-1] == '\n':
    password = password[0:-1]

# Fill credentials
browser.find_element_by_name('session_key').send_keys(email);
browser.find_element_by_name('session_password').send_keys(password);

# Click Log In
browser.find_element_by_class_name('sign-in-form__submit-button').click();


