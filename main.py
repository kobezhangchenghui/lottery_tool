import pymysql


def mysql_connection():
    db = pymysql.Connect(host='localhost', port=3306, user='root', passwd='Changeme_123', db='lottery')
    return db


def get_data():
    try:
        conn = mysql_connection()
        cursor = conn.cursor()
        n = input("How many members you want to get:")
        cursor.execute("SELECT * FROM members ORDER BY RAND() limit %s" % n)
        for row in cursor.fetchall():
            print(row[1])
        conn.commit()
    except Exception as e:
        print("something was wrong,cause:%s" % e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def add_data():
    try:
        conn = mysql_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(id) FROM members")
        max_id = cursor.fetchone()[0]
        while True:
            user_name = input("Please input user's name:")
            if user_name == "exit":
                break
            cursor.execute("INSERT INTO members (id, name) VALUES (%s, '%s')" % (max_id+1, user_name))
            max_id += 1
        conn.commit()
    except Exception as e:
        print("something was wrong,cause:%s" % e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def update_data():
    try:
        conn = mysql_connection()
        cursor = conn.cursor()
        while True:
            id = input("Please input the member's id that you want to update:")
            newuser_name = input("Please input the newuser's name:")
            if id == 0 or newuser_name == "exit":
                break
            cursor.execute("UPDATE members SET name='%s' WHERE id=%s" % (newuser_name, id))
        conn.commit()
    except Exception as e:
        print("something was wrong,cause:%s" % e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def delete_data():
    try:
        conn = mysql_connection()
        cursor = conn.cursor()
        while True:
            id = input("Please input the member's id that you want to delete:")
            if id == "0":
                break
            cursor.execute("DELETE FROM members WHERE id=%s" % id)
        conn.commit()
    except Exception as e:
        print("something was wrong,cause:%s" % e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    n = int(input("1.add\n2.get\n3.update\n4.delete\nWhat do you want to do? Please input a number:"))
    if n == 1:
        add_data()
    elif n == 2:
        get_data()
    elif n == 3:
        update_data()
    elif n == 4:
        delete_data()
    else:
        print("Your input is illegal!")
