🖥️ Realtime System Monitor

Realtime System Monitor es una aplicación web ligera que permite visualizar en tiempo real el uso de CPU, RAM y Disco de un sistema.
Desarrollada en Python (Flask) y con visualización mediante Chart.js, está diseñada como un ejemplo práctico de observabilidad y monitoreo en tiempo real.

Ideal para:

📊 Demostraciones técnicas de monitoreo y métricas en vivo.

🛠️ Prácticas fullstack (backend + frontend en un solo archivo).

🚀 Portafolio profesional para perfiles Cloud, DevOps, SysOps y Observabilidad.

🚀 Características

⚡ Backend en Flask: servidor ligero y rápido en Python.

📈 Gráficos dinámicos con Chart.js, actualizados cada 2 segundos.

🔎 Datos en vivo: métricas de CPU, RAM y Disco obtenidas con psutil.

🌐 API REST lista para integrarse:

/data → Devuelve métricas en JSON.

/metrics → Exporta métricas en formato Prometheus.

🖥️ Dashboard responsive: interfaz simple y moderna.

🛠️ Fácil despliegue: funciona en local, Codespaces o contenedores.

📦 Código minimalista en un solo archivo (app.py).

📂 Estructura del proyecto
realtime-system-monitor/
│
├── app.py            # Código principal (Flask + Chart.js + psutil)
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Documentación

⚙️ Instalación y ejecución
Opción 1 — Local (Python 3.9+)
# 1. Clonar el repositorio
git clone https://github.com/tuusuario/realtime-system-monitor.git
cd realtime-system-monitor

# 2. Instalar dependencias
pip install flask psutil

# 3. Ejecutar el servidor
python app.py


Accede a:

📊 Dashboard → http://localhost:5000

📡 Prometheus Metrics → http://localhost:5000/metrics

Opción 2 — GitHub Codespaces
pip install flask psutil
python app.py


Haz clic en "Open in Browser" cuando Codespaces te lo sugiera.

📡 API Endpoints
Endpoint	Método	Descripción
/	GET	Dashboard HTML con gráficos en vivo
/data	GET	Métricas en JSON (CPU, RAM, Disco)
/metrics	GET	Métricas en formato Prometheus
🛠️ Tecnologías utilizadas

🐍 Python 3

🌐 Flask → Backend web

⚙️ psutil → Métricas del sistema

📊 Chart.js → Visualización en tiempo real

📡 Prometheus exposition format → Integración con observabilidad avanzada

💡 Mejoras futuras

🔐 Autenticación y seguridad para el dashboard.

⚠️ Alertas por email/Slack cuando se superen umbrales críticos.

📦 Dockerfile para despliegue en contenedores.

📊 Persistencia de métricas en base de datos o integración con Prometheus/Grafana.

📜 Licencia

Este proyecto está bajo la licencia MIT.
Eres libre de usarlo, modificarlo y distribuirlo, citando la fuente original.

👨‍💻 Autor

Emanuel Gonzalez Michea

🌐 LinkedIn
https://www.linkedin.com/in/emanuel-gonzalez-michea/