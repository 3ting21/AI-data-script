import re

def clean_raw_text(text: str) -> str:
    """
    增强型文本清洗函数
    
    处理步骤：
    1. 去除URL/网址
    2. 去除Emoji表情
    3. 去除多余换行符
    4. 保留中文、英文、数字，清除其余特殊符号
    5. 压缩多余空格
    """
    if not text:
        return ""
    
    # 1. 去除URL/网址（http、https、www开头的链接）
    text = re.sub(r"https?://[^\s]+|www\.[^\s]+", "", text)
    
    # 2. 去除Emoji表情
    # 覆盖大多数emoji字符范围
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642"
        "\u2600-\u2B55"
        "\u200d"
        "\u23cf"
        "\u23e9"
        "\u231a"
        "\ufe0f"
        "\u3030"
        "]+",
        flags=re.UNICODE
    )
    text = emoji_pattern.sub(r"", text)
    
    # 3. 去除多余换行符（将多个换行符压缩为单个空格）
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"\r+", " ", text)
    
    # 4. 保留中文、英文、数字，清除其余特殊符号
    text = re.sub(r"[^\u4e00-\u9fa5a-zA-Z0-9\s]", "", text)
    
    # 5. 合并多个空格为单个空格并去除首尾空格
    text = re.sub(r"\s+", " ", text).strip()
    
    return text


# 自测入口
if __name__ == "__main__":
    # 原始测试
    test_input1 = "大模型@@数据预处理！！练习脚本#￥"
    print("测试1 - 特殊符号：", clean_raw_text(test_input1))
    
    # 新增测试用例
    test_input2 = "今天天气不错😊😄，推荐看这个网址https://github.com/test"
    print("测试2 - Emoji和URL：", clean_raw_text(test_input2))
    
    test_input3 = "这是第一行\n\n\n这是第二行\n这是第三行"
    print("测试3 - 多余换行：", clean_raw_text(test_input3))
    
    test_input4 = "综合测试🎉 访问www.example.com了解更多！！\n\n中文English123"
    print("测试4 - 综合测试：", clean_raw_text(test_input4))