# Python虚拟环境管理插件

这是一个用于管理Python虚拟环境的Trae插件，可以帮助开发者更方便地创建和管理Python虚拟环境。

## 功能特点

- 创建虚拟环境
- 管理Python包依赖
- 简化环境配置过程

## 安装方法

```bash
pip install virtualenv-plugin
```

或者通过Trae安装：

```bash
trae install virtualenv-plugin
```

## 使用方法

1. 创建新的虚拟环境：
```bash
trae virtualenv create
```

2. 激活虚拟环境：
```bash
trae virtualenv activate
```

3. 管理包依赖：
```bash
trae virtualenv install <package_name>
```

## 配置说明

可以在配置文件中自定义虚拟环境目录：

```json
{
  "venv_dir": "custom_venv"
}
```

## 贡献指南

欢迎提交Issue和Pull Request来帮助改进这个项目。

## 许可证

本项目采用MIT许可证。