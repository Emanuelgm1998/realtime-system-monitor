#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template_string, Response
import psutil

app = Flask(__name__)

DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Monitor de Recursos</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f4f4f4; }
        h1 { text-align: center; }
        canvas { background: white; padding: 10px; border-radius: 10px; }
    </style>
</head>
<body>
    <h1>Monitor de Recursos — Flask + Chart.js</h1>
    <canvas id="chart" width="800" height="400"></canvas>
    <script>
        const ctx = document.getElementById('chart').getContext('2d');
        const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [],
                datasets: [
                    { label: 'CPU %', borderColor: 'red', fill: false, data: [] },
                    { label: 'RAM %', borderColor: 'blue', fill: false, data: [] },
                    { label: 'Disco %', borderColor: 'green', fill: false, data: [] }
                ]
            },
            options: { scales: { y: { min: 0, max: 100 } } }
        });

        async function fetchData() {
            const res = await fetch('/data');
            const data = await res.json();
            const timeLabel = new Date().toLocaleTimeString();

            chart.data.labels.push(timeLabel);
            chart.data.datasets[0].data.push(data.cpu);
            chart.data.datasets[1].data.push(data.ram);
            chart.data.datasets[2].data.push(data.disk);

            if (chart.data.labels.length > 20) {
                chart.data.labels.shift();
                chart.data.datasets.forEach(ds => ds.data.shift());
            }
            chart.update();
        }
        setInterval(fetchData, 2000);
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(DASHBOARD_HTML)

@app.route("/data")
def get_data():
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    return jsonify({"cpu": cpu, "ram": ram, "disk": disk})

@app.route("/metrics")
def metrics():
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    metrics_str = f"""# HELP cpu_usage CPU usage percentage
# TYPE cpu_usage gauge
cpu_usage {cpu}
# HELP ram_usage RAM usage percentage
# TYPE ram_usage gauge
ram_usage {ram}
# HELP disk_usage Disk usage percentage
# TYPE disk_usage gauge
disk_usage {disk}
"""
    return Response(metrics_str, mimetype="text/plain")

if __name__ == "__main__":
    print("🚀 Servidor iniciado en http://localhost:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
