from Common import HTMLTestRunner_cn
import unittest
import os

# # 查找测试用例
#
# startdir = "E:\\CRM\\CMTestProject\\Cases"
# discover = unittest.defaultTestLoader.discover(start_dir=startdir,
#                                                pattern="test*.py")
# print(discover)
#
#
#
# # 生成测试报告
#
# report_path = "E:\\CRM\\CMTestProject\\Report\\result.html"
#
# runner = HTMLTestRunner_cn.HTMLTestRunner(stream=open(report_path, "wb"),
#                                           verbosity=2,
#                                           title="TestReport",
#                                           description="此报告用于测试快速录入测试")
#
# # 执行用例
# runner.run(discover)

# 动态导入用例和测试报告路径
curpath = os.path.realpath(__file__)
curprojpath = os.path.dirname(curpath)

startdir = os.path.join(curprojpath,"Case")
discover = unittest.defaultTestLoader.discover(start_dir=startdir,
                                               pattern='test*.py')

report =os.path.join(curprojpath,"Report")
report_path = os.path.join(report,"result.html")
fp = open(report_path, "wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                          verbosity=2,
                                          title='TestReport',
                                          description='此报告用于测试快速录入测试')

runner.run(discover)
fp.close()




