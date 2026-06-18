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
| `test_eliminar_producto_del_carrito` | Verifica que un producto se puede eliminar del carrito y el contador se actualiza correctamente |
| `test_ordenar_por_precio_menor_a_mayor` | Verifica que el ordenamiento de productos por precio funcione correctamente |
| `test_checkout_completo` | Test E2E: simula el flujo completo de compra, desde login hasta la confirmación del pedido |
| `test_agregar_varios_productos_al_carrito` | Verifica que se pueden agregar múltiples productos y que el carrito refleje la cantidad y el contenido correcto |

## 📂 Estructura del proyecto

```
mis-test/
├── conftest.py                    # Fixture que gestiona el navegador (setup/teardown)
├── test_login.py                  # Caso de login exitoso
├── test_login_fallido.py          # Caso de login con credenciales incorrectas
├── test_usuario_bloqueado.py      # Caso de usuario bloqueado
├── test_carrito.py                # Caso de agregar producto al carrito
├── test_eliminar_carrito.py       # Caso de eliminar producto del carrito
├── test_ordenar_productos.py      # Caso de ordenamiento por precio
├── test_checkout_completo.py      # Test E2E de flujo de compra completo
└── README.md
```

## 📌 Buenas prácticas aplicadas

- Uso de **esperas explícitas** (`WebDriverWait`) en lugar de esperas fijas (`sleep()`)
- **Fixtures de Pytest** para evitar duplicar código de configuración del navegador
- Separación de casos positivos y negativos
- Nomenclatura clara y descriptiva en cada test

## 👤 Autor

**Tomás Illanes**  
QA Analyst con +4 años de experiencia, en proceso de especialización en automatización de pruebas.

[LinkedIn](https://www.linkedin.com/in/tom%C3%A1s-illanes-vidal-6711b557/) · [GitHub](https://github.com/tomasillanes-tech)