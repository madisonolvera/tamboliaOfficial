import ast
import os


class DataBase:
    def get_table(self, table:str):
        self.__load_tables()
        if table in self.tables.keys():
            return self.tables[table]
        else:
            return f'ERROR - table: {table} not found'
    ''''''
    def add_rows(self, table:str, rows:dict):
        """ can add one or multiple

        :param table:  journal
        :param rows: { timestamp: {
                        "name": 'peter',
                        'age': 45,
                        'question': 'Why am I here?'
                        'answer': 'Who know?!'},

                    timestamp: {
                        "name": 'peter',
                        'age': 45,
                        'question': 'Why am I here?'
                        'answer': 'Who know?!'}
                    }
        :return: success or error
        """
        if table in self.tables.keys():
            data = dict
            for row in rows:
                self.tables[table][row] = rows[row]
            self.__update_table(table=table, data=self.tables[table])
            return f'SUCCESS - {len(rows)} rows added to table: {table}'
        else:
            return f'ERROR - table: {table} not found'

    def edit_row(self, table:str, row:str, field:str, value):
        """"""

    ''''''
    def __load_tables(self):
        tables_files = os.listdir('utils/tables')
        tables = dict()
        for file in tables_files:
            table_name = file.split('.')[0]
            with open(f'utils/tables/{file}') as f:
                data = ast.literal_eval(f.read())
            tables[table_name] = data
        self.tables = tables
        ''
    def __update_table(self, table, data):
        with open(f'utils/tables/{table}.txt', 'w') as f:
            f.write(str(data))
        self.__load_tables()
        ''
    """"""
""""""