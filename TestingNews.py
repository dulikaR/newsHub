from selenium import webdriver

class A:
    def start(self, driver):
        newsTypes = (
        'http://www.hirunews.lk/', 'http://www.hirunews.lk/local-news.php', 'http://www.hirunews.lk/entertainment/',
        'http://www.hirunews.lk/international-news.php', 'http://www.hirunews.lk/sports/',
        'http://www.hirunews.lk/business/')
        for i in newsTypes:
            print i
            self.loopmethod( i, driver )

    def loopmethod(self, type, driver):
        driver.get(type)
        print 'done'
        mainBar = driver.find_elements_by_css_selector( '.rp-mian' )

        for webElement in mainBar:
            print webElement
            barHeader = webElement.find_element_by_css_selector( '.lts-cntp a' )
            barContent = webElement.find_element_by_css_selector( '.lts-txt2' )
            print barHeader.get_attribute('text')
            print barContent.get_attribute('text')
        print "one finished"
        # driver.implicitly_wait(10000)
        # Thread.sleep(100000)


driver = webdriver.Chrome( "C:\chromedriver.exe" )
a = A()
a.start( driver )



