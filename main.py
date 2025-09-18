def main():
    num = input().strip()  # 读取输入并去除首尾空格
    # 判断输入是否为纯数字，且长度为5
    if not num.isdigit() or len(num) != 5:
        print("输入错误: 请输入5位数字")
    else:
        if num == num[::-1]:
            print("是回文数")
        else:
            print("不是回文数")
if __name__ == "__main__":
    main()
