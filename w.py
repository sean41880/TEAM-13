import psycopg2
import os
import get_data

def web_select_overall():
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    
    postgres_select_query = f"""SELECT * FROM alpaca_training ORDER BY record_no;"""
    
    cursor.execute(postgres_select_query)
    
    message = []
    while True:
        temp = cursor.fetchmany(10)
        
        if temp:
            message.extend(temp)
        else:
            break
    
    cursor.close()
    conn.close()
    
    return message

def web_select_specific(condition):
    DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    
    condition_query = []
    
    for key, value in condition.items():
        if value:
            condition_query.append(f"{key}={value}")
    if condition_query:
        condition_query = "WHERE " + ' AND '.join(condition_query)
    else:
        condition_query = ''
    
    postgres_select_query = f"""SELECT * FROM alpaca_training {condition_query} ORDER BY record_no;"""
    print(postgres_select_query)
    
    cursor.execute(postgres_select_query)

    table = []
    while True:
        temp = cursor.fetchmany(10)

        if temp:
            table.extend(temp)
        else:
            break

    cursor.close()
    conn.close()

    return table

def web_select_py(D):
    data = get_data.get_data()
    if D['survivor'] == '':
        if D['counter'] == '':
            matching= [{'survivor': d['survivor'], 'counter': d['counter'], 'hunter': d['hunter']} for d in data if d['hunter'] == D['hunter']]
        else:    
            matching= [{'survivor': d['survivor'], 'counter': d['counter'], 'hunter': d['hunter']} for d in data if d['hunter'] == D['hunter'] and d['counter'] == D['counter']]
    if D['hunter'] == '':
        if D['counter'] == '':
            matching= [{'survivor': d['survivor'], 'counter': d['counter'], 'hunter': d['hunter']} for d in data if d['survivor'] == D['survivor']]
        else:    
            matching= [{'survivor': d['survivor'], 'counter': d['counter'], 'hunter': d['hunter']} for d in data if d['survivor'] == D['survivor'] and d['counter'] == D['counter']]


    return matching