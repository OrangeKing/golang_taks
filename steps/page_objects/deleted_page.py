from page_objects.home_page import HomePage


class DeletedPage(HomePage):
    URI = "http://localhost:8081/deleted/"
    def __init__(self, driver):
        super(DeletedPage, self).__init__(driver)
