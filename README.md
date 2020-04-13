# AirflowDatadogsetup
**1.Install the Airflow StatsD plugin **
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
    Check Datadog.yaml file and the extra part<br>
**4.Restart DataDog with Airflow**<br>
    sudo service datadog-agent restart
    
***Configuration on Ubantu***<br>
    The configuration files and folders for the Agent are located in:<br>
    
        /etc/datadog-agent/datadog.yaml <br>
        Configuration files for Integrations:<br>

        /etc/datadog-agent/conf.d/<br> 
        ** if conf.yaml.example file is given then rename into conf.yaml <br>
        
#Resources<br>
Airflow Integrate Datadog :- https://docs.datadoghq.com/integrations/airflow/<br> ***
        
        



