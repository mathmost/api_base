# api_autotest_base
基于pytest allure yaml实现接口自动化的base业务，可根据环境设置不同的参数，比如邮件通知、数据库以及redis的使用等

1. 根据不同环境自行修改env_cof.py文件的配置信息<br/>

2. 根据env_cof.py文件的app对象设置的环境加载配置信息结合pytest收集并执行用例<br/>

3. task文件下存在生成报告及邮件发送，安装步骤如下（个人操作）<br/>
  pip install celery-with-redis<br/>
  pip uninstall celery && pip uninstall redis<br/>
  pip install celery && pip install redis<br/>

4. 本地安装mysql以及redis<br/>

5. 启动celery异步任务<br/>
  celery -A report.demo.tasks worker --concurrency=1000 -P eventlet<br/>
  ps: report.demo.tasks为当前任务脚本所在的目录
  
6. 以上都准备完成后, report_demo下运行主入口: run.py<br/>
  ps: 修改env_cof.py下的域名则需要在pages下修改登录接口以及可能调用了登录接口的文件<br/>

ps<br/>
  1. 建议在utils下封装的脚本除必须条件都使用单例，在constans.py的case_data类中添加该对象, 调用封装脚本，只需要在用例中导入case_data实例<br/>
  2. 可以在utils下封装微信、企业微信、钉钉等一系列后置通知或者封装其他公共处理的脚本<br/>
  3. case_data实例的全局变量、局部变量皆可以在整个项目中使用，如果考虑需要写入文件做后续的预览或者其他项目的使用则在实体类中对应的set()方法中添加写入文件代码<br/>
  4. 重要<br/>
    a. 该框架仅为base<br/>
    b. 接口放在pages目录下, 需要根据接口文档及业务自行添加接口<br/>
    c. 用例放在cases目录下，遵循pytest.ini自定义或者默认的文件、方法等命名规则<br/>
    d. 测试数据以yaml形式封装在cases_data目录下, 需根据业务自行添加模块数据<br/>
  5. 已经在cases用例目录提供了最基本的login session result 变量池等demo的使用<br/>
  6. 如何安装mysql redis以及邮件通知的设置请自行百度
  7. 如果需要测试登录模块, 尽可能避免env_cof.py文件的登录信息与登录模块的用例数据冲突，避免业务上导致session或者toke过期

