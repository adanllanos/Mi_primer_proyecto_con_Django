from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Inicializar el navegador y abrir la URL
options = Options()
#options.add_argument('--headless')  # Ejecutar en modo headless para no mostrar la ventana del navegador
#driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

driver.get("www.google.com")

# Esperar a que la página cargue completamente
driver.implicitly_wait(20)

# Guardar la página en PDF
driver.execute_script("return window.print()")

# Cerrar el navegador
driver.quit()