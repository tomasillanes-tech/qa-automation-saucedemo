# QA Automation - SauceDemo

Suite de automatización de pruebas funcionales sobre [SauceDemo](https://www.saucedemo.com/), un sitio de práctica para QA. Proyecto desarrollado para aplicar y demostrar habilidades de automatización con Python, Selenium y Pytest.

## 🛠️ Tecnologías utilizadas

- **Python 3.14**
- **Selenium WebDriver** - automatización del navegador
- **Pytest** - framework de testing y organización de casos
- **WebDriver Manager** - gestión automática de drivers del navegador

## ✅ Casos de prueba incluidos

| Test | Descripción |
|------|-------------|
| `test_login_exitoso` | Verifica que un usuario válido puede iniciar sesión correctamente |
| `test_login_credenciales_incorrectas` | Verifica que el sistema rechaza credenciales inválidas con el mensaje de error correspondiente |
| `test_usuario_bloqueado` | Verifica que un usuario bloqueado no puede iniciar sesión |
| `test_agregar_producto_al_carrito` | Verifica el flujo de login y agregado de un producto al carrito de compras |

## 📂 Estructura del proyecto

## 🚀 Cómo ejecutar los tests

1. Clonar el repositorio
```bash
git clone https://github.com/tomasillanes-tech/qa-automation-saucedemo.git
cd qa-automation-saucedemo
```

2. Instalar dependencias
```bash
pip install selenium pytest webdriver-manager
```

3. Ejecutar toda la suite
```bash
pytest -v
```

## 📌 Buenas prácticas aplicadas

- Uso de **esperas explícitas** (`WebDriverWait`) en lugar de esperas fijas (`sleep()`)
- **Fixtures de Pytest** para evitar duplicar código de configuración del navegador
- Separación de casos positivos y negativos
- Nomenclatura clara y descriptiva en cada test

## 👤 Autor

**Tomás Illanes**  
QA Analyst con +4 años de experiencia, en proceso de especialización en automatización de pruebas.

[LinkedIn](https://www.linkedin.com/in/tom%C3%A1s-illanes-vidal-6711b557/) ·
