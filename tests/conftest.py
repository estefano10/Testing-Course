import pytest
import selenium.webdriver

@pytest.fixture
def browser():
    #Inicializar la instancia de ChromeDriver
    b = selenium.webdriver.Chrome()

    #Hacemos una espera de 10seg para que los elementos aparezcan
    b.implicitly_wait(10)

    #Retornamos la instancia de WebDriver para la configuracion
    yield b

    #Cerramos la instancia para limpiar
    b.quit()