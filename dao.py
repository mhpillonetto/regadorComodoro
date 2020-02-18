from models import Evento

SQL_DELETA_EVENTO = 'delete from evento where id = %s'
SQL_EVENTO_POR_ID = 'SELECT id, nome, data_inicio, data_fim from evento where id = %s'
SQL_ATUALIZA_EVENTO = 'UPDATE evento SET nome=%s, data_inicio=%s, data_fim=%s where id = %s'
SQL_BUSCA_EVENTOS = 'SELECT id, nome, data_inicio, data_fim from evento'
SQL_CRIA_EVENTO = 'INSERT into evento (nome, data_inicio, data_fim) values (%s, %s, %s)'


class EventoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, evento):
        cursor = self.__db.connection.cursor()

        if (evento.id):
            cursor.execute(SQL_ATUALIZA_EVENTO, (evento.nome, evento.data_inicio, evento.data_fim, evento.id))
        else:
            cursor.execute(SQL_CRIA_EVENTO, (evento.nome, evento.data_inicio, evento.data_fim))
            evento.id = cursor.lastrowid
        self.__db.connection.commit()
        return evento

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_EVENTOS)
        eventos = traduz_eventos(cursor.fetchall())
        return eventos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_EVENTO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Evento(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_EVENTO, (id, ))
        self.__db.connection.commit()


def traduz_eventos(eventos):
    def cria_evento_com_tupla(tupla):
        return Evento(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_evento_com_tupla, eventos))
