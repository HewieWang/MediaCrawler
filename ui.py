"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_frame_lwemfsc4 = self.__tk_label_frame_lwemfsc4(self)
        self.tk_table_lwempfpz = self.__tk_table_lwempfpz( self.tk_label_frame_lwemfsc4) 
        self.tk_button_lwemvqoh = self.__tk_button_lwemvqoh( self.tk_label_frame_lwemfsc4) 
        self.tk_button_lwemwxje = self.__tk_button_lwemwxje( self.tk_label_frame_lwemfsc4) 
        self.tk_label_frame_lwemrpev = self.__tk_label_frame_lwemrpev(self)
        self.tk_table_lwemsjl4 = self.__tk_table_lwemsjl4( self.tk_label_frame_lwemrpev) 
        self.tk_button_lwemuitd = self.__tk_button_lwemuitd( self.tk_label_frame_lwemrpev) 
        self.tk_button_lwemtwz5 = self.__tk_button_lwemtwz5(self)
        self.tk_check_button_lweojus4 = self.__tk_check_button_lweojus4(self)
        self.tk_check_button_lweomgi5 = self.__tk_check_button_lweomgi5(self)
        self.tk_label_frame_lweoqumn = self.__tk_label_frame_lweoqumn(self)
        self.tk_check_button_lweor6yu = self.__tk_check_button_lweor6yu( self.tk_label_frame_lweoqumn) 
        self.tk_input_lweoshw6 = self.__tk_input_lweoshw6( self.tk_label_frame_lweoqumn) 
        self.tk_label_lweot0b3 = self.__tk_label_lweot0b3( self.tk_label_frame_lweoqumn) 
        self.tk_progressbar_lweouqqw = self.__tk_progressbar_lweouqqw(self)
        self.tk_button_lweovyrj = self.__tk_button_lweovyrj(self)
        self.tk_label_frame_lweowt2g = self.__tk_label_frame_lweowt2g(self)
        self.tk_text_lweoy6d5 = self.__tk_text_lweoy6d5( self.tk_label_frame_lweowt2g) 
        self.tk_check_button_lweoxfwy = self.__tk_check_button_lweoxfwy(self)
        self.tk_label_lwepishb = self.__tk_label_lwepishb(self)
        self.tk_input_lwepjh7a = self.__tk_input_lwepjh7a(self)
        self.tk_label_lwepjmn3 = self.__tk_label_lwepjmn3(self)
        self.tk_input_lwepju0f = self.__tk_input_lwepju0f(self)
    def __win(self):
        self.title("小红书点赞助手1.0")
        # 设置窗口大小、居中
        width = 1055
        height = 615
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_label_frame_lwemfsc4(self,parent):
        frame = LabelFrame(parent,text="账号列表",)
        frame.place(x=20, y=13, width=410, height=287)
        return frame
    def __tk_table_lwempfpz(self,parent):
        # 表头字段 表头宽度
        columns = {"ID":26,"账号":133,"状态":106}
        tk_table = Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=15, y=6, width=268, height=233)
        self.create_bar(parent, tk_table,True, False,15, 6, 268,233,410,287)
        return tk_table
    def __tk_button_lwemvqoh(self,parent):
        btn = Button(parent, text="新增", takefocus=False,)
        btn.place(x=319, y=5, width=50, height=30)
        return btn
    def __tk_button_lwemwxje(self,parent):
        btn = Button(parent, text="检测", takefocus=False,)
        btn.place(x=320, y=74, width=50, height=30)
        return btn
    def __tk_label_frame_lwemrpev(self,parent):
        frame = LabelFrame(parent,text="点赞链接列表",)
        frame.place(x=441, y=16, width=568, height=286)
        return frame
    def __tk_table_lwemsjl4(self,parent):
        # 表头字段 表头宽度
        columns = {"ID":89,"链接":224,"状态":134}
        tk_table = Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=29, y=20, width=450, height=229)
        self.create_bar(parent, tk_table,True, False,29, 20, 450,229,568,286)
        return tk_table
    def __tk_button_lwemuitd(self,parent):
        btn = Button(parent, text="清空", takefocus=False,)
        btn.place(x=503, y=98, width=50, height=30)
        return btn
    def __tk_button_lwemtwz5(self,parent):
        btn = Button(parent, text="导入", takefocus=False)
        btn.place(x=946, y=62, width=50, height=30)
        return btn
    def __tk_check_button_lweojus4(self,parent):
        cb = Checkbutton(parent,text="点赞完毕继续下一个帐号轮询",)
        cb.place(x=730, y=378, width=208, height=30)
        return cb
    def __tk_check_button_lweomgi5(self,parent):
        cb = Checkbutton(parent,text="开启无头模式(没有登陆的情况请取消勾选)",)
        cb.place(x=726, y=333, width=278, height=30)
        return cb
    def __tk_label_frame_lweoqumn(self,parent):
        frame = LabelFrame(parent,text="代理",)
        frame.place(x=17, y=328, width=286, height=178)
        return frame
    def __tk_check_button_lweor6yu(self,parent):
        cb = Checkbutton(parent,text="是否开启代理",)
        cb.place(x=20, y=10, width=145, height=30)
        return cb
    def __tk_input_lweoshw6(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=17, y=108, width=248, height=30)
        return ipt
    def __tk_label_lweot0b3(self,parent):
        label = Label(parent,text="代理地址(仅支持URL调用)",anchor="center", )
        label.place(x=20, y=60, width=169, height=30)
        return label
    def __tk_progressbar_lweouqqw(self,parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL,)
        progressbar.place(x=23, y=584, width=998, height=20)
        return progressbar
    def __tk_button_lweovyrj(self,parent):
        btn = Button(parent, text="开始点赞", takefocus=False,)
        btn.place(x=730, y=515, width=196, height=52)
        return btn
    def __tk_label_frame_lweowt2g(self,parent):
        frame = LabelFrame(parent,text="日志",)
        frame.place(x=322, y=330, width=382, height=241)
        return frame
    def __tk_text_lweoy6d5(self,parent):
        text = Text(parent)
        text.place(x=10, y=0, width=362, height=217)
        self.create_bar(parent, text,True, False, 10, 0, 362,217,382,241)
        return text
    def __tk_check_button_lweoxfwy(self,parent):
        cb = Checkbutton(parent,text="保存登陆状态",)
        cb.place(x=733, y=422, width=116, height=30)
        return cb
    def __tk_label_lwepishb(self,parent):
        label = Label(parent,text="点赞间隔时间(秒)",anchor="center", )
        label.place(x=730, y=470, width=116, height=30)
        return label
    def __tk_input_lwepjh7a(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=860, y=470, width=34, height=30)
        return ipt
    def __tk_label_lwepjmn3(self,parent):
        label = Label(parent,text="到",anchor="center", )
        label.place(x=910, y=470, width=33, height=30)
        return label
    def __tk_input_lwepju0f(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=960, y=470, width=35, height=30)
        return ipt

class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)
    def __event_bind(self):
        self.tk_button_lwemvqoh.bind('<Button-1>',self.ctl.addaccount)
        self.tk_button_lwemwxje.bind('<Button-1>',self.ctl.jiance)
        self.tk_button_lwemuitd.bind('<Button-1>',self.ctl.dellink)
        self.tk_button_lwemtwz5.bind('<Button-1>',self.ctl.daoru)
        self.tk_check_button_lweojus4.bind('<Button-1>',self.ctl.lunxun)
        self.tk_check_button_lweomgi5.bind('<Button-1>',self.ctl.nohead)
        self.tk_button_lweovyrj.bind('<Button-1>',self.ctl.dianzan)
        pass

    def __style_config(self):
        pass
    def add_account(self, event):
        print("新增账号")
    
    def jiance(self, event):
        print("检测账号")
    
    def dellink(self, event):
        print("清空链接")
    
    def daoru(self, event):
        print("导入链接")
    
    def lunxun(self, event):
        print("开启轮询")
    
    def nohead(self, event):
        print("开启无头模式")
    
    def dianzan(self, event):
        print("开始点赞")

    def __style_config(self):
        pass

if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()