from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
driver = webdriver.Chrome()

#get source
def scrap_data():
    index = 0
    with open('cars1.csv', 'a', newline='') as cars:
        writer = csv.writer(cars)
        writer.writerow(('Model', 'Price')) 

        while index < 64:

            driver.get(f'https://www.carsguide.com.au/buy-a-car/all-new-and-used/all-states/all-locations/sedan/mazda?distanceFromMe=Sydney%2CNSW&searchOffset={index * 13}&searchLimit=13')

            models = driver.find_elements(By.CLASS_NAME,'carListing--textHeading')
            prices = driver.find_elements(By.CLASS_NAME,'carListing--textPrice')
            for i in range(len(models)):
                model = models[i].text
                price = prices[i].text
                writer.writerow((model, price))

            index = index + 1
    

# def scrap_data_auto():
#     driver.get('https://www.carsguide.com.au/buy-a-car/all-new-and-used/all-states/all-locations/sedan/mazda?distanceFromMe=Sydney%2CNSW&searchOffset=0&searchLimit=13')

#     pagination_element = driver.find_element(By.XPATH, '//*[@id="all-tab-content"]/div/div[4]/div[6]/ul/li[7]/a')

#     with open('cars1.csv', 'a', newline='') as cars:
#         writer = csv.writer(cars)
#         writer.writerow(('Model', 'Price'))
#         print(pagination_element.is_displayed())
#         pagination_element.click()
#         while pagination_element.is_displayed():
#             # scrap data
#             models = driver.find_elements(By.CLASS_NAME,'carListing--textHeading')
#             prices = driver.find_elements(By.CLASS_NAME,'carListing--textPrice')
#             for i in range(len(models)):
#                 model = models[i].text
#                 price = prices[i].text
#                 writer.writerow((model, price))
#             # go to next

#             #wait for page to load
#             driver.implicitly_wait(15)

    

if __name__ == '__main__':
        scrap_data()
        driver.quit()