import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException



file_path = '/Users/visvamurali/Downloads/Contact Information ~ MAGIC (File responses)/Contact Information (Responses).xlsx'

df = pd.read_excel(file_path)
df['First Name'] = df['First Name'].str.strip()
df['Last Name'] = df['Last Name'].str.strip()
df['ISS DATE'] = df['ISS DATE'].dt.strftime('%m/%d/%Y')
df['Birthday (MM/DD/YYYY) - you are 21 right?\nremember include the slashes!'] = df['Birthday (MM/DD/YYYY) - you are 21 right?\nremember include the slashes!'].dt.strftime('%m/%d/%Y')
columns_to_modify = ['EYE COLOR?', 'HAIR COLOR? (choose whatever fits best)']  # List your columns here
df[columns_to_modify] = df[columns_to_modify].replace(r'\s+', '', regex=True)

#SET EVERYTHING UP AND LOGIN HERE!
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options) 
driver.get("https://magicfakes.ph/login")
driver.maximize_window()

print("LOGGING IN")

time.sleep(2)

email = driver.find_element("xpath", '//*[@id="container_body"]/div/div/div[3]/div/div/div[1]/input')
email.send_keys("bbccbb12@gmail.com")
password = driver.find_element("xpath", '//*[@id="container_body"]/div/div/div[3]/div/div/div[2]/input')
password.send_keys("12bbccbb")
login_button = driver.find_element("xpath", '/html/body/div[2]/div/div/div/div[3]/div/div/div[5]/button')
login_button.click()

print("SUCCESS")

time.sleep(2)
count = 0
ids = len(df)
for index, row in df.iterrows():
    count += 1
    print(f"{count}/{ids}")
    ordering = driver.get('https://magicfakes.ph/ordernow')

    wait = WebDriverWait(driver, 10)
    state = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container_body"]/div/div/div[1]/div/div/div[2]/select')))
    stateSelect = Select(state)
    stateOfFake = 'Michigan Driver License' # change this to whatever the person asks for!
    stateSelect.select_by_visible_text(stateOfFake) # set up options for this

    state = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="personial_information_date_6"]')))

    FirstName = driver.find_element('xpath', '//*[@id="container_body"]/div/div/div[2]/div/div/div/div/div[1]/input')
    MiddleName = driver.find_element('xpath', '//*[@id="container_body"]/div/div/div[2]/div/div/div/div/div[2]/input')
    LastName = driver.find_element('xpath', '//*[@id="container_body"]/div/div/div[2]/div/div/div/div/div[3]/input')
    dateOfBirth = driver.find_element('xpath', '//*[@id="personial_information_date_6"]')
    weight = driver.find_element('xpath', '//*[@id="container_body"]/div/div/div[2]/div/div/div/div/div[9]/input')
    StAdd = driver.find_element('xpath', '//*[@id="container_body"]/div/div/div[2]/div/div/div/div/div[10]/input')
    city = driver.find_element('xpath', '//*[@id="container_body"]/div/div/div[2]/div/div/div/div/div[11]/input')
    zipCode = driver.find_element('xpath', '//*[@id="container_body"]/div/div/div[2]/div/div/div/div/div[12]/input')
    iss = driver.find_element('xpath', '//*[@id="personial_information_date_1"]')


    #CHANGE ALL OF THIS BASED ON ETC
    firstName = row['First Name']
    FirstName.send_keys(f"{firstName}")
    middleName = row["Middle Name (LEAVE BLANK IF YOU DON'T HAVE ONE)"]
    MiddleName.send_keys()#f"{firstName}")
    lastName = row["Last Name"]
    LastName.send_keys(f"{lastName}")
    
    print(f"{firstName} {lastName} # . . . . STARTED . . . . #")
    
    DateofBirth = row['Birthday (MM/DD/YYYY) - you are 21 right?\nremember include the slashes!']
    dateOfBirth.send_keys(f"{DateofBirth}")
    Weight = row['WEIGHT (in pounds and a whole number)']
    weight.send_keys(f"{Weight}")
    stAdd = row["Street Address (like everything before the city) *EXAMPLE* - 382 Tallwood St"]
    StAdd.send_keys(f"{stAdd}")
    City = row["CITY YOU FROM: *EXAMPLE* : Centerville"]
    city.send_keys(f"{City}")
    ZipCode = row["ZIP CODE"]
    zipCode.send_keys(f"{ZipCode}")
    iSS = row["ISS DATE"]
    iss.send_keys(f"{iSS}")
    
    eyeColor = row["EYE COLOR?"]
    genderSel = row["Gender (Only male or Female)"]
    HairColor = row["HAIR COLOR? (choose whatever fits best)"]
    OrganDonor = row["Are you an organ donor?"]
    restrictions = "NO"
    Height = row["Height ? (if you're under 5 foot or over 7, no you're not just choose what fits best ig..)"]
    
    pictures = f"{firstName}_{lastName}.png"
    

    eyes = driver.find_element('xpath', '//*[@id="container_body"]/div/div/div[2]/div/div/div/div/div[5]/div/div').click()
    color  = driver.find_element('xpath', f'//*[@data-value="{eyeColor}"]').click()

    gender = driver.find_element('xpath', '//*[@id="container_body"]/div/div/div[2]/div/div/div/div/div[4]/div/div').click()
    genderClick  = driver.find_element('xpath', f'//*[@data-value="{genderSel}"]').click()

    hair = driver.find_element('xpath', '//*[@id="container_body"]/div/div/div[2]/div/div/div/div/div[6]/div/div').click()
    hairColor = driver.find_element('xpath', f"/html/body/div[2]/div/div/div/div[2]/div/div/div/div/div[6]/div/div/ul/li[@data-value='{HairColor}']").click()

    organ = driver.find_element(By.CSS_SELECTOR, '.nice-select.form-control.input-sm._select_23').click()
    organDonor = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='container_body']/div/div/div[3]/div/div/div/div/div[4]/div/div/ul/li[@data-value='{OrganDonor}']")))
    organDonor.click()

    restrictive = driver.find_element(By.CSS_SELECTOR, '.nice-select.form-control.input-sm._select_22').click()
    lens = wait.until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div/div/div/div[3]/div/div/div/div/div[3]/div/div/ul/li[@data-value='{restrictions}']")))
    lens.click()

    height = driver.find_element('xpath', '//*[@id="container_body"]/div/div/div[2]/div/div/div/div/div[8]/div/div').click()
    heightClick = driver.find_element(By.XPATH, f'//*[@data-value="{Height}"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", heightClick)
    heightClick.click()
    
    facePath = f"/Users/visvamurali/Downloads/Contact Information ~ MAGIC (File responses)/PICTURE OF FACE! - White background please (File responses)/{pictures}"
    signPath = f"/Users/visvamurali/Downloads/Contact Information ~ MAGIC (File responses)/SIGNATURE! - black pen white paper - only pictures accepted_ (File responses)/{pictures}"
    
    pictureFind = driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[4]/div[1]/div/div[1]/div/div[1]/div[2]/input')
    pictureSend = pictureFind.send_keys(facePath)
    
    wait = WebDriverWait(driver, 20)
    
    signatureClickable = EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[4]/div[1]/div/div[2]/div[1]/div[1]/div[2]/input'))
    signWait = wait.until(signatureClickable)
    
    signFind = driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[4]/div[1]/div/div[2]/div[1]/div[1]/div[2]/input')
    signSend = signFind.send_keys(signPath)
    
    print("Information in")
    
    # XPath for the progress bar
    face_progress_bar_xpath = "/html/body/div[2]/div/div/div/div[4]/div[1]/div/div[1]/div/div[2][contains(@class, 'progress-bar progress-bar-success')]"
    
    sign_progress_bar_xpath = "/html/body/div[2]/div/div/div/div[4]/div[1]/div/div[2]/div[1]/div[2][contains(@class, 'progress-bar progress-bar-success')]"
    
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, sign_progress_bar_xpath))
    )
    # Wait for the progress bar to be visible
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, face_progress_bar_xpath))
    )
    shopping_cart_button_xpath = '//*[@id="container_body"]/div/div/div[4]/div[2]/button[3]'

    # Wait for the overlay to disappear
    for i in range(3):
        time.sleep(4)
        print(f"waiting: {(i+1)*4} : 12 seconds")
    
    attempts = 8
    for i in range(attempts):
        try:
            shopping_cart_button = driver.find_element(By.XPATH, shopping_cart_button_xpath)
            driver.execute_script("arguments[0].scrollIntoView(true);", shopping_cart_button)
            shopping_cart_button.click()
            break
        except ElementClickInterceptedException:
            if i < attempts - 1:
                time.sleep(10)
                print("Failed attempt: couldn't add to cart - Trying again")
            else:
                print("failure")
    
    time.sleep(4)
    
    print("DONE")


print("%/\% . COMPLETE . %/\% . ")
driver.quit()