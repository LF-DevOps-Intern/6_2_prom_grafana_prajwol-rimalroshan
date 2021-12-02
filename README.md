# 6_2_Prom_Grafana_Prajwol
Assignment for Prometheus &amp; Grafana for Week 6 Day 2

Tasks:

1. Install Prometheus Server
- Configuration basic authentication username/password
- Screenhot of login prompt while trying to access prometheus
- Screenshot of prometheus dashboard

2. Install node exporter on another machine than the server
- Add that machine target to server configuration
- Share screenshot from status->targets to show the available nodes
- Share configuration of node exporter & prometheus server

3. Install grafana server on same server as prometheus 
- Add prometheus data source to grafana, should be connected through basic auth
- Screenshot of working data source config
- Import & apply dashboard for node_exporter
- Screenshot of dashboard of nodes with live metrics shown.

Sample Server Config:
global:
  scrape_interval: 10s
  scrape_timeout: 6s

scrape_configs:
  - job_name: 'prometheus'
    scrape_interval: 5s
    static_configs:
      - targets: ['10.10.4.105:9090']

  - job_name: 'node'
    scrape_interval: 5s
    static_configs:
      - targets: ['10.10.5.218:9100','10.10.4.105:9100']

  - job_name: 'docker'
    scrape_interval: 5s
    static_configs:
      - targets: ['10.10.5.218:9323']

  - job_name: 'mysql'
    scrape_interval: 5s
    static_configs:
      - targets: ['10.10.5.218:9104']

rule_files:
  - "prometheus-rules.yml"

alerting:
  alertmanagers:
  - static_configs:
    - targets: ['localhost:9093']


