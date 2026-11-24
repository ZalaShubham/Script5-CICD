
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def run_test(browser_name):

    print(f"\n--- Running test on {browser_name} ---")

    # Select browser
    if browser_name == "Chrome":
        driver = webdriver.Chrome()

    elif browser_name == "Firefox":
        driver = webdriver.Firefox()

    elif browser_name == "Edge":
        driver = webdriver.Edge()

    # Browser settings
    driver.implicitly_wait(10)
    driver.maximize_window()

    start_time = time.time()

    # Open website
    driver.get("https://www.saucedemo.com")

    # Enter login details
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click login button
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Get page title
    title = driver.title
    print(f"{browser_name} - Page Title: {title}")

    # Verify successful login
    try:
        logo = driver.find_element(By.CLASS_NAME, "app_logo")

        if logo.is_displayed():
            print(f"{browser_name} - Test Passed")
        else:
            print(f"{browser_name} - Test Failed")

    except Exception:
        print(f"{browser_name} - Test Failed")

    # Calculate execution time
    end_time = time.time()

    print(
        f"{browser_name} - Time Taken: "
        f"{round(end_time - start_time, 2)} seconds"
    )

    time.sleep(4)

    # Close browser
    driver.quit()


# Run test on all three browsers
run_test("Chrome")
run_test("Firefox")
run_test("Edge")

print("\nAll browser tests completed!")
