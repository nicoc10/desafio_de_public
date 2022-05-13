from pyspark.sql.functions import row_number, desc
from pyspark.sql.window import Window


class Transform:

    def top_10_by_console(games):
        # Ordenar por mayor metascore por consola
        windowSpec = Window.partitionBy("console").orderBy(desc("metascore"),desc("userscore"))
        # Top 10 por consola, ordenando por metascore.
        return games.withColumn("row_number", row_number().over(windowSpec)).where("row_number <11").coalesce(1)

    def worst_10_by_console(games):
        # Oedenar los metascore bajos por consola
        windowSpec = Window.partitionBy("console").orderBy("metascore","userscore")
        # Top peores 10 juegos por consola, ordenando por metascore. Coalesce para guardar
        return games.withColumn("row_number", row_number().over(windowSpec)).where("row_number <11").coalesce(1)

    def top_10_all(games):
        # 10 mejores por metascore
        return games.orderBy(desc("metascore"), desc("userscore")).limit(10).coalesce(1)

    def worst_10_all(games):
        # 10 peores por metascore
        return games.orderBy("metascore","userscore").limit(10).coalesce(1)
