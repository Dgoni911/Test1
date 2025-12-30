import pytest


class TestLogin:
    
    @pytest.mark.parametrize("username,password", [
        ("standard_user", "secret_sauce"),
    ])
    def test_valid_login(self, login_page, username, password):

        inventory_page = login_page.login(username, password)
        
        assert inventory_page.is_displayed(), "Страница продуктов не отображается"
        
        assert "Products" in inventory_page.get_title(), \
            f"Ожидался заголовок 'Products', но получен: {inventory_page.get_title()}"
        
        # Шаг 4: Проверить URL
        assert "inventory" in inventory_page.get_current_url(), \
            f"URL не содержит 'inventory': {inventory_page.get_current_url()}"
        
        print(f"✓ Успешный вход пользователя: {username}")
    
    def test_invalid_login(self, login_page):

        login_page.login("invalid_user", "wrong_password")
        
        error_message = login_page.get_error_message()
        assert error_message is not None, "Сообщение об ошибке не отображается"
        assert "Username and password do not match" in error_message, \
            f"Неверное сообщение об ошибке: {error_message}"
        
        print("✓ Корректное сообщение об ошибке при неверном входе")