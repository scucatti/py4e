# Chapter 15: Python and Databases

import json
import sqlite3

# inicia um arquivo SQLite chamado 'students_courses.sqlite'
conn = sqlite3.connect('students_courses.sqlite')
cur = conn.cursor()

# criar uma tabela para cada item pedido em uma série de comandos SQL
# os primeiros comandos 'limpam' o arquivo caso já existam tabelas nomeadas
# como as que vamos modificar
# em sequencia, criamos as tabelas 'User', 'Course' com informações dos
# usuários e dos cursos
# A tabela 'Member' vai unir as outras duas tabelas.
# 'User' e 'Course' tem uma relação many-to-many
cur.executescript('''

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE 'User' (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE
);

CREATE TABLE 'Course' (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
title TEXT UNIQUE
);

CREATE TABLE 'Member' (
user_id INTEGER,
course_id INTEGER,
role INTEGER,
PRIMARY KEY (user_id, course_id)
);
''')

fname = input('Enter file name:')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

# abre o conteúdo do file e transforma tudo em uma única string
str_data = open(fname).read()
# analisa a string considerando que é um arquivo json
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0];
    title = entry[1];
    role = entry[2];

    print((name, title, role))

    #adiciona os nomes dos usuários obtidos no arquivo json na coluna 'name'
    # da tabela User, criando ids para cada nome
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    # usa a id criada na tabela users e armazena na variável user_id
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    #adiciona os títulos dos cursos na coluna 'title' da tabela 'Course' e
    # armazena a id na variável course_id
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )


    conn.commit()

    # para conectar todos juntos
# cur.execute(''' SELECT User.name, Member.role, Course.title
# FROM User JOIN Member JOIN Course
# ON Member.user_id = User.id AND Member.course_id = Course.id
# ORDER BY Course.title, Member.role DESC, User.name
# ''')
