import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def login():
    driver.get("https://rewards.microsoft.com/")

    email = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "loginfmt")))
    email.send_keys(Email)

    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    next_button.click()

    pwd = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "i0118")))
    pwd.send_keys(Password)

    sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    sign_in_button.click()

    stay_signed_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    stay_signed_in_button.click()

def finish_rewards():
    try:
        RewardsButton = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card-group.ng-scope:nth-child(7) > div:nth-child(1) > mee-card:nth-child(1) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-daily-set-item-content:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton)
        RewardsButton.click()
        print("Successfully clicked on the first rewards button.")

        time.sleep(1)
        
        RewardsButton2 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card-group.ng-scope:nth-child(7) > div:nth-child(1) > mee-card:nth-child(2) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-daily-set-item-content:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton2)
        RewardsButton2.click()
        print("Successfully clicked on the second rewards button.")
    
        time.sleep(1)

        RewardsButton3 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card-group.ng-scope:nth-child(7) > div:nth-child(1) > mee-card:nth-child(3) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-daily-set-item-content:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton3)
        RewardsButton3.click()
        print("Successfully clicked on the third rewards button.")

        time.sleep(1)

        RewardsButton4 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#more-activities > div:nth-child(1) > mee-card:nth-child(1) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton4)
        RewardsButton4.click()
        print("Successfully clicked on the fourth rewards button.")

        time.sleep(1)

        RewardsButton5 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#more-activities > div:nth-child(1) > mee-card:nth-child(2) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton5)
        RewardsButton5.click()
        print("Successfully clicked on the fifth rewards button.")

        time.sleep(1)

        RewardsButton6 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#more-activities > div:nth-child(1) > mee-card:nth-child(3) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton6)
        RewardsButton6.click()
        print("Successfully clicked on the sixth rewards button.")

        time.sleep(1)

        RewardsButton7 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#more-activities > div:nth-child(1) > mee-card:nth-child(4) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton7)
        RewardsButton7.click()
        print("Successfully clicked on the seventh rewards button.")

        time.sleep(1)

        RewardsButton8 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(5) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton8)
        RewardsButton8.click()
        print("Successfully clicked on the eighth rewards button.")
    
        time.sleep(1)

        RewardsButton9 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(6) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton9)
        RewardsButton9.click()
        print("Successfully clicked on the ninth rewards button.")


        time.sleep(1)

        # RewardsButton10 = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(7) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        # )
        # driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton10)
        # RewardsButton10.click()
        # print("Successfully clicked on the tenth rewards button.")

        # time.sleep(1)

        # RewardsButton11 = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(8) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        # )
        # driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton11)
        # RewardsButton11.click()
        # print("Successfully clicked on the eleventh rewards button.")

        # time.sleep(1)

        # RewardsButton12 = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(9) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        # )
        # driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton12)
        # RewardsButton12.click()
        # print("Successfully clicked on the twelfth rewards button.")

        # time.sleep(1)

        # RewardsButton13 = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(10) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        # )
        # driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton13)
        # RewardsButton13.click()
        # print("Successfully clicked on the thirteenth rewards button.")

        # time.sleep(1)

        # RewardsButton14 = WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(11) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        # )
        # driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton14)
        # RewardsButton14.click()
        # print("Successfully clicked on the fourteenth rewards button.")

        # time.sleep(1)

        RewardsButton15 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(12) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton15)
        RewardsButton15.click()
        print("Successfully clicked on the fifteenth rewards button.")

        time.sleep(1)

        RewardsButton16 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(13) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton16)
        RewardsButton16.click()
        print("Successfully clicked on the sixteenth rewards button.")

        time.sleep(1)

        RewardsButton17 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(14) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton17)
        RewardsButton17.click()
        print("Successfully clicked on the seventeenth rewards button.")

        time.sleep(1)

        RewardsButton18 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(15) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton18)
        RewardsButton18.click()
        print("Successfully clicked on the eighteenth rewards button.")

        time.sleep(1)

        RewardsButton19 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(16) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton19)
        RewardsButton19.click()
        print("Successfully clicked on the nineteenth rewards button.")

        time.sleep(1)

        RewardsButton20 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(17) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton20)
        RewardsButton20.click()
        print("Successfully clicked on the twentieth rewards button.")

        time.sleep(1)

        RewardsButton21 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(18) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton21)
        RewardsButton21.click()
        print("Successfully clicked on the twenty-first rewards button.")

        time.sleep(1)

        RewardsButton22 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(19) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton22)
        RewardsButton22.click()
        print("Successfully clicked on the twenty-second rewards button.")

        time.sleep(1)

        RewardsButton23 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "mee-card.ng-scope:nth-child(20) > div:nth-child(1) > card-content:nth-child(1) > mee-rewards-more-activities-card-item:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(4) > span:nth-child(1)"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", RewardsButton23)
        RewardsButton23.click()
        print("Successfully clicked on the twenty-third rewards button.")

        time.sleep(1)

    except Exception as e:
        print('Error:', str(e))

def main():
    login()
    print(f"Logged in as: {Email}")
    time.sleep(1.77)
    finish_rewards()

if __name__ == "__main__":
    Email = input(f"Enter Your Email: ")
    Password = input(f"Enter Your Password: ")
    driver = webdriver.Firefox()
    main()
    time.sleep(10)
    driver.quit()