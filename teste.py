
import sqlite3


class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite3')
        self.cursor = self.conn.cursor()
        #testeeeee

    def user_exists(self, login, senha):
        try:
            self.cursor.execute("""
                SELECT * FROM login WHERE login = ? and senha = ?
            """, (login, senha))
            return bool(self.cursor.fetchone())
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False

    def cadastrar_usuario(self, login, senha, nome, sobrenome, email, matricula):
        if self.user_exists(login, senha):
            print("Usuario ja existe")
            return None
        try:
            self.cursor.execute("""
                INSERT INTO login (login, senha, nome, sobrenome, email, matricula, datacriacao)
                VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """, (login, senha, nome, sobrenome, email, matricula))
            self.conn.commit()
            print("Usuario criado com sucesso")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            self.conn.rollback()

    def login(self, login, senha):
        try:
            self.cursor.execute("""
                SELECT * FROM login WHERE login = ? AND senha = ?
            """, (login, senha))
            user = self.cursor.fetchone()
            return user
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return f"Error: {e}"

    def close(self):
        self.conn.close()


db_manager = DatabaseManager()
# db_manager.cadastrar_usuario(
#     'a', 'a', 'John', 'Doe', 'johndoe@example.com', 12345)
user = db_manager.login('a', 'a')
print(user)
