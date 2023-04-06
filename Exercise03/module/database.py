import pymysql

from Post import Post


class Database:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="password", database="article_db",
                               charset='utf8mb4')

    def get_posts(self):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT id, title, content, created FROM posts ORDER BY created DESC")
            data = cursor.fetchall()
            return [Post(*post) for post in data]
        except:
            return ()
        finally:
            con.close()
        pass

    def get_post_by_id(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("SELECT id, title, content, created FROM posts WHERE id = %s", (id))
            post = cursor.fetchone()
            return Post(post[0], post[1], post[2], post[3])
        except:
            return None
        finally:
            con.close()
        pass

    def insert(self, post):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO posts(title, content) VALUES(%s, %s)",
                           (post.title, post.content))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, post):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE posts set title = %s, content = %s where id = %s",
                           (post.title, post.content, post.id))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM posts where id = %s", (id))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
