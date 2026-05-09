# API测试项目

## 项目简介
这是一个API自动化测试项目，使用pytest框架编写测试用例，通过GitHub Actions实现CI/CD自动化。

## 本地运行测试

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行测试
```bash
pytest test-case1.py -v
```

### 3. 查看测试报告
```bash
pytest test-case1.py --html=reports/test-report.html --self-contained-html
```

## CI/CD说明

### 自动触发
- 推送代码到 `main/master` 分支时自动运行测试
- 创建Pull Request时自动运行测试

### 查看结果
1. 进入GitHub仓库
2. 点击 **Actions** 标签
3. 查看最近的运行记录
4. 点击下载测试报告

## 项目结构
```
api-test-cicd/
├── .github/workflows/ci.yml  # CI/CD配置
├── requirements.txt           # 依赖包
├── pytest.ini                 # 测试配置
├── test-case1.py              # 测试用例
└── README.md                  # 说明文档
```

## 技术栈
- **测试框架**: pytest
- **CI/CD工具**: GitHub Actions
- **Python版本**: 3.9+
