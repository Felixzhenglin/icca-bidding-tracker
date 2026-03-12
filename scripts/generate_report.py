#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成 ICCA 竞标报告脚本
"""

import json
from datetime import datetime

def generate_report():
    """生成竞标报告"""
    
    print("正在生成 ICCA 竞标报告...")
    
    try:
        # 读取会议数据
        try:
            with open('meetings_temp.json', 'r', encoding='utf-8') as f:
                meetings = json.load(f)
            print(f"读取到 {len(meetings)} 个会议")
        except FileNotFoundError:
            print("未找到会议数据，使用示例")
            meetings = []
        
        # 生成报告内容
        report = f"""# ICCA 竞标报告

## 📅 生成时间
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 📊 会议汇总

"""
        
        if meetings:
            for i, meeting in enumerate(meetings, 1):
                report += f"""### {i}. {meeting.get('name', '未知会议')}
- **状态**: 🏆 已中标
- **链接**: {meeting.get('url', '')}
- **检索时间**: {meeting.get('retrieved_at', '')}

"""
        else:
            report += """> 暂无会议数据，请检查 retrieved_icca.py 脚本

"""
        
        report += """
## 📝 必填字段检查

报告应包含以下必填字段：
1. 📍 待举办地区
2. ⏰ 竞标截止时间
3. 👤 会议联络人
4. 📧 联络方式（邮箱）
5. 📊 会议规模（可选）

## 🔍 下一步

1. 将报告内容更新到飞书多维表格
2. 更新"最后更新时间"字段
3. 发送消息通知相关人员

"""
        
        # 保存报告
        with open('reports/ICCA_report.md', 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"报告已保存到: reports/ICCA_report.md")
        print(f"报告生成完成!")
        
        return True
        
    except Exception as e:
        print(f"生成报告出错: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    generate_report()
