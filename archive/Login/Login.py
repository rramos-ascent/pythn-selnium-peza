try:
    InputUserName = driver.find_element(By.XPATH, '//input[@id="username"]')
    InputUserName.send_keys("RUSSELRAMOS0001")
    print("Username Input")
    #return 1
except NoSuchElementException:
    print("Element Not found! Test Fail")
    #return 0

try:
    InputPassword = driver.find_element(By.XPATH, '//input[@id="password"]')
    InputPassword.send_keys("RUSSELRAMOS0001")
    print("Password Input")
    #return 1
except NoSuchElementException:
    print("Element Not found! Test Fail")
    #return 0

try:
    ProceedLogin = driver.find_element(By.XPATH, '//button[@class="btn btn-primary d-grid w-100"]')
    driver.execute_script("arguments[0].click();", ProceedLogin)
    print("Login Initiated")
    try:
        driver.find_element(By.XPATH, '//html[@class="light-style layout-navbar-fixed layout-menu-fixed layout-footer-fixed"]')
        print("Login Success")
        #return 1
    except NoSuchElementException:
        print("Login failed")
        #return 0
except NoSuchElementException:
    print("Element Not found! Test Fail")
    #return 0

time.sleep(5)

try:
    imgUserAvatar = driver.find_element(By.XPATH, '//html//body//div[2]//div[1]//div//div//nav//div[2]//ul//li[5]//a//div//img')
    driver.execute_script("arguments[0].click();", imgUserAvatar)
    print("Avatar Listings")
except NoSuchElementException:
    print("Element Not found! Test Fail")
    #return 0

time.sleep(5)

try:
    imgUserAvatarLogin = driver.find_element(By.XPATH, '//html//body//div[2]//div[1]//div//div//nav//div[2]//ul//li[5]//ul//li[10]//a//span')
    driver.execute_script("arguments[0].click();", imgUserAvatarLogin)
    print("Initiate Logout")
except NoSuchElementException:
    print("Element Not found! Test Fail")
    #return 0

time.sleep(5)