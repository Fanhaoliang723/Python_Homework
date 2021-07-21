from UI import cmdUI
#不会sys.path因此把主函数都放到了资源文件的上级目录
if __name__ == "__main__":
   ui = cmdUI.CmdUi()
   ui.welcome()
   ui.choose_moudle()
