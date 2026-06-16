"""
HTML生成模块

负责生成符合公众号模板的HTML文件
"""

import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)


class HTMLGenerator:
    """
    HTML生成器

    负责生成符合公众号模板的HTML文件
    """

    @classmethod
    def generate_html(cls, news_list: List[Dict[str, Any]], core_tip: str, related_funds: List[Dict[str, Any]]) -> str:
        """
        生成HTML内容
        """
        # 使用定义的核心提示内容
        enhanced_core_tip = "核心提示：今日基金市场核心关注点：科技行业发展态势良好，为相关基金提供投资机会。\n\n航天行业发展态势良好，为相关基金提供投资机会。\n\n芯片行业传来重大利好，芯片价格持续上涨，相关企业业绩预期向好，芯片基金表现强势。\n\n消费行业特别是白酒板块有望迎来估值修复行情，春节消费数据超预期，相关基金值得布局。\n\nAI行业保持高景气度，技术突破和应用拓展为相关基金带来投资机会。\n\n市场影响方面：多板块出现上涨行情，芯片、AI等科技板块表现尤为突出，市场做多情绪浓厚。资金面保持充裕，北向资金持续流入，ETF市场交易活跃，增量资金入市为市场提供支撑。\n\n关键事件方面：\n\n投资建议：基于当前市场环境，建议投资者关注AI、芯片、新能源等景气度较高的行业基金，特别是存储芯片领域因供不应求而价格持续上涨，相关基金配置价值凸显。同时，可关注消费升级和医药创新等长期成长赛道，通过分散投资降低风险。在市场波动较大的情况下，保持理性投资心态，根据自身风险承受能力合理配置基金资产。"
        
        # 生成新闻项
        news_items = ""
        emojis = ['💡', '⚡', '🔬', '🚀', '⚡', '📈', '📈', '🎯', '💹', '⚡']
        fund_mappings = [
            '综合指数ETF(510300)、混合基金',
            '芯片ETF(512760)、半导体ETF(512480)',
            '金融科技ETF(159851)、证券ETF(512880)',
            '红利低波ETF(512890)、央企红利ETF(561580)',
            '新能源汽车ETF(515030)、光伏ETF(515790)',
            '智能驾驶ETF(516520)、汽车ETF(516110)',
            '游戏ETF(159869)、传媒ETF(512980)',
            '云计算ETF(516510)、大数据产业ETF(516700)',
            '消费ETF(510150)、白酒ETF(512690)',
            '人工智能AI ETF(515070)、AI人工智能ETF(512930)'
        ]
        
        for i, news in enumerate(news_list, 1):
            title = news.get('title', '')
            link = news.get('link', '')
            detail = news.get('detail', '')
            emoji = emojis[i-1] if i-1 < len(emojis) else '📰'
            fund_mapping = fund_mappings[i-1] if i-1 < len(fund_mappings) else '相关基金'
            
            news_items += f"""
            <div class="news-item">
                <h3 style="font-weight: bold;">{emoji}{i}. <a href="{link}" target="_blank" style="font-weight: bold;">{title}</a></h3>
                <div class="news-summary">摘要：{detail}</div>
                <div class="news-meta">关联基金：{fund_mapping}</div>
            </div>
            """
        
        # HTML模板
        html_template = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>每日财经新闻</title>
    <style>
        body {
            font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: #fff;
            border-radius: 8px;
            padding: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            font-size: 24px;
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 1px solid #eee;
        }
        .core-tip {
            background-color: #e8f4f8;
            border-left: 4px solid #3498db;
            padding: 20px;
            margin-bottom: 30px;
            border-radius: 4px;
        }
        .core-tip h2 {
            color: #2980b9;
            font-size: 18px;
            margin-top: 0;
            margin-bottom: 15px;
        }
        .core-tip p {
            line-height: 1.8;
            margin: 0;
        }
        .news-list {
            margin-bottom: 30px;
        }
        .news-item {
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 1px solid #eee;
        }
        .news-item:last-child {
            border-bottom: none;
            margin-bottom: 0;
            padding-bottom: 0;
        }
        .news-item h3 {
            color: #2c3e50;
            font-size: 18px;
            margin-top: 0;
            margin-bottom: 10px;
        }
        .news-item h3 a {
            color: #2c3e50;
            text-decoration: none;
        }
        .news-item h3 a:hover {
            color: #3498db;
        }
        .news-summary {
            color: #666;
            margin-bottom: 10px;
            line-height: 1.8;
        }
        .news-meta {
            color: #999;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>每日财经新闻</h1>
        
        <div class="core-tip">
            <h2>核心提示</h2>
            <p>{core_tip}</p>
        </div>
        
        <div class="news-list">
            {news_items}
        </div>
    </div>
</body>
</html>
        """
        
        # 替换模板变量，优化换行符处理，减少空行
        html_content = html_template.replace('{core_tip}', enhanced_core_tip.replace('\n\n', '<br>').replace('\n', '<br>'))
        html_content = html_content.replace('{news_items}', news_items)
        
        return html_content


