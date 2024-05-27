import random,os
from playwright.sync_api import sync_playwright, TimeoutError

def ensure_xiaohongshu_url(input_string):
    if "http" not in input_string:
        input_string = "https://www.xiaohongshu.com/explore/" + input_string
    return input_string

def login_xhs(headless=False,proxy=False,proxy_url=""):
    # Launch the browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        if os.path.exists("auth/state.json"):
            context = browser.new_context(storage_state="auth/state.json")
            page = context.new_page()
            pass
        else:
            # Create a new page
            page = browser.new_page()

        page.set_default_timeout(0)
        # Add init script
        page.context.add_init_script(path='C:/Users/Administrator/Desktop/stealth.min.js')

        # Set proxy if needed
        # Replace 'proxy_server' and 'proxy_port' with your proxy server details
        # page.context.set_http_proxy('proxy_server:proxy_port')

        # Open the page
        page.goto('https://www.xiaohongshu.com/explore')
        page.click(".login-btn")

        while True:
            page.goto("https://creator.xiaohongshu.com/creator/home")
            if page.title=="小红书创作服务平台":
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"----登录成功")
                break;
            else:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"----正在登录")
            pass


        print("登录成功")
        notes=[
            "https://www.xiaohongshu.com/explore/664ab2bb00000000150137d6",
            "https://www.xiaohongshu.com/explore/664da40c000000000c019638",
            "https://www.xiaohongshu.com/explore/6636fa44000000001e034238"
        ]

        for n in notes:
            page.goto(ensure_xiaohongshu_url(n))
            page.click(".interactions.engage-bar .like-lottie")
        pass  
        # storage = page.context.storage_state(path="auth/state.json")

        
    pass

def main():
    login_xhs()
    pass

if __name__ == "__main__":
    main()