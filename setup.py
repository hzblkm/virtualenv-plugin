from setuptools import setup

setup(
    name='virtualenv-plugin',
    version='0.1',
    description='Python虚拟环境管理插件',
    author='hzblkm',
    author_email='hzblkm@gmail.com',
    py_modules=['install_env'],
    install_requires=[
        'trae>=1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'venv-plugin=install_env:main',
        ],
        'trae.plugins': [
            'virtualenv=install_env:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['trae_plugin.json'],
    },
)