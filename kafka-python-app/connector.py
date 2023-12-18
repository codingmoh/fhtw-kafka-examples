from datetime import datetime
from utils.kafka_connector import run_consumer
from utils import ccloud_lib as ccloud_lib

# Use the AppSearch client directly:
from elastic_enterprise_search import AppSearch

app_search = AppSearch(
    "https://3a5fa9f6b56d41128a585a22d5f14349.ent-search.us-central1.gcp.cloud.es.io",
    http_auth="private-c5z5xwm7sepyk9sgmugeb9st"
)
engine_name = "product-search-engine"

def process_data(message):
    code = message['code']
    print(f'document { code } received => sending...')
    app_search.index_documents(
        engine_name=engine_name,
        documents=[message])

if __name__ == '__main__':
    # Read arguments and configurations and initialize
    args = ccloud_lib.parse_args()
    conf = ccloud_lib.read_ccloud_config(args.config_file)

    # Create Consumer instance
    consumer_conf = ccloud_lib.pop_schema_registry_params_from_config(conf)
    run_consumer(conf, 'es_group', args.topic, process_data)