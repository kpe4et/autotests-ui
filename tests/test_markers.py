import pytest

@pytest.mark.smoke
def test_smoke_case():
    ...


@pytest.mark.regression
def test_regression_case():
    ...

@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        ...

    @pytest.mark.regression
    def test_case2(self):
        ...
        
@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_passwerd_reset(self):
        ...

    def test_logout(self):
        ...

@pytest.mark.regression
@pytest.mark.critical
@pytest.mark.smoke
def test_critical_login():
    ...

@pytest.mark.ui
class TestUserInterface:
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass
    
    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass