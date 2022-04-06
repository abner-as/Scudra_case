from flask import Flask, request, json, abort, jsonify
import scudra_ingestion
import json

app = Flask(__name__)

@app.route('/ingestion', methods=['POST'])
def ingestion():
    ingestion = scudra_ingestion.Ingestion()
    ingestion.debug("New Event")
    try:
        request_json = request.get_json(silent=True)
        dict_data = request_json
        result = ingestion.db_load_event(dict_data)
    except:
        ingestion.error("Error on process")
        result = 'error'
    finally:
        del ingestion

    return result

@app.route('/get_table_payments', methods=['POST', 'GET'])
def query_data_payments():
    ingestion = scudra_ingestion.Ingestion()
    ingestion.debug("New Query")
    try:
        dict_data = {"event_type":"payments"}
        result = ingestion.db_query_table(dict_data)
    except:
        ingestion.error("Error on process Query")
        result = 'error'
    finally:
        del ingestion

    return json.dumps(result)

@app.route('/get_table_originations', methods=['POST', 'GET'])
def query_data_originations():
    ingestion = scudra_ingestion.Ingestion()
    ingestion.debug("New Query")
    try:
        dict_data = {"event_type":"originations"}
        result = ingestion.db_query_table(dict_data)
    except:
        ingestion.error("Error on process Query")
        result = 'error'
    finally:
        del ingestion

    return json.dumps(result)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e))