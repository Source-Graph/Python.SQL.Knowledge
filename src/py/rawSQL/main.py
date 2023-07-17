from rawSQL.list import *
from rawSQL.create_db import *
from rawSQL.delete_db import *

createDb("testdatabase")

listDbs()

deleteDb("testdatabase")
