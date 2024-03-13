from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:72200571Jf@localhost:3306/prueba")

conn = engine.connect()

meta_data = MetaData()