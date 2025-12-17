import sqlite3

def get_db():
    conn = sqlite3.Connection('data/users.db')
    conn.row_factory= sqlite3.Row
    return conn
    

class UserModel:
    
    @staticmethod
    def get_all_users():
        conn=get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        users = c.fetchall()
        conn.close()
        return users
    
    @staticmethod
    def get_user(username):
        conn= get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=?',(username,))
        user=c.fetchone()
        conn.close()
        return user
    
    @staticmethod
    def get_user_by_id(id):
        conn= get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE id=?',(id,))
        user=c.fetchone()
        conn.close()
        return user
    
    @staticmethod
    def insert_user(user):
        conn = get_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
            "INSERT INTO users (username, password_hash, admin) VALUES (?, ?, ?)",
            (user.username, user.password_hash, user.admin))
            conn.commit()
            return True
        except Exception as ex:
            return Exception(ex)
        finally:
            conn.close()
        
    @staticmethod
    def delete_user(id):
        conn = get_db()
        cursor=conn.cursor()
        cursor.execute('DELETE FROM users WHERE id=?',(id,))
        conn.commit()
        conn.close()
        
    @staticmethod
    def update_user(id,username,admin):
        conn = get_db()
        cursor=conn.cursor()
        admin = bool(admin)
        try:
            cursor.execute('UPDATE users SET username=?,admin=? WHERE id=?',(username,admin,id))
            conn.commit()
        except Exception as ex:
            return Exception(ex)
        finally:
            conn.close()
        
    @staticmethod
    def update_admin(id,admin):
        conn = get_db()
        cursor=conn.cursor()
        admin = bool(admin)
        cursor.execute('UPDATE users SET admin=? WHERE id=?',(admin,id))
        conn.commit()
        conn.close()
        
    @staticmethod
    def update_pswd(id,pswd):
        conn = get_db()
        cursor=conn.cursor()
        try:
            cursor.execute('UPDATE users SET password_hash=? WHERE id=?',(pswd,id))
            conn.commit()
        except Exception:
            return "Error en contraseña update"
        finally:
            conn.close()
       