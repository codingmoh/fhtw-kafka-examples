from datetime import datetime
from elasticsearch import Elasticsearch
from consumer_helper import run_consumer
from ../utils import consumer_helper

def process_data(data):
    print(data)

if __name__ == '__main__':
    run_consumer('python_es_consumer', process_data)

es = Elasticsearch()

es = Elasticsearch(
    ['https:/cloudhosturl'],
    http_auth=('accessor', 'AHV1wMlFliyuIBiLAxLK'),
    scheme="https", port=443,)


res = es.index(index='ads', doc_type="_doc", id=data[0]['ad_id'], body=data[0])

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", id=1, body=doc)
print(res['result'])

res = es.get(index="test-index", id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])