import logging
import sqlite3
import json

logging.basicConfig(filename='log_file.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# GCP Access Resources Handler Class
class Ingestion(object):

    @staticmethod
    def debug(msg):
        logger.debug(msg)

    @staticmethod
    def error(msg):
        logger.error(msg)

    @staticmethod
    def __db_lite_connection():
        try:
            conn = sqlite3.connect('/app/db_folder/scudra.db')
            c = conn.cursor()

            c.execute('''
                      CREATE TABLE IF NOT EXISTS originations
                      ([originationId] TEXT , [clientId] TEXT, [registerDate] TIMESTAMP, [installments] json, [ingestion_time] TIMESTAMP )
                      ''')

            c.execute('''
                      CREATE TABLE IF NOT EXISTS payments
                      ([paymentId] TEXT, [installmentId] TEXT, [paymentDate] TIMESTAMP, [paymentValue] NUMERIC, [ingestion_time] TIMESTAMP )
                      ''')

            conn.commit()

        except sqlite3.Error as e:
            conn = None
            print(e)
            logger.error("Error on Sqlite connection - ", e)

        return conn

    @staticmethod
    def db_load_event(data):
        result = 0
        try:
            conn = Ingestion.__db_lite_connection()
            c = conn.cursor()

            list_values = []
            for item in data['data']:
                for value in tuple(item.values()):
                    list_values.append(json.dumps(value) if type(value) == list else value)

            sqlite_insert_script = """INSERT INTO {}
                                    VALUES (?,?,?,?, strftime('%Y-%m-%d %H:%M:%S', datetime('now'))) ;""".format(data['event_type'])


            c.execute(sqlite_insert_script, tuple(list_values))
            conn.commit()
            conn.close()
            return "Event processed"

        except Exception as e:
            conn.close()
            print(e)
            logger.error("Error on Sqlite connection - ", e)
            return "Error on load event"

    @staticmethod
    def db_query_table(data):
        result = {'result': 'No rows'}
        try:
            conn = Ingestion.__db_lite_connection()
            conn.row_factory = sqlite3.Row
            c = conn.cursor()

            query_result = c.execute("""SELECT * FROM {};""".format(data['event_type'])).fetchall()

            list_dict = []
            for item in query_result:
                list_dict.append({k: item[k] for k in item.keys()})

            result = list_dict
            conn.close()

        except Exception as e:
            conn.close()
            print(e)
            logger.error("Error on Sqlite connection - ", e)
            result = {'result': 'error'}
        finally:
            return result
