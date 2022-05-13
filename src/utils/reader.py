class Reader():

    def __init__(self, spark):
        self.spark = spark

    def read(self, path, schema):
        # Leer archivo y borrar duplicados y filas nulas (no está en el desafío su tratamiento)
        return self.spark.read.csv(path, schema=schema).dropna(how='any').dropDuplicates()
