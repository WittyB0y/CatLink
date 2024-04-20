from django.core.management import BaseCommand
from django.db import connection
from utils.sql_query import SQL_QUERY


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """
        func for execute SQL query
        """
        with connection.cursor() as cursor:
            cursor.execute(SQL_QUERY)
            result = cursor.fetchall()

        self.stdout.write('Success!!!')

        for row in result:
            email, count_links, website, book, article, music, video = row
            self.stdout.write(
                f'{email=}, {count_links=}, {website=}, '
                f'{book=}, {article=}, {music=}, {video=}'
            )
