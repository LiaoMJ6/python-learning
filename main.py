# main.py —— 项目总入口
# 运行这个文件，一条命令跑通：读取数据 -> 分析统计 -> 输出报告

print('=' * 40)
print('          订单数据分析报告')
print('=' * 40)

# 导入 analyze 时，它会自动读取 orders.csv 并完成全部统计
import analyze

print('=' * 40)
print('          报告生成完毕')
print('=' * 40)
