import re

def clean_raw_text(text: str) -> str:
    """基础文本清洗：过滤特殊符号、压缩多余空格"""
    if not text:
        return ""
    # 保留中文、英文、数字，清除其余特殊符号
    text = re.sub(r"[^\u4e00-\u9fa5a-zA-Z0-9\s]", "", text)
    # 合并多个空格为单个空格并去除首尾空格
    text = re.sub(r"\s+", " ", text).strip()
    return text

# 自测入口
if __name__ == "__main__":
    test_input = "大模型@@数据预处理！！练习脚本#￥"
    print("清洗结果：", clean_raw_text(test_input))