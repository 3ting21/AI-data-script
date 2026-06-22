import sys
sys.path.append(".")

from utils.text_clean import clean_raw_text
from utils.text_truncate import truncate_text

if __name__ == "__main__":
    raw_text = "人工智能数据集清洗@样本去重练习"
    clean_result = clean_raw_text(raw_text)
    print("清洗前文本：", raw_text)
    print("清洗后文本：", clean_result)

    demo_text = "人工智能文本截断示例，包含中文和 English 混合内容。"
    print("\n=== text_truncate 演示 ===")
    print("原文：", demo_text)
    print("限制12字符，带省略号：", truncate_text(demo_text, 12))
    print("限制12字符，不带省略号：", truncate_text(demo_text, 12, add_ellipsis=False))
    print("限制12字符，保留词语边界：", truncate_text(demo_text, 12, preserve_word=True))