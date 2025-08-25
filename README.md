# 🖥️ Realtime System Monitor

**Realtime System Monitor** es una aplicación web ligera que permite visualizar en tiempo real el uso de **CPU**, **RAM** y **Disco** de un sistema.  
Está desarrollada en **Python (Flask)** y utiliza **Chart.js** para renderizar gráficos interactivos en el navegador.

Este proyecto es ideal para:
- 📊 **Demostraciones técnicas** de monitoreo en tiempo real.
- 🛠️ **Prácticas de backend y frontend** en un solo archivo.
- 🚀 **Portafolio profesional** para perfiles Cloud, DevOps, SysOps y Observabilidad.

---

## 🚀 Características

- **Backend en Flask**: Servidor ligero y rápido en Python.
- **Gráficos en tiempo real**: Integración con Chart.js para actualizar cada 2 segundos.
- **Datos del sistema**: Uso de CPU, memoria RAM y disco vía `psutil`.
- **API REST**:
  - `/data` → Devuelve datos en formato JSON.
  - `/metrics` → Devuelve métricas en formato Prometheus.
- **Fácil despliegue**: Ejecutable localmente o en GitHub Codespaces sin configuración extra.
- **Código en un solo archivo (`app.py`)** para máxima simplicidad.

---

## 📂 Estructura del proyecto

realtime-system-monitor/
│
├── app.py # Código principal (Flask + Chart.js + psutil)
├── requirements.txt # Dependencias (opcional)
└── README.md # Documentación

yaml
Copiar
Editar

---

## ⚙️ Instalación y ejecución

### **Opción 1 — Local**
Requiere Python 3.9 o superior.

```bash
# 1. Clonar el repositorio
git clone https://github.com/tuusuario/realtime-system-monitor.git
cd realtime-system-monitor

# 2. Instalar dependencias
pip install flask psutil

# 3. Ejecutar el servidor
python app.py
Accede a:

Dashboard: http://localhost:5000

Métricas Prometheus: http://localhost:5000/metrics

Opción 2 — GitHub Codespaces
Abre este repositorio en Codespaces.

Instala dependencias:

bash
Copiar
Editar
pip install flask psutil
Ejecuta:

bash
Copiar
Editar
python app.py
Haz clic en "Open in Browser" cuando Codespaces te lo sugiera.

📡 API Endpoints
Endpoint	Método	Descripción
/	GET	Dashboard HTML con gráficos
/data	GET	Datos en JSON con CPU, RAM y Disco
/metrics	GET	Métricas en formato Prometheus

🛠️ Tecnologías utilizadas
Python 3

Flask (backend web)

psutil (métricas del sistema)

Chart.js (visualización de datos en el navegador)

Prometheus exposition format (monitorización avanzada)

💡 Mejoras futuras
🔐 Autenticación para proteger el dashboard.

⚠️ Alertas por email o Slack al superar umbrales críticos.

📦 Dockerfile para despliegue rápido en contenedores.

📊 Persistencia de métricas en base de datos o Prometheus.

📜 Licencia
Este proyecto está bajo la licencia MIT.
Puedes usarlo, modificarlo y distribuirlo libremente, citando la fuente original.

👨‍💻 Autor
Emanuel Gonzalez Michea
LinkedIn | GitHub

