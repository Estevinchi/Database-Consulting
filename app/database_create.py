# import sqlite3

# # # Importación de controllers
# # from controllers.admin_controller import AdminController

# # # Conexión y creación
# conn = sqlite3.Connection('data/users.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS users(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE,
#             password_hash TEXT NOT NULL,
#             admin BOOLEAN DEFAULT False)
#         ''')
# conn.commit()


# # Creación del administrador
# # AdminController.create_user('admin','admin',True)


# conn.commit()
# conn.close()
