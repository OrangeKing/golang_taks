from page_objects.home_page import HomePage


class DeletedPage(HomePage):
    URI = "{}deleted/".format(HomePage.URI)
    def __init__(self, driver):
        super(DeletedPage, self).__init__(driver)
