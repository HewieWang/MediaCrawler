import tkinter as tk
from tkinter import messagebox
import json
import datetime
import threading
import requests

LICENSE_URL = 'https://hewiewang.github.io/dev/xhs/licenses.json'
LICENSE_FILE = 'licenses.json'

def load_license_info():
    try:
        with open(LICENSE_FILE, 'r') as file:
            license_key = file.read().strip()
            if not license_key:
                return None
            return license_key
    except FileNotFoundError:
        return None

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

def on_check_license():
    license_key = entry_license_key.get()
    if not license_key:
        messagebox.showwarning("警告", "请输入授权码。")
        return

    threading.Thread(target=check_license_async, args=(license_key,), daemon=True).start()

def check_license_async(license_key):
    root.config(cursor="wait")
    label_status.config(text="正在验证授权，请稍候...")
    
    licenses = load_license_info()
    if licenses is None:
        messagebox.showerror("失败", "授权验证失败或授权已过期。请联系管理员获取有效授权。")
        root.config(cursor="")
        label_status.config(text="")
        return

    if check_license(license_key, licenses):
        messagebox.showinfo("成功", "授权验证通过，程序继续执行。")
        save_license_info(license_key)
        root.destroy()
        open_new_window()
    else:
        messagebox.showerror("失败", "授权验证失败或授权已过期。请联系管理员获取有效授权。")
    
    root.config(cursor="")
    label_status.config(text="")

def open_new_window():
    new_root = tk.Tk()
    new_root.title("新窗口")
    new_root.geometry("300x150")

    label = tk.Label(new_root, text="授权验证成功！")
    label.pack()

    new_root.mainloop()

def main():
    license_key = load_license_info()
    if license_key is not None:
        open_new_window()
        return

    global root, entry_license_key, button_check_license, label_status

    root = tk.Tk()
    root.title("授权验证")
    root.geometry("300x150")

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
