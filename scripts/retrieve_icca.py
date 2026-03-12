#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ICCA 官网 Bid Wins 数据检索脚本
"""

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def retrieve_icca_bid_wins():
    """检索 ICCA 官网 Bid Wins 页面"""
    url = "https://www.iccaworld.org/news/bid-wins/"
    
    print(f"正在检索 ICCA 官网 Bid Wins: {url}")
    
    try:
        # 发送请求
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # 解析 HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 查找所有会议条目
        meetings = []
        
        # ICCA 网站结构可能变化，这里使用更通用的查找方式
        content = soup.find('div', class_='content')
        if not content:
            content = soup.find('article')
        if not content:
            content = soup
        
        # 查找所有链接
        links = content.find_all('a', href=True)
        
        for link in links:
            href = link.get('href', '')
            text = link.text.strip()
            
            # 检查是否为 ICCA 会议链接
            if 'iccaworld' in href and 'bid-wins' not in href:
                # 这是一个可能的会议链接
                meetings.append({
                    'name': text or href.split('/')[-1],
                    'url': href,
                    'status': 'bid_win',
                    'retrieved_at': datetime.now().isoformat()
                })
        
        print(f"共检索到 {len(meetings)} 个潜在会议")
        
        # 保存到临时文件（后续步骤会读取）
        import json
        with open('meetings_temp.json', 'w', encoding='utf-8') as f:
            json.dump(meetings, f, ensure_ascii=False, indent=2)
        
        print("会议数据已保存到 meetings_temp.json")
        
        return meetings
        
    except Exception as e:
        print(f"检索出错：{e}")
        return []

if __name__ == "__main__":
    retrieve_icca_bid_wins()
