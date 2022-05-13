from pyspark.sql.functions import to_date, when

class Clean():

    # Cambia 'tbd' a -1 (float)
    def clean_tbd(result):
        return result.withColumn('userscore', when(result.userscore == 'tbd', '-1').otherwise(result.userscore).cast('float'))

    # Cast de fecha
    def cast_date(result):
        return result.withColumn('date', to_date(result.date, 'LLL d, yyyy'))
