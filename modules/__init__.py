"""
财经新闻爬取生成工具 - 模块包

该包包含以下模块：
- news_fetcher: 新闻获取模块
- news_processor: 新闻处理模块
- fund_analyzer: 基金分析模块
- html_generator: HTML生成模块
- data_saver: 数据保存模块
"""

from .news_fetcher import NewsFetcher
from .news_processor import NewsProcessor
from .fund_analyzer import FundAnalyzer
from .html_generator import HTMLGenerator
from .data_saver import DataSaver

__all__ = [
    'NewsFetcher',
    'NewsProcessor',
    'FundAnalyzer',
    'HTMLGenerator',
    'DataSaver'
]