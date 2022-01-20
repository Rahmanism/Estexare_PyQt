import sys
import random
import sqlite3
from sqlite3 import Error
import os

class Estexare:
  def __init__(self, dbPath = ''):
    self.errorMsg = ''
    if dbPath == '':
      self.dbPath = f"{os.path.dirname(os.path.realpath(__file__))}/db.db"
    else:
      self.dbPath = dbPath
    self._loadData()

  def _loadData(self):
    try:
      self.db = sqlite3.connect(self.dbPath)
      self.db.row_factory = sqlite3.Row
      self.cursor = self.db.cursor()
      self.cursor.execute("SELECT * FROM estexare")
      self.data = self.cursor.fetchall()
      self.db.close()
    except Error as e:
      self.errorMsg = f"ERROR: {e}"
      return

  def newEstexare(self):
    no = random.randint(1, len(self.data))
    return self.data[no - 1]