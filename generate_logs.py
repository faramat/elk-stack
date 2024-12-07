import json, os
from loguru import logger
from elasticsearch import Elasticsearch


es_login = os.getenv("ELASTIC_USERNAME")
es_password = os.getenv("ELASTIC_PASSWORD")
es = Elasticsearch(["http://localhost:9200"], basic_auth=(es_login, es_password))

def elastic_header(message):
    log_record = message.record
    doc = {
        "@timestamp": log_record["time"].isoformat(),
        "level": log_record["level"].name,
        "message": log_record["message"],
        "module": log_record["module"],
        "function": log_record["function"],
        "line": log_record["line"]
    }
    es.index(index="logs", body=json.dumps(doc))

logger.add(elastic_header, level="INFO")



def main():
    logger.info("Запуск функции отправки смс")
    logger.warning("Скоро истечет токен")
    logger.debug("Отправил смс")
    logger.error("Ошибка при отправке")


main()