class Config:
    url = "https://wikipedia.org"
    ext = "wiki"


class Wikipedia:
    info = "World War 1"
    search_field_id = "searchInput"
    search_button_id = '//*[@id="search-form"]/fieldset/button/i'
    expected_element = "Verden"

    def __init__(self, url):
        self.url = f'{url}'
