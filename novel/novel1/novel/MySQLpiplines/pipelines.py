from .sql import Sql
from novel1.novel.items import NovelItem


class NovelPipeline(object):

    def process_item(self, item, spider):
        xs_name = item['name']
        xs_author = item['author']
        category = item['category']
        name_id = item['name_id']
        serial_status = item['serial_status']
        serial_number = item['serial_number']
        Sql.insert_dd_name(xs_name, xs_author, category, name_id, serial_status, serial_number)
        print('Storing')
