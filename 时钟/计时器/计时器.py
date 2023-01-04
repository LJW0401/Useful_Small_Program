import tkinter as tk
import tkinter.ttk
import tkinter.messagebox
# import os
import datetime
import time
import os.path


def App_path():
    import sys
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)  #使用pyinstaller打包后的exe目录
    return os.path.dirname(__file__)            #没打包前的py目录


class Counter:
    def __init__(self) -> None:
        pass

    def