import psycopg2

conn = psycopg2.connect(database = "skov",
                        host = "127.0.0.1",
                        user = "postgres",
                        password = "admin",
                        port = "5432")

cursor = conn.cursor()
