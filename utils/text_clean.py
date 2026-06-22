import re

# 中文停用词表（常见的功能词）
CHINESE_STOPWORDS = {
    '的', '一', '是', '在', '不', '了', '有', '和', '人', '这',
    '中', '大', '为', '上', '个', '国', '我', '以', '要', '他',
    '时', '来', '用', '们', '生', '到', '作', '地', '于', '出',
    '就', '分', '对', '成', '会', '可', '主', '发', '年', '动',
    '同', '工', '也', '能', '下', '过', '民', '前', '面', '书',
    '着', '多', '从', '其', '后', '寸', '对', '说', '设', '要',
    '把', '那', '他', '她', '它', '什么', '这样', '就是', '下去',
    '一般', '几乎', '已经', '开始', '虽然', '但是', '因为', '所以',
    '然而', '况且', '再者', '首先', '其次', '最后', '总之', '总而言之',
}

# 英文停用词表（常见的功能词）
ENGLISH_STOPWORDS = {
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'with', 'by', 'from', 'up', 'about', 'into', 'through', 'during',
    'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
    'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might',
    'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it',
    'we', 'they', 'what', 'which', 'who', 'when', 'where', 'why', 'how',
}

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


def remove_stopwords(text: str, remove_chinese: bool = True, remove_english: bool = True) -> str:
    """
    去除停用词函数
    
    参数：
        text: 输入文本
        remove_chinese: 是否移除中文停用词，默认True
        remove_english: 是否移除英文停用词，默认True
    
    返回：
        移除停用词后的文本
    
    例子：
        >>> remove_stopwords("这���一个很好的例子")
        "好的例子"
    """
    if not text:
        return ""
    
    words = text.split()
    filtered_words = []
    
    for word in words:
        # 检查是否为停用词
        is_stopword = False
        
        # 检查中文停用词
        if remove_chinese and word in CHINESE_STOPWORDS:
            is_stopword = True
        
        # 检查英文停用词（转小写后检查）
        if remove_english and word.lower() in ENGLISH_STOPWORDS:
            is_stopword = True
        
        # 非停用词才保留
        if not is_stopword:
            filtered_words.append(word)
    
    return " ".join(filtered_words)


def clean_and_remove_stopwords(text: str, remove_stopwords_flag: bool = True) -> str:
    """
    完整的文本清洗流程：先清洗，再去停用词
    
    参数：
        text: 输入文本
        remove_stopwords_flag: 是否执行去停用词步骤，默认True
    
    返回：
        处理后的文本
    
    例子：
        >>> clean_and_remove_stopwords("这是一个很好的🎉例子，访问https://example.com")
        "好的例子"
    """
    # 第一步：基础清洗
    text = clean_raw_text(text)
    
    # 第二步：去停用词（可选）
    if remove_stopwords_flag:
        text = remove_stopwords(text)
    
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
    
    print("\n--- 去停用词测试 ---")
    
    # 去停用词测试
    test_input5 = "这是一个很好的例子 it is a good example"
    print("测试5 - 原始文本：", test_input5)
    print("去停用词后：", remove_stopwords(test_input5))
    
    test_input6 = "数据预处理是大模型训练的重要步骤"
    print("\n测试6 - 原始文本：", test_input6)
    print("去中文停用词：", remove_stopwords(test_input6, remove_chinese=True, remove_english=False))
    
    # 完整流程测试
    test_input7 = "这是一个很好的💯例子！！！访问www.test.com了解更多🎉"
    print("\n测试7 - 完整流程：")
    print("原始文本：", test_input7)
    print("只清洗：", clean_raw_text(test_input7))
    print("清洗+去停用词：", clean_and_remove_stopwords(test_input7, remove_stopwords_flag=True))
