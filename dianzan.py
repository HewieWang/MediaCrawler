import tkinter as tk
from tkinter import messagebox
import json
import datetime
import threading
import requests

LICENSE_URL = 'https://hewiewang.github.io/dev/xhs/licenses.json'
LICENSE_FILE = 'licenses.txt'

def load_license_info():
    try:
        with open(LICENSE_FILE, 'r') as file:
            license_info = file.read()

            licenses = load_remote_license_info()

            # print(licenses)
            if check_license(license_info, licenses):
                return license_info
            else:
                return None
    except FileNotFoundError:
        return None

def load_remote_license_info():
    try:
        response = requests.get(LICENSE_URL)
        if response.status_code == 200:
            licenses = json.loads(response.text)
            return licenses
        else:
            messagebox.showerror("错误", f"无法获取授权信息。")
            return []
    except Exception as e:
        messagebox.showerror("错误", f"发生异常：{e}")
        return []

def save_license_info(license_key):
    with open(LICENSE_FILE, 'w') as file:
        file.write(license_key)

def check_license(license_key, licenses):
    for license_info in licenses:
        if license_info.get('LICENSE_KEY') == license_key:
            expiration_date = datetime.datetime.strptime(license_info['EXPIRATION_DATE'], '%Y-%m-%d').date()
            if expiration_date >= datetime.date.today():
                return True
            else:
                return False
    return False

def hide_elements():
    entry_license_key.pack_forget()
    button_check_license.pack_forget()
    # label_instruction.pack_forget()
    label_status.pack()

def get_expiration_date(license_key, licenses):
    for license_info in licenses:
        if license_info.get('LICENSE_KEY') == license_key:
            expiration_date = datetime.datetime.strptime(license_info['EXPIRATION_DATE'], '%Y-%m-%d').date()
            return expiration_date
    return None

def on_check_license():
    license_key = entry_license_key.get()
    if not license_key:
        messagebox.showwarning("警告", "请输入授权码。")
        return

    threading.Thread(target=check_license_async, args=(license_key,), daemon=True).start()

def check_license_async(license_key):
    root.config(cursor="wait")
    label_status.config(text="正在验证授权，请稍候...")
    
    licenses = load_remote_license_info()
    if not licenses:
        root.config(cursor="")
        label_status.config(text="")
        return

    if check_license(license_key, licenses):
        messagebox.showinfo("成功", "授权验证通过，程序继续执行。")
        save_license_info(license_key)
        # root.after(100, lambda: root.destroy())
        hide_elements()
        expiration_date = get_expiration_date(license_key, licenses)
        remaining_days = (expiration_date - datetime.datetime.now().date()).days
        label_status.config(text=f"剩余有效期：{remaining_days} 天")
        open_new_window()


    else:
        messagebox.showerror("失败", "授权验证失败或授权已过期。请联系管理员获取有效授权。")
    
    root.config(cursor="")
    label_status.config(text="")

def open_new_window():

    new_root = tk.Toplevel()
    app = RedBookApp(new_root)
    new_root.mainloop()

def load_ids_from_file(filename):
    try:
        with open(filename, 'r') as file:
            ids = file.readlines()
            return [id.strip() for id in ids]
    except FileNotFoundError:
        messagebox.showerror("错误", f"文件 {filename} 不存在")
        return []

class RedBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("小红书点赞器")

        # 获取屏幕的宽度和高度
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # 获取窗口的宽度和高度
        window_width = 500
        window_height = 300

        # 计算窗口在屏幕中央的位置
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.id_list = load_ids_from_file("note_id.txt")

        self.create_table()
        self.create_button()

    def create_table(self):
        self.table_frame = tk.Frame(self.master)
        self.table_frame.pack(pady=10)

        self.id_label = tk.Label(self.table_frame, text="ID列表", bg="white", bd=1, relief="solid", width=40, height=2, anchor="center")
        self.id_label.grid(row=0, column=0)

        self.status_label = tk.Label(self.table_frame, text="状态", bg="white", bd=1, relief="solid", width=20, height=2, anchor="center")
        self.status_label.grid(row=0, column=1)

        num_rows = len(self.id_list)
        self.rows = []
        for i, id_ in enumerate(self.id_list, start=1):
            id_label = tk.Label(self.table_frame, text=id_, bg="white", bd=1, relief="solid", width=40, height=2, anchor="center")
            id_label.grid(row=i, column=0)

            status_var = tk.StringVar(value="未点赞")
            status_label = tk.Label(self.table_frame, textvariable=status_var, bg="white", bd=1, relief="solid", width=20, height=2, anchor="center")
            status_label.grid(row=i, column=1)

            self.rows.append((id_label, status_var))

    def create_button(self):
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()

        self.like_button = tk.Button(self.button_frame, text="开始点赞", command=self.like_posts)
        self.like_button.pack(pady=10)

    def like_posts(self):
        # 这里添加点赞的逻辑，可以根据需要进行修改
        for id_label, status_var in self.rows:
            status_var.set("点赞中...")


def main():
    license_key = load_license_info()
    print(license_key)
    if license_key is not None:
        open_new_window()
        return

    global root, entry_license_key, button_check_license, label_status

    root = tk.Tk()
    root.title("授权验证")

    # 获取屏幕的宽度和高度
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 获取窗口的宽度和高度
    window_width = 300
    window_height = 150

    # 计算窗口在屏幕中央的位置
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label_instruction = tk.Label(root, text="请输入授权码：")
    label_instruction.pack()

    entry_license_key = tk.Entry(root)
    entry_license_key.pack()

    button_check_license = tk.Button(root, text="验证授权", command=on_check_license)
    button_check_license.pack()

    label_status = tk.Label(root, text="", fg="blue")
    label_status.pack()

    root.mainloop()

    

if __name__ == "__main__":
    main()
