import sys
sys.path.append(".")

from utils.text_clean import clean_raw_text

if __name__ == "__main__":
    raw_text = "人工智能数据集清洗@样本去重练习"
    clean_result = clean_raw_text(raw_text)
    print("清洗前文本：", raw_text)
    print("清洗后文本：", clean_result)