
import os

class BasePath:
    pass


class ProjectPath(BasePath):
    # 项目路径
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 测试用例数据的路径
    DATA_PATH = os.path.join(ROOT_PATH, 'data')
    # 配置文件路径
    CONFIG_PATH = os.path.join(ROOT_PATH, 'setting')
    # 测试用例方法路径
    CASE_PATH = os.path.join(ROOT_PATH, 'Case')
    # 测试报告路径
    REPORT_PATH = os.path.join(ROOT_PATH, 'test_result')
    # 如果没有改文件夹，自动创建
    if not os.path.exists(REPORT_PATH):
        os.mkdir(REPORT_PATH)

class SubPath(ProjectPath):
    pass


p_path = ProjectPath()
print(p_path.DATA_PATH)
