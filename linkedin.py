from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initiate the browser and go to LinkedIn
options = Options();
options.add_argument("--incognito");

browser  = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options);
browser.get('https://www.linkedin.com/');

# Implicitly wait for up to 5 seconds per element
browser.implicitly_wait(5);

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
try:
    browser.find_element_by_xpath('//*[@id="remember-me-prompt__form-secondary"]/button').click();
except:
    print("BOT: No Remember Me prompt.");

# Click Jobs
browser.find_element_by_xpath('//*[@id="primary-navigation"]/ul/li[3]').click();

# Retrieve Search Criteria from text file
role = lines[2];
location = lines[3];

if role[-1] == '\n':
    role = role[0:-1];
    
if location[-1] == '\n':
    location = location[0:-1];

# Close Messages
messages = browser.find_elements_by_class_name('msg-overlay-bubble-header__control');
messages[1].click();

# Search
search_box = browser.find_elements_by_class_name('jobs-search-box__text-input');
search_box[0].send_keys(role);
search_box[3].send_keys(location);

browser.find_element_by_class_name('jobs-search-box__submit-button').click();

# Filter Search
filters = browser.find_elements_by_class_name('artdeco-pill');
##   0    |  Jobs               //
##   1    |  Date Posted        //
##   2    |  Experience Level   
##   3    |  Company            //
##   4    |  Job Type           
##   5    |  Remote             //
##   6    |  Easy Apply         //
##   7    |  All Filters        //

## Date Posted
filters[1].click();
### Past 24 Hours
browser.find_element_by_xpath("//label[@for='timePostedRange-r86400']").click();
filters[1].click();
time.sleep(5);

## Experience Level
filters = browser.find_elements_by_class_name('artdeco-pill');
print(len(filters));
filters[2].click();
time.sleep(5);
### Internship
browser.find_element_by_xpath("//label[@for='experience-1']").click();
time.sleep(2);
### Entry Level
browser.find_element_by_xpath("//label[@for='experience-2']").click();
time.sleep(2);
### Associate 
browser.find_element_by_xpath("//label[@for='experience-3']").click();
time.sleep(2);
filters[2].click();



# ## Easy Apply
# filters = browser.find_elements_by_class_name('artdeco-pill');
# filters[6].click();


# # Quit
# time.sleep(5);
# file.close();
# browser.quit();
# print("BOT: Quit successfully.\n");
