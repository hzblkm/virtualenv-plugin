import os
import sys
import subprocess
import argparse

VENV_DIR = "venv"


def create_virtualenv():
    if not os.path.exists(VENV_DIR):
        print("正在创建虚拟环境...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_DIR])
        print("虚拟环境创建成功！")
    else:
        print("虚拟环境已存在。")

def activate_virtualenv():
    if sys.platform == "win32":
        activate_script = os.path.join(VENV_DIR, "Scripts", "activate.bat")
    else:
        activate_script = os.path.join(VENV_DIR, "bin", "activate")
    
    if os.path.exists(activate_script):
        print(f"正在激活虚拟环境...")
        try:
            subprocess.check_call([activate_script], shell=True)
            print("虚拟环境激活成功！")
        except subprocess.CalledProcessError:
            print(f"激活失败，请手动运行: {activate_script}")
    else:
        print("未找到激活脚本，请确认虚拟环境已正确创建。")


def parse_args():
    parser = argparse.ArgumentParser(description='Python虚拟环境管理工具')
    parser.add_argument('--create', '-c', action='store_true', help='创建新的虚拟环境')
    parser.add_argument('--activate', '-a', action='store_true', help='激活虚拟环境')
    parser.add_argument('--path', '-p', default=VENV_DIR, help='指定虚拟环境路径（默认：venv）')
    return parser.parse_args()

def main():
    args = parse_args()
    global VENV_DIR
    VENV_DIR = args.path

    if args.create:
        create_virtualenv()
    if args.activate:
        activate_virtualenv()
    if not (args.create or args.activate):
        # 如果没有指定参数，则执行所有操作
        create_virtualenv()
        activate_virtualenv()

if __name__ == "__main__":
    main()