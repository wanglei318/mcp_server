# MCP Server

这是一个使用Flask框架构建的Web应用，实现了一个简单的任务管理系统。

## 功能特点

- 使用Flask框架
- SQLAlchemy数据库ORM
- 任务的增删改查
- 响应式界面设计
- Bootstrap 5界面

## 项目结构

```
mcp_server/
├── app/                    # 应用包
│   ├── __init__.py        # 应用工厂
│   ├── models.py          # 数据模型
│   ├── routes.py          # 路由和视图
│   └── templates/         # HTML模板
│       └── index.html     # 主页模板
├── config.py              # 配置文件
├── run.py                 # 应用入口
├── requirements.txt       # 项目依赖
└── README.md             # 项目文档
```

## 安装说明

1. 克隆仓库：
   ```bash
   git clone https://github.com/wanglei318/mcp_server.git
   cd mcp_server
   ```

2. 创建虚拟环境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或
   .\venv\Scripts\activate  # Windows
   ```

3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

4. 运行应用：
   ```bash
   python run.py
   ```

访问 http://localhost:5000 查看应用。

## 功能说明

- 添加任务：在输入框中输入任务内容，点击"添加任务"按钮
- 完成任务：点击任务旁边的"完成"按钮
- 删除任务：点击任务旁边的"删除"按钮

## 技术栈

- Python 3.8+
- Flask 3.0.2
- SQLAlchemy
- Bootstrap 5
- SQLite数据库

## 开发说明

1. 数据库在首次运行时会自动创建
2. 开发模式下启用了调试功能
3. 可以通过环境变量配置数据库URL和密钥

## 许可证

MIT License