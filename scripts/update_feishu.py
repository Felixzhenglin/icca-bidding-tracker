#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新飞书多维表格脚本
"""

import requests
import json

def update_feishu_table():
    """更新飞书多维表格"""
    
    # 从环境变量读取配置
    app_id = "cli_a994361f73b85cd2"
    app_secret = "2EYHbKL9A4dzSzpD4t2eBe3YY2f7fmrG"
    app_token = "G1kybHcb7ajRwLscJJBcfQbhncf"
    table_id = "tblkAj8VMvK90PnY"
    
    print(f"正在更新飞书表格：{app_token}/{table_id}")
    
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
        
        # 读取临时会议数据
        try:
            with open('meetings_temp.json', 'r', encoding='utf-8') as f:
                meetings = json.load(f)
            print(f"读取到 {len(meetings)} 个会议数据")
        except FileNotFoundError:
            print("未找到 meetings_temp.json，使用示例数据")
            meetings = []
        
        # 这里是示例代码，实际需要根据表格字段结构更新
        print("表格更新逻辑需要根据实际字段结构调整")
        print("当前演示模式，不会实际更新飞书表格")
        
        # 示例：更新"最后更新时间"字段
        from datetime import datetime
        update_time = datetime.now().isoformat()
        print(f"最后更新时间：{update_time}")
        
        return True
        
    except Exception as e:
        print(f"更新出错：{e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    update_feishu_table()
