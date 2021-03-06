### 1.测试框架介绍 <h3> 
本项目是基于python3+selenium+unittest+DDT数据驱动+关键字驱动实现的Web自动化测试框架，特点如下：
* 采用POM设计模式，复用性高容易维护
* 采用关键字驱动对selenium的常用方法进行了二次封装
* DDT数据驱动，测试数据和测试脚本进行了分离
* 使用HTMLTestRunner自动生成测试报告，并发送邮件
* logging日志输出，便于定位问题
### 2.测试目录结构介绍 <h3> 
* config/: 文件路径配置
* data/: 测试用例数据文件
* drivers/: 浏览器驱动
* log/: 生成日志文件
* report/: 测试报告
* test/: 业务相关文件
   *  base_page/: 封装页面基类
    * pages/: 封装各页面业务
   *  testcase/: 编写测试用例
* utils：封装工具类，例如日志、发送邮件、读取excel数据、读取配置文件
* run_main.py: 执行所有测试用例的主程序

### 3.测试报告 <h3> 
![image](https://user-images.githubusercontent.com/78137626/131795765-55b0d559-3c40-4ff2-9e54-a205806f7c34.png)

### 4.日志 <h3> 
![image](https://user-images.githubusercontent.com/78137626/131796109-f17b13cf-f2fa-403b-a766-afd9a5aa79f5.png)
