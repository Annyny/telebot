import sqlite3
import random

class Database:
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file)
        self.cur = self.con.cursor()

    def history_questions(self):
        with self.con:
            random_id = random.choice(range(1, 36))
            result = self.cur.execute("SELECT * FROM history_table WHERE id=?", (random_id,)).fetchone()[1]
            return result

    def biology_questions(self):
        with self.con:
            random_id = random.choice(range(1, 36))
            result = self.cur.execute("SELECT * FROM biology_table WHERE id=?", (random_id,)).fetchone()[1]
            return result

    def biology_answers(self, questions):
        with self.con:
            result = self.cur.execute("SELECT * FROM biology_table WHERE questions=?", (questions,)).fetchone()[2]
            return result

    def history_answers(self, questions):
        with self.con:
            result = self.cur.execute("SELECT * FROM history_table WHERE questions=?", (questions,)).fetchone()[2]
            return result

    def history_wrong_answers(self, questions):
        with self.con:
            result = self.cur.execute("SELECT * FROM history_table WHERE questions=?", (questions,)).fetchone()[3]
            return result

    def biology_wrong_answers(self, questions):
        with self.con:
            result = self.cur.execute("SELECT * FROM biology_table WHERE questions=?", (questions,)).fetchone()[3]
            return result

