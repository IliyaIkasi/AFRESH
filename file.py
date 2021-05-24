CREATE_TABLE = "CREATE TABLE IF NOT EXISTS details(" \
               "'id' INTEGER," \
               "'firstName' TEXT(10) NOT NULL," \
               "'lastName' TEXT(10) NOT NULL," \
               "'email' TEXT(30) NOT NULL UNIQUE," \
               "'age' INTEGER(10) NOT NULL," \
               "'gender' TEXT(10) NOT NULL," \
               "PRIMARY KEY ('id' AUTOINCREMENT)"\
               ")"