+35# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


class LinkedInBot:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
    
    def closeBrowser(self):
        self.driver.close()
        

    def login(self):    
        driver = self.driver
        driver.get("https://www.linkedin.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath("/html/body/nav/a[3] ")
        login_button.click()
        user_name_elem = driver.find_element_by_xpath("//input[@name='session_key']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='session_password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(4)
        #"//input[@name='session_key']"
        #"//input[@name='session_password']"
        #html body.global-alert-transition nav.nav a.nav__button-secondary
        #/html/body/nav/a[3]
        #
    def click_friends(self):
        driver = self.driver
        friends_tab = driver.find_element_by_xpath('//*[@id="mynetwork-tab-icon"]')
        friends_tab.click()
        time.sleep(4) 
        accept_button = driver.find_elements_by_css_selector('button.invitation-card__action-btn:nth-child(2)') 
        
        for friends in accept_button:
            friends.click() 
            time.sleep(1)
        
        
    def look_for_jobs(self,job_title):
        
        driver = webdriver.Firefox()
        driver.get("https://www.linkedin.com/jobs/search/?keywords=" + job_title + "&location=Barcelona%20Area%2C%20Spain&locationId=es%3A5064")
        all_jobs = driver.find_elements_by_class_name("result-card__full-card-link")
        links = [a.get_attribute('href') for a in all_jobs ]
        #time.sleep(5)
        #experience = driver.find_elements_by_class_name('filter-button-dropdown__icon')
        #experience[1].click()
        #time.sleep(5)
        #entry_level = driver.find_element_by_xpath('//*[@id="EXPERIENCE-0"]')
        #entry_level.click()
        
        
        
        
        
        return links
      
        
        
JoseLink = LinkedInBot('username' ,'password' )

#JoseLink.login()

#JoseLink.closeBrowser()

links = JoseLink.look_for_jobs('Data Science')





#//*[@id="jobs-search-box-keyword-id-ember99"]
# #jobs-search-box-keyword-id-ember99

#html.artdeco body.render-mode-BIGPIPE.nav-v2.ember-application.boot-complete.icons-loaded header#extended-nav.extended-nav.nav-main-container.global-alert-offset-top.nav--compact div.nav-main__content.full-height.display-flex.align-items-center form#extended-nav-search.nav-search div.nav-search-bar div#nav-typeahead-wormhole div div#ember99.jobs-search-box.ember-view div.jobs-search-box__input.jobs-search-box__input--keyword artdeco-typeahead-deprecated#ember101.ember-view artdeco-typeahead-deprecated-input#ember102.ember-view input#jobs-search-box-keyword-id-ember99 ç

#


