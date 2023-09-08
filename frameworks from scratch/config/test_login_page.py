class LoginPage:
    def open_url(self, param):
        pass


def test_valid_login(driver, config):
    login_page = LoginPage()
    login_page.open_url(config.get("WebAppConfig", "base_url"))
