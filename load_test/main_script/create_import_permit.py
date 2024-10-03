from datetime import datetime
import time
from multiprocessing import Process
import threading
from load_test.database_script.qa_russelramos03_ip_1000_items import get_pt_script
from load_test.database_script.qa_RBETEST0026_ip_1000_items import get_pt_script1
from load_test.database_script.qa_RBETEST0028_ip_1000_items import get_pt_script3
import psycopg2

def database_insert_execute_01(db_script, scenario):
    print("Test Scenario ", scenario, " Started: ", datetime.now())

    pt_script = db_script['create_ip_1000_items']

    for x in range(5000):
        conn = psycopg2.connect(database="peza_db", host="192.168.20.15", user="qatest_user", password="W1m$q@1234", port="55432")
        cursor = conn.cursor()
        cursor.execute(pt_script)
        conn.close()
        x = x + 1

    print("Test Scenario ", scenario, " Completed: ",datetime.now())

def database_insert_execute_02(db_script, scenario):
    print("Test Scenario ", scenario, " Started: ", datetime.now())

    pt_script = db_script['create_ip_1000_items']

    for x in range(1000):
        conn = psycopg2.connect(database="peza_db", host="192.168.20.15", user="qatest_user", password="W1m$q@1234", port="55432")
        cursor = conn.cursor()
        cursor.execute(pt_script)
        conn.close()
        x = x + 1

    print("Test Scenario ", scenario, " Completed: ",datetime.now())

def database_insert_execute_03():
    print("Test Scenario 3 Started: ", datetime.now())

    conn = psycopg2.connect(database="peza_db", host="192.168.20.15", user="qatest_user", password="W1m$q@1234", port="55432")
    cursor = conn.cursor()
    cursor.execute("select now();")
    get_result = cursor.fetchone()
    conn.close()
    print(get_result, time.tzname)
    print("Test Scenario 3 Completed: ", datetime.now())

if __name__ == "__main__":
    # Create two threads for each function
    thread_one = threading.Thread(target=database_insert_execute_01, args=(get_pt_script, "01"))
    thread_two = threading.Thread(target=database_insert_execute_01, args=(get_pt_script1, "02"))
    thread_three = threading.Thread(target=database_insert_execute_01, args=(get_pt_script3, "03"))
    # thread_three = threading.Thread(target=database_insert_execute_03)

    # Start both threads
    thread_one.start()
    thread_two.start()
    thread_three.start()

    # Wait for both threads to finish (this won't happen in this example)
    thread_one.join()
    thread_two.join()
    thread_three.join()

# print("Test Started: ", datetime.now())
#
# pt_script1 = get_pt_script1['create_ip_1000_items']
#
# for x in range(1000):
#     conn = psycopg2.connect(database="peza_db", host="192.168.20.15", user="qatest_user", password="W1m$q@1234", port="55432")
#     cursor = conn.cursor()
#     cursor.execute(pt_script1)
#     conn.close()
#     x = x + 1
#
# print("Test Complete: ", datetime.now())