"""
财经新闻爬取生成工具 - 主程序入口

功能描述:
    本脚本从多个财经网站抓取最新的财经新闻，
    经过数据处理后生成符合公众号模板的HTML文件，
    并将数据按平台和日期保存到JSON文件。

主要特性:
    1. 支持从多个财经网站获取新闻
    2. 自动提取新闻核心信息
    3. 生成符合公众号模板的HTML格式
    4. 包含基金相关信息和推荐
    5. 支持自动化更新
    6. 数据按平台和日期保存到JSON文件

使用方式:
    直接运行: python app.py
    生成的文件: 
        - index.html（项目根目录）
        - data/YYYY/MM/DD/*.json（数据目录）

作者: Auto-generated
版本: 2.0
"""

import logging
from modules import NewsFetcher, NewsProcessor, FundAnalyzer, HTMLGenerator, DataSaver

# =============================================================================
# 日志配置
# =============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class App:
    """
    应用主类

    负责协调各个模块，完成新闻的获取、处理、保存和HTML生成
    """

    def __init__(self):
        self.news_fetcher = NewsFetcher()
        self.news_processor = NewsProcessor()
        self.fund_analyzer = FundAnalyzer()
        self.html_generator = HTMLGenerator()
        self.data_saver = DataSaver()

    def run(self):
        """
        运行应用
        """
        print("开始获取财经新闻...")
        logger.info("开始获取财经新闻...")
        
        try:
            # 获取新闻
            print("获取东方财富网新闻...")
            eastmoney_news = self.news_fetcher.fetch_eastmoney_news(20)
            print(f"东方财富网新闻获取完成，共 {len(eastmoney_news)} 条")
            
            print("获取新浪财经新闻...")
            sina_news = self.news_fetcher.fetch_sina_finance_news(20)
            print(f"新浪财经新闻获取完成，共 {len(sina_news)} 条")
            
            print("获取每日经济新闻...")
            nbd_news = self.news_fetcher.fetch_nbd_news(20)
            print(f"每日经济新闻获取完成，共 {len(nbd_news)} 条")
            
            print("获取同花顺财经新闻...")
            jqka_news = self.news_fetcher.fetch_10jqka_news(20)
            print(f"同花顺财经新闻获取完成，共 {len(jqka_news)} 条")
            
            # 保存新闻数据到JSON文件（按平台和日期）
            print("保存新闻数据到JSON文件...")
            news_data = {
                'eastmoney': eastmoney_news,
                'sina': sina_news,
                'nbd': nbd_news,
                '10jqka': jqka_news
            }
            save_dir = self.data_saver.save_news_to_json(news_data)
            print(f"新闻数据已保存到目录: {save_dir}")
            
            # 合并新闻列表
            all_news = eastmoney_news + sina_news + nbd_news + jqka_news
            print(f"合并新闻列表完成，共 {len(all_news)} 条")
            
            # 去重
            unique_news = []
            seen_titles = set()
            seen_detail_prefixes = set()
            for news in all_news:
                title = news.get('title', '')
                detail = news.get('detail', '')
                # 确保标题不重复，并且摘要的前100个字符
                if title and detail and title not in seen_titles:
                    # 检查摘要前缀是否重复
                    detail_prefix = detail[:100] if len(detail) > 100 else detail
                    if detail_prefix not in seen_detail_prefixes:
                        seen_titles.add(title)
                        seen_detail_prefixes.add(detail_prefix)
                        unique_news.append(news)
            print(f"去重完成，共 {len(unique_news)} 条")
            
            # 处理新闻，过滤出基金相关新闻
            processed_news, _ = self.news_processor.process_news(unique_news)
            print(f"处理新闻完成，共 {len(processed_news)} 条")
            
            # 确保至少有10条新闻
            if len(processed_news) < 10:
                print(f"警告：新闻数量不足10条，实际获取: {len(processed_news)}条")
                logger.warning(f"新闻数量不足10条，实际获取: {len(processed_news)}条")
            
            # 生成核心提示
            print("生成核心提示...")
            core_tip = self.news_processor.generate_core_tip(processed_news)
            print("核心提示生成完成")
            
            # 分析基金相关信息
            print("分析基金相关信息...")
            related_funds = self.fund_analyzer._get_related_funds(processed_news)
            print(f"基金相关信息分析完成，共 {len(related_funds)} 条")
            
            # 生成HTML内容
            print("生成HTML内容...")
            html_content = self.html_generator.generate_html(processed_news, core_tip, related_funds)
            print("HTML内容生成完成")
            
            # 保存HTML到文件
            output_file = 'index.html'
            print(f"保存HTML到文件: {output_file}")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"HTML文件保存完成: {output_file}")
            
            logger.info(f"HTML文件已生成: {output_file}")
            logger.info(f"共生成 {len(processed_news)} 条新闻")
        except Exception as e:
            print(f"发生错误: {str(e)}")
            logger.error(f"发生错误: {str(e)}")
            import traceback
            traceback.print_exc()


if __name__ == '__main__':
    app = App()
    app.run()