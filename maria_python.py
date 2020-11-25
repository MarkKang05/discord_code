import pymysql

def exe_sql(week):
    conn = pymysql.connect(host="localhost", user='classroom', password='abc123', db='classroom', charset='utf8')

    curs = conn.cursor()

    sql_query = "SELECT period, A.name AS class_name, A.z_code FROM class_time B \
     INNER JOIN class A \
     ON B.code = A.code \
     WHERE WEEK = '{}' \
     ORDER BY WEEK, period, B.code".format(week)     
    #week = input("input: ")
    #print(exe_sql(week))
    curs.execute(exe_sql(week))

    rows = curs.fetchall()
    #print(rows)
    #print("{:^6}{:^15}{:^30}".format("Period", "class_name", "z_code"))
    
    row_list = [] 
    for value in rows:
        period = value[0]
        class_name = value[1]
        z_code = value[2]
        row_list.append([value[0], value[1], value[2]]) 
        #print("{:>6}{:>15}{:>30}".format(period, class_name, z_code)) 
    
    conn.close()

    return row_list


