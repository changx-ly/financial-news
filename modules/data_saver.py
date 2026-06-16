"""
数据保存模块

负责将新闻数据按平台和日期保存到JSON文件
"""

import os
import json
import logging
from typing import Dict, List, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class DataSaver:
    """
    数据保存器
    
    负责将新闻数据按平台和日期保存到JSON文件
    """
    
    @staticmethod
    def save_news_to_json(news_data: Dict[str, List[Dict[str, Any]]]) -> str:
        """
        将新闻数据按平台和日期保存到JSON文件
        
        Args:
            news_data: 按平台分类的新闻数据字典，格式为：
                      {
                          'eastmoney': [...],
                          'sina': [...],
                          'nbd': [...],
                          '10jqka': [...]
                      }
        
        Returns:
            保存的目录路径
        """
        # 获取当前日期
        now = datetime.now()
        year = now.strftime('%Y')
        month = now.strftime('%m')
        day = now.strftime('%d')
        
        # 创建目录结构: data/YYYY/MM/DD/
        base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', year, month, day)
        os.makedirs(base_dir, exist_ok=True)
        
        # 保存每个平台的新闻数据
        for platform, news_list in news_data.items():
            if not news_list:
                continue
                
            # 生成文件名: platform_YYYYMMDD_HHMMSS.json
            timestamp = now.strftime('%Y%m%d_%H%M%S')
            filename = f"{platform}_{timestamp}.json"
            filepath = os.path.join(base_dir, filename)
            
            # 构建保存的数据结构
            data_to_save = {
                'platform': platform,
                'fetch_time': now.strftime('%Y-%m-%d %H:%M:%S'),
                'count': len(news_list),
                'news': news_list
            }
            
            # 保存到JSON文件
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data_to_save, f, ensure_ascii=False, indent=2)
            
            logger.info(f"保存 {platform} 新闻到: {filepath}")
            print(f"保存 {platform} 新闻到: {filepath}")
        
        return base_dir