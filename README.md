# AirflowDatadogsetup
**1.install the Airflow StatsD plugin **
<br>
    pip install 'apache-airflow[statsd]'
    <br>
**2.Update the Airflow configuration file airflow.cfg by adding some properties**
<br>
[scheduler]
<br>
statsd_on = True<br>
statsd_host = localhost<br>
statsd_port = 8125<br>
statsd_prefix = airflow<br>
**3.Update the Datadog Agent main configuration file datadog.yaml by adding someproparties into datadog.yaml.**<br>
**4.Restart DataDog with Airflow**<br>
    sudo service datadog-agent restart
    
#Resources
Airflow Integrate Datadog :- https://docs.datadoghq.com/integrations/airflow/


