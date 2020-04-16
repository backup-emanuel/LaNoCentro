import os
import mysql.connector
import io
import datetime
import csv
import random
import logging

class ConnectMysql(object):

    def __init__(self, db_name=""):
        try:
            # conectando...
            self.conn = mysql.connector.connect(host="localhost", user="root", passwd="ifpbinfo", database="lanocentro")
            self.cursor = self.conn.cursor()
            print("Banco:", self.conn.database)
            self.cursor.execute('SELECT VERSION()')
            self.data = self.cursor.fetchone()
            print("MySQL version: %s" % self.data)
        except sqlite3.Error:
            print("Erro ao abrir banco.")

    def CommitDb(self):
        if self.conn:
            self.conn.commit()

    def CloseDb(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")


class LaNoCentroDb(object):

    def __init__(self):
        self.db = ConnectMysql()

    def CloseConnection(self):
        self.db.CloseDb()

    def setEmpresa(self, nome, id_endereco, email, telefone, instagram, facebook):
        conn = self.db.conn
        cursor = self.db.conn.cursor()
        cursor.execute("""
            insert into tb_empresa(nome, id_endereco, email, telefone, instagram, facebook)
            values(?, ?, ?, ?, ?, ?);
        """, (nome, id_endereco, email, telefone, instagram, facebook))
        conn.commit()

        id = cursor.lastrowid

        return id

    def setEndereco(self, logradouro, numero, complemento, cidade, estado, cep, ponto_referencia):
        conn = self.db.conn
        cursor = self.db.conn.cursor()
        cursor.execute("""
            insert into tb_endereco(logradouro, numero, complemento, cidade, estado, cep, ponto_referencia)
            values(%s, %s, %s, %s, %s, %s, %s);
        """, (logradouro, numero, complemento, cidade, estado, cep, ponto_referencia))
        conn.commit()

        id = cursor.lastrowid

        return id


if __name__ == '__main__':
    n = LaNoCentroDb()
