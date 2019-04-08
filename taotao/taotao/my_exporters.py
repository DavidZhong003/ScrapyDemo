from scrapy.exporters import BaseItemExporter
import xlwt


class ExcelItemExporter(BaseItemExporter):
    """
    导出为Excel
    在执行命令中指定输出格式为excel
    e.g. scrapy crawl -t excel -o books.xls
    """

    def __init__(self, file, **kwargs):
        self._configure(kwargs)
        self.file = file
        self.wbook = xlwt.Workbook(encoding='utf-8')
        self.wsheet = self.wbook.add_sheet('scrapy')
        self._headers_not_written = True
        self.fields_to_export = list()
        self.row = 0

    def finish_exporting(self):
        self.wbook.save(self.file)

    def export_item(self, item):
        if self._headers_not_written:
            self._headers_not_written = False
            self._write_headers_and_set_fields_to_export(item)

        fields = self._get_serialized_fields(item)
        for col, v in enumerate(x for _, x in fields):
            print(self.row, col, str(v))
            self.wsheet.write(self.row, col, str(v))
        self.row += 1

    def _write_headers_and_set_fields_to_export(self, item):
        if not self.fields_to_export:
            if isinstance(item, dict):
                self.fields_to_export = list(item.keys())
            else:
                self.fields_to_export = list(item.fields.keys())
        for column, v in enumerate(self.fields_to_export):
            self.wsheet.write(self.row, column, v)
        self.row += 1
