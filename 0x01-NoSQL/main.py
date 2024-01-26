#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school
update_topics = __import__('10-update_topics').update_topics
schools_by_topic = __import__('11-schools_by_topic').schools_by_topic

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    print('--------------------------')
    print(client.list_database_names())
    school_collection = client.bookstore.books
    schools = list_all(school_collection)
    print(len(schools))
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
    
    # new_school_id = insert_school(school_collection, name="Holberton school", address="505 Parnassus Ave")
    # print("New school created: {}".format(new_school_id))

    # schools = list_all(school_collection)
    # for school in schools:
    #     print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))

    # update_topics(school_collection, "UCSF", ["Sys admin", "AI", "Algorithm"])

    # schools = list_all(school_collection)
    # for school in schools:
    #     print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    # update_topics(school_collection, "Holberton school", ["iOS"])

    # schools = list_all(school_collection)
    # for school in schools:
    #     print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
    # j_schools = [
    #     { 'name': "Holberton school", 'topics': ["Algo", "C", "Python", "React"]},
    #     { 'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
    #     { 'name': "UCLA", 'topics': ["C", "Python"]},
    #     { 'name': "UCSD", 'topics': ["Cassandra"]},
    #     { 'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
    # ]
    # for j_school in j_schools:
    #     insert_school(school_collection, **j_school)

    # schools = schools_by_topic(school_collection, "Python")
    # for school in schools:
    #     print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))