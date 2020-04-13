from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import statsd

# Statsd
# TCP connection
# statsd_client = statsd.TCPStatsClient('localhost', 8125, prefix='AirFlow')
# UDP connection
statsd_client = statsd.StatsClient('localhost', 8125, prefix='AirFlow')
@statsd_client.timer('print_hello.time')
def print_hello():
    return 'Hello world!'

dag = DAG('hello_world', description='My_first_dag',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator
