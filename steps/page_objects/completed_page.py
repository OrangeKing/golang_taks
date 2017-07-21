from page_objects.home_page import HomePage


class CompletedPage(HomePage):
    URI = "http://localhost:8081/completed/"
    def __init__(self, driver):
        super(CompletedPage, self).__init__(driver)
