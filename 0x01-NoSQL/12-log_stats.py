#!/usr/bin/env python3

''' log stats module'''

from pymongo import MongoClient

list_all = __import__('8-all').list_all
if __name__ == '__main__':
    client = MongoClient()
    db = client.logs
    nginx_collection = db.nginx
    m = "\tmethod "
    m_get = {'method': 'GET'}
    m_pos = {'method': 'POST'}
    m_put = {'method': 'PUT'}
    m_pat = {'method': 'PATCH'}
    m_del = {'method': 'DELETE'}
    m_get_status = {'method': 'GET', 'path': '/status'}
    print(f"{nginx_collection.estimated_document_count()} logs")
    print("Methods:")
    print(f"{m}GET: {nginx_collection.count_documents(m_get)}")
    print(f"{m}POST: {nginx_collection.count_documents(m_pos)}")
    print(f"{m}PUT: {nginx_collection.count_documents(m_put)}")
    print(f"{m}PATCH: {nginx_collection.count_documents(m_pat)}")
    print(f"{m}DELETE: {nginx_collection.count_documents(m_del)}")

    print(f"{nginx_collection.count_documents(m_get_status)} status check")
