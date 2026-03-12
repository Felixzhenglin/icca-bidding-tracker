#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
发送飞书消息脚本
"""

import requests
import json
from datetime import datetime

def send_feishu_message():
    """发送飞书消息"""
    
    app_id = "cli_a994361f73b85cd2"
    app_secret = "2EYHbKL9A4dzSzpD4t2eBe3YY2f7fmrG"
    user_open_id = "ou_87b9878f58c5ef10bf70ba072160782b"
    
    print("正在发送飞书消息...")
    
    try:
        # 获取 tenant_access_token
        token_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
        token_payload = {
            "app_id": app_id,
            "app_secret": app_secret
        }
        
        token_response = requests.post(token_url, json=token_payload)
        token_response.raise_for_status()
        
        token_data = token_response.json()
        tenant_token = token_data.get("tenant_access_token")
        
        if not tenant_token:
            print("获取 tenant_access_token 失败")
            return
        
        print("已获取 tenant_access_token")
        
        # 构建消息
        message_content = f"""# 📊 ICCA 竞标检索完成

**执行时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## ✅ 任务完成

- 📡 数据检索: 完成
- 📊 表格更新: 完成  
- 📝 报告生成: 完成

## 🔗 相关链接

- 📋 飞书多维表格: https:// ICCA-table-url
- 📄 本地报告: reports/ICCA_report.md

## 📌 下一步

1. 检查飞书表格中的数据
2. 确认中标会议信息
3. 准备竞标材料

---
*本消息由 ICCA 每日检索系统自动发送*

"""
        
        # 这里是示例代码，实际发送需要使用飞书 API
        # 示例：发送到用户
        print(f"消息内容预览:")
        print(message_content)
        print(f"目标用户: {user_open_id}")
        
        print("消息发送逻辑需要根据实际需求调整")
        print("当前演示模式，不会实际发送消息")
        
        return True
        
    except Exception as e:
        print(f"发送消息出错: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    send_feishu_message()
