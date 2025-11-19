try:
    num1_string=input("请输入第一个数字")
    num1=float(num1_string)
    num2_string=input("请输入第二个数字")
    num2=float(num2_string)
    sum_result = num1 + num2
    print(f"结果是{sum_result}")
    input("\n计算完成，请按回车键退出...")
except ValueError:
    print("\n错误：请输入有效的数字！")
    input("发生错误，请按回车键退出...")
except Exception as e:
    print(e)
    input("发生意料之外的错误，请按回车键退出...")