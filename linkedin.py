from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Initiate the browser and go to LinkedIn
browser  = webdriver.Chrome(ChromeDriverManager().install());
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

# Remember Me? -> Click Not Now
browser.find_element_by_xpath('//*[@id="remember-me-prompt__form-secondary"]/button').click();

# Click Jobs