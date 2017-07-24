from page_objects.home_page import HomePage


class CompletedPage(HomePage):
    URI = "{}completed/".format(HomePage.URI)
    def __init__(self, driver):
        super(CompletedPage, self).__init__(driver)
