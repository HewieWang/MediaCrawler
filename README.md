# 仓库描述
## UI
![QQ截图20240520175337.png](https://img2.imgtp.com/2024/05/20/fj9zU3np.png)
**小红书爬虫**，**抖音爬虫**， **快手爬虫**， **B站爬虫**， **微博爬虫**...。  
目前能抓取小红书、抖音、快手、B站、微博的视频、图片、评论、点赞、转发等信息。

原理：利用[playwright](https://playwright.dev/)搭桥，保留登录成功后的上下文浏览器环境，通过执行JS表达式获取一些加密参数
通过使用此方式，免去了复现核心加密JS代码，逆向难度大大降低

### 运行GUI
2024.5.9更新了授权码
   ```shell   
   python dianzan.py

   ```

## 功能列表
| 平台  | Cookie 登录 | 二维码登录 | 手机号登录 | 关键词搜索 | 指定视频/帖子 ID 爬取 | 登录状态缓存 | 数据保存 | IP 代理池 | 滑块验证码 |
|:---:|:---------:|:-----:|:-----:|:-----:|:-------------:|:------:|:----:|:------:|:-----:|
| 小红书 |     ✅     |   ✅   | ✅     |   ✅   |       ✅       |   ✅    |  ✅   |   ✅    |   ✕   |
| 抖音  |     ✅     |   ✅   | ✅     |   ✅   |       ✅       |   ✅    |  ✅   |   ✅    |   ✅   |
| 快手  |     ✅     |   ✅   | ✕     |   ✅   |       ✅       |   ✅    |  ✅   |   ✅    |    ✕   |
| B 站 |     ✅     |   ✅   | ✕     |   ✅   |       ✅       |   ✅    |  ✅   |   ✅    |   ✕   |
| 微博  |     ✅      |   ✅    | ✕     |   ✅    |       ✅        |    ✅    |   ✅   |    ✅    |   ✕   |


## 使用方法

### 创建并激活 python 虚拟环境
   ```shell   
   # 进入项目根目录
   cd MediaCrawler
   
   # 创建虚拟环境
   # 注意python 版本需要3.7 - 3.9 
   python -m venv venv
   
   # macos & linux 激活虚拟环境
   source venv/bin/activate

   # windows 激活虚拟环境
   venv\Scripts\activate

   ```

### 安装依赖库

   ```shell
   pip3 install -r requirements.txt
   ```

### 安装 playwright浏览器驱动

   ```shell
   playwright install
   ```

### 运行爬虫程序

   ```shell
   # 从配置文件中读取关键词搜索相关的帖子并爬取帖子信息与评论
   python main.py --platform xhs --lt qrcode --type search
   
   # 从配置文件中读取指定的帖子ID列表获取指定帖子的信息与评论信息
   python main.py --platform xhs --lt qrcode --type detail
  
   # 打开对应APP扫二维码登录
     
   # 其他平台爬虫使用示例，执行下面的命令查看
   python main.py --help    
   ```


### 数据保存
- 支持保存到关系型数据库（Mysql、PgSQL等）
    - 执行 `python db.py` 初始化数据库数据库表结构（只在首次执行）
- 支持保存到csv中（data/目录下）
- 支持保存到json中（data/目录下）
 

➡️➡️➡️ [常见问题](docs/常见问题.md)


## 项目代码结构
➡️➡️➡️ [项目代码结构说明](docs/项目代码结构.md)

## 手机号登录说明
➡️➡️➡️ [手机号登录说明](docs/手机号登录说明.md)


## 参考

- xhs客户端 [ReaJason的xhs仓库](https://github.com/ReaJason/xhs)
- 短信转发 [参考仓库](https://github.com/pppscn/SmsForwarder)
- 内网穿透工具 [ngrok](https://ngrok.com/docs/)
