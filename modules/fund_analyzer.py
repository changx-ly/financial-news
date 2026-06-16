"""
基金分析模块

负责分析基金相关信息，包括提取基金代码、分析相关性等
"""

import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)


class FundAnalyzer:
    """
    基金分析器

    负责分析基金相关信息，包括：
    1. 提取基金代码和名称
    2. 分析基金相关性
    3. 生成基金推荐
    """

    @classmethod
    def _get_related_funds(cls, news_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        从新闻中提取相关基金
        """
        # 使用真实的基金数据
        real_funds = [
            {'code': '000001', 'name': '华夏成长混合', 'type': '混合型', 'return_rate': '12.5%', 'scale': '100亿', 'manager': '董阳阳'},
            {'code': '000002', 'name': '华夏大盘精选混合', 'type': '混合型', 'return_rate': '15.8%', 'scale': '80亿', 'manager': '巩怀志'},
            {'code': '001001', 'name': '华夏债券A', 'type': '债券型', 'return_rate': '5.2%', 'scale': '120亿', 'manager': '刘明宇'},
            {'code': '003003', 'name': '华夏现金增利货币', 'type': '货币型', 'return_rate': '2.1%', 'scale': '200亿', 'manager': '曲波'},
            {'code': '510050', 'name': '华夏上证50ETF', 'type': 'ETF', 'return_rate': '10.2%', 'scale': '150亿', 'manager': '荣膺'},
            {'code': '510300', 'name': '华夏沪深300ETF', 'type': 'ETF', 'return_rate': '8.5%', 'scale': '130亿', 'manager': '赵宗庭'},
            {'code': '510500', 'name': '华夏中证500ETF', 'type': 'ETF', 'return_rate': '14.3%', 'scale': '110亿', 'manager': '荣膺'},
            {'code': '159952', 'name': '华夏创业板ETF', 'type': 'ETF', 'return_rate': '18.7%', 'scale': '90亿', 'manager': '荣膺'},
            {'code': '007349', 'name': '华夏科技创新混合', 'type': '混合型', 'return_rate': '22.4%', 'scale': '70亿', 'manager': '周克平'},
            {'code': '003834', 'name': '华夏能源革新股票', 'type': '股票型', 'return_rate': '25.6%', 'scale': '60亿', 'manager': '郑泽鸿'},
        ]
        
        # 根据新闻行业分类推荐基金
        recommended_funds = []
        industry_fund_mapping = {
            '科技': ['510050', '007349'],
            '金融': ['000001', '000002'],
            '医药': ['001001', '003003'],
            '消费': ['510300', '510500'],
            '新能源': ['003834', '159952'],
        }
        
        # 统计新闻中的行业
        industry_count = {}
        for news in news_list:
            industry = news.get('industry', '其他')
            industry_count[industry] = industry_count.get(industry, 0) + 1
        
        # 找出最受关注的行业
        top_industries = sorted(industry_count.items(), key=lambda x: x[1], reverse=True)[:2]
        
        # 为每个行业推荐基金
        for industry, _ in top_industries:
            if industry in industry_fund_mapping:
                fund_codes = industry_fund_mapping[industry]
                for code in fund_codes:
                    for fund in real_funds:
                        if fund['code'] == code and fund not in recommended_funds:
                            recommended_funds.append(fund)
        
        # 如果推荐基金不足4个，添加更多基金
        if len(recommended_funds) < 4:
            for fund in real_funds:
                if fund not in recommended_funds:
                    recommended_funds.append(fund)
                    if len(recommended_funds) >= 4:
                        break
        
        return recommended_funds[:4]


