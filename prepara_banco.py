import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='', )

# Descomente se quiser desfazer o banco...
# conn.cursor().execute("DROP DATABASE `my_logger`;")
# conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `my_logger` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `my_logger`;
    CREATE TABLE `evento` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) COLLATE utf8_bin NOT NULL,
      `data_inicio` varchar(50) COLLATE utf8_bin NOT NULL,
      `data_fim` varchar(50) COLLATE utf8_bin NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

# conn.cursor().execute(criar_tabelas)

# inserindo eventos
cursor = conn.cursor()
cursor.executemany(
      'INSERT INTO my_logger.evento (nome, data_inicio, data_fim) VALUES (%s, %s, %s)',
      [
            ('Evento 1', '2020-02-21T10:00', '2020-02-21T12:00'),
			('Evento 2', '2020-02-22T10:00', '2020-02-22T12:00'),
            ('Evento 3', '2020-02-23T10:00', '2020-02-23T12:00'),
      ])

cursor.execute('select * from my_logger.evento')
print(' -------------  Eventos:  -------------')
for evento in cursor.fetchall():
    print(evento[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()
