import click
import sys
from pathlib import Path, PurePath
from use_case import reader as reader
from use_case import joseph as joseph

class CmdUi(object):
    def __init__(self):
        self.map_reader = {".txt":reader.TxtReader, ".csv":reader.CsvReader, ".xlsx":reader.XlsxReader, ".zip":reader.ZipReader}
        self.map_moudle = {"1":self.choose_file, "2":self.show_file, "3":self.run_joseph, "4":self.exit_ui}
        self.path = None
        self.filename = None
        self.person_lst = []

    def choose_file(self):
        flag_file = True
        self.path = input("请输入文件路径：")
        while flag_file:
            if Path(self.path).exists():
               click.echo("文件路径输入成功！")
               flag_file = False
            else:
               self.path = input("文件路径错误，请重新输入")
        click.echo('\n')
        self.choose_moudle()
        
    def show_file(self):
        while self.path == None:
            click.echo('路径为空，请读取文件\n')
            self.choose_moudle()
        suffix = PurePath(self.path).suffix

        if suffix == '.zip':
            if self.filename == None:
                self.filename = input("由于您选择了zip文件，请输入读取文件名称：")
                new_reader = self.map_reader[suffix](self.path, self.filename)
        else:
            new_reader = self.map_reader[suffix](self.path)
        self.person_lst = new_reader.create_lst()
        
        click.echo("文件内容如下所示：")
        for person in self.person_lst:
            click.echo(person)

        click.echo('\n')
        self.choose_moudle()

    def run_joseph(self):
        while self.person_lst == []:
            click.echo('未读取人员信息，请读取文件\n')
            self.choose_moudle()

        start = input("请设置起始位置(start>0):")
        step = input("请设置步长：")
        josepher_iter = joseph.JosephIter(self.person_lst,int(start),int(step))
        result_lst = []

        click.echo("约瑟夫环结果如下所示：")
        for out_person in josepher_iter:
            result_lst.append(out_person)
            click.echo(out_person)
        
        click.echo('\n')
        self.choose_moudle()

    def exit_ui(self):
        answer = input("是否退出？y/n：")
        if str(answer) == 'y':
           click.clear()
           sys.exit(0)
        else:
            click.echo('\n')
            self.choose_moudle()

    def welcome(self):
        click.echo("***************************")
        click.echo("** 欢迎使用约瑟夫环程序  **")
        click.echo("** 请您根据提示进行操作  **")
        click.echo("***************************\n")
    
    def choose_moudle(self):
        click.echo("***************************")
        click.echo("**       功能选择        **")
        click.echo("**1：读取文件 2：显示文件**")
        click.echo("**3：约瑟夫环 4：退出程序**")
        click.echo("***************************")
        moudle = str(input("\n请选择功能："))
        self.verify_moudle(moudle)

    def verify_moudle(self,moudle):
        flag_moudle = True
        while flag_moudle:
            for keys in self.map_moudle:
               if keys == moudle:
                  self.map_moudle[keys]()
                  flag_moudle = False

            if flag_moudle:
               click.echo('模式选择错误，请重新输入')
               moudle = str(input('\n请选择功能:'))

