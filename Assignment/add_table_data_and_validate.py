import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://testpages.herokuapp.com/styled/tag/dynamic-table.html"
original_data = '[{"name": "Bob", "age": 20, "gender": "male"}, {"name": "George", "age": 42, "gender": "male"}, {"name": "Sara", "age": 42, "gender": "female"}, {"name": "Conor", "age": 40, "gender": "male"}, {"name": "Jennifer", "age": 42, "gender": "female"}]'
original_data_list = json.loads(original_data)
try:
    driver.get(url)
    time.sleep(5)
    table_button = driver.find_element(By.XPATH, '/html/body/div/div[3]/details/summary')
    time.sleep(5)
    table_button.click()
    time.sleep(10)
    json_data = driver.find_element(By.ID, 'jsondata')
    time.sleep(5)
    json_data.clear()
    json_data.send_keys(original_data)
    time.sleep(10)
    refresh_button = driver.find_element(By.XPATH, '//*[@id="refreshtable"]')
    refresh_button.click()
    time.sleep(5)
    print("Origina_data_list", original_data_list)
    table = driver.find_element(By.ID, 'dynamictable')

    name = []
    age = []
    gender = []

    rows = table.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')

        if len(cells) >= 3:
            name.append(cells[0].text)
            age.append(cells[1].text)
            gender.append(cells[2].text)

    stored_data = []
    for name, age, gender in zip(name, age, gender):
        entry = {'name': name, 'age': int(age), 'gender': gender}
        stored_data.append(entry)
    assert stored_data == original_data_list, "Data mismatch detected"

    print("Data on the webpage matches the original data.")


except Exception as e:
    print(f"An error occurred: {e}")
