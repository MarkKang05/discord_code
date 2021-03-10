import pymysql

def make_query(week):
    return "SELECT period, A.name AS class_name, A.z_code FROM class_time B \
     INNER JOIN class A \
     ON B.code = A.code \
     WHERE WEEK = '{}' \
     ORDER BY WEEK, period, B.code".format(week)

def make_query_6(week):
    return "SELECT period, A.name AS class_name, A.z_code FROM class_time_6 B \
     INNER JOIN class A \
     ON B.code = A.code \
     WHERE WEEK = '{}' \
     ORDER BY WEEK, period, B.code".format(week)



def exe_sql(classroom, week):
    conn = pymysql.connect(host="192.168.0.31", user='classroom', password='123456', db='classroom', charset='utf8')

    curs = conn.cursor()
  
    #week = input("input: ")
    #print(exe_sql(week))
    if classroom == 6:
        curs.execute(make_query_6(week))
    else:
        curs.execute(make_query(week))

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


