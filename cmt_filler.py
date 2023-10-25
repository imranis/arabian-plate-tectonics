from selenium import webdriver
import time
import csv


def fill_form(row, web, writer):
    end_year = '2023'
    end_month = '10'
    end_day = '1'
    moment_mag = '5.0'
    minx, miny, maxx, maxy = row

    web.execute_script("window.open('https://www.globalcmt.org/CMTsearch.html');")
    web.switch_to.window(web.window_handles[-1])

    time.sleep(1)

    select_date = web.find_element_by_name('otype')
    select_date.click()

    year_element = web.find_element_by_name('oyr')
    year_element.clear()
    year_element.send_keys(end_year)

    month_element = web.find_element_by_name('omo')
    month_element.clear()
    month_element.send_keys(end_month)

    day_element = web.find_element_by_name('oday')
    day_element.clear()
    day_element.send_keys(end_day)

    moment_mag_element = web.find_element_by_name('lmw')
    moment_mag_element.send_keys(moment_mag)

    output_type = web.find_element_by_xpath('/html/body/form/p[4]/input[4]')
    output_type.click()

    minx_element = web.find_element_by_name('llon')
    minx_element.clear()
    minx_element.send_keys(minx)

    maxx_element = web.find_element_by_name('ulon')
    maxx_element.clear()
    maxx_element.send_keys(maxx)

    miny_element = web.find_element_by_name('llat')
    miny_element.clear()
    miny_element.send_keys(miny)

    maxy_element = web.find_element_by_name('ulat')
    maxy_element.clear()
    maxy_element.send_keys(maxy)

    submit = web.find_element_by_xpath('/html/body/form/p[4]/input[7]')
    submit.click()

    ####
    time.sleep(1)

    psmeca_data = web.find_element_by_xpath('/html/body/pre[2]')
    writer.writerow([psmeca_data.text + '\n'])


web = webdriver.Chrome()

with open('squares_coordinates.csv', 'r') as file, open('output.csv', 'w', newline='') as outfile:
    reader = csv.reader(file)
    writer = csv.writer(outfile)
    next(reader)  # Skip the header
    for row in reader:
        fill_form(row, web, writer)
