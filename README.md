# Pruebas Automatizadas - Sistema de Prácticas de Campo
Conjunto de pruebas automatizadas para la interfaz web del "Sistema de Prácticas de Campo". El objetivo principal es validar el correcto funcionamiento de la página de inicio de sesión, comprobando la carga de la interfaz y verificando los flujos de autenticación tanto con credenciales válidas como inválidas.
---
## Tecnologías utilizadas
- Lenguaje: Python
- Framework de Pruebas: Pytest 
- Herramienta de Automatización: Selenium WebDriver
- Navegador Web de Prueba: Google Chrome
---
## Instalación
1. Clonar o descargar el proyecto: Asegurarse de tener todos los scripts .py en un mismo directorio local.
2. Instalar Python
3. Instalar dependencias: Abrir una terminal en la carpeta del proyecto e instalar Selenium y Pytest usando pip, por ejemplo: pip install selenium pytest
4. Navegador Web: Asegurarse de tener Google Chrome instalado en el equipo, ya que los scripts utilizan el controlador específico para este navegador (webdriver.Chrome()).
---
## Ejecutar sistema
Se puede ejecutar las pruebas de dos maneras dependiendo del script:
Para el script completo del Pytest: pytest ejemploPytest.py -v
Para los demás scripts: python ejemploCarga.py
—
## Uso del sistema
Al ejecutar los scripts, se abrirá automáticamente una ventana de Google Chrome. El sistema navegará a la URL del proyecto (https://alexanderggfi.github.io/IS2026-2-Sistema-de-Practicas-de-Campo/), ingresará datos en los campos de texto simulando a un usuario real, hará clic en el botón de ingresar y verificará los resultados en pantalla. Es de suma importancia NO interactuar con la ventana del navegador mientras las pruebas estén corriendo.
---
## Funcionalidades principales
- Verificación de carga: Comprueba que la página principal cargue correctamente validando el título de la pestaña ("Login").
- Validación de Login Exitoso: Simula el ingreso con credenciales correctas y verifica que el sistema redirija al usuario a principal.html.
- Validación de Login Fallido: Simula el ingreso con correos o contraseñas incorrectas y verifica que el sistema arroje el mensaje "Credenciales incorrectas".
- Captura de errores automática: Si una prueba con Pytest falla, o si el script de error se ejecuta, el sistema toma automáticamente una captura de pantalla del navegador.
---
## Evidencias
Todas las capturas de pantalla generadas por pruebas fallidas o validaciones de errores se almacenan automáticamente en la carpeta llamada evidencias/.
---
## Estructura del proyecto
TESTING/
│
|── evidencias/                   
│   └── testLoginFallido.png         
└── test/                            
    |── __pycache__/                 
    |── .pytest_cache/               
    |── evidencias/                  
    |── ejemploBusqueda.py           
    |── ejemploCarga.py              
    |── ejemploLoginCorrecto.py      
    |── ejemploLoginIncorrecto.py    
    └── ejemploPytest.py            
---
## Notas adicionales
- Conexión a Internet: Es indispensable contar con conexión a internet para que el WebDriver pueda acceder a la página alojada en GitHub Pages.
