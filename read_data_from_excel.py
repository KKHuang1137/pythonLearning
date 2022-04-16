import xlrd
import openpyxl


class ReadData(object):

    def __init__(self, path):
        self.path = path
        self.file_format = ["xlsx", "xls"]


    # 读取xlx文件，返回工作簿
    def read_xls(self):
        data = xlrd.open_workbook(self.path)
        # print(data.sheet_names())  # 输出所有页的名称
        table = data.sheets()[0]  # 获取第一页
        # table = data.sheet_by_index(0)  # 通过索引获得第一页
        # table = data.sheet_by_name('Over')  # 通过名称来获取指定页
        rows = table.nrows  # 为行数，整形
        cols = table.ncols  # 为列数，整形
        # print(rows, cols)
        # print(table.row_values(0))  # 输出第一行值 为一个列表

        # 遍历输出所有行值
        info = []
        for row in range(rows):
            # print(table.row_values(row))
            info.append(table.row_values(row))
        # # 输出某一个单元格值
        # print(table.cell(0, 0).value)
        # print(table.row(0)[0].value)
        return info[1:]


    # 读取xlsx文件，返回工作簿
    def read_xlsx(self):
        sheet = openpyxl.load_workbook(self.path)  # 打开工作簿
        table = sheet.active  # 获取正在激活的工作簿，为了读写正确，只能有一个工作簿
        rows = table.rows  # 获得行数 类型为迭代器
        cols = table.columns  # 获得列数 类型为迭代器
        info = []
        # 遍历获取每个单元格的数据
        for row in rows:
            data = [col.value for col in row]  # 取值
            info.append(data)
        return info[1:]  # 第一行为标题，不导入




    # 获取文件后缀名
    def get_suffix(self):
        suffixs = self.path.split(".")  # 把字符串根据.号分割，最后一个是后缀名
        return suffixs[-1]


    # 判断读取方式，xlx或者xlsx，返回读取方法
    def decide_use_way(self):
        # 如果返回值在定义的文件列表中
        if self.get_suffix() in self.file_format:
            if self.get_suffix() == "xlsx":
                return self.read_xlsx  # 返回读取xlsx文件方法
            else:
                return self.read_xls  # 返回读取xls文件方法
        else:
            file_format = ",".join(self.file_format)  # 格式字典拼接成字符串
            print("源文件格式不在以下{}格式中".format(file_format))


    # 获取数据
    def read_data(self):
        way = self.decide_use_way()
        return way()  # 执行方法，返回数据



read_data = ReadData(r"C:\Users\11376\Desktop\text.xls")
print(read_data.read_data())







