# ai-data-script
大模型训练前置数据预处理Python工具集

## 项目简介
本仓库为AI数据处理实习练习代码，封装通用文本数据集预处理全套流程：
1. 原始数据集清洗：过滤空文本、异常脏数据、无效字符
2. 文本规范化：全角转半角、繁简体转换、特殊符号清理、停用词过滤
3. 样本去重：精确字符串去重、基于相似度模糊去重
4. 数据集划分：自动拆分训练集/验证集/测试集
5. 数据导出：支持csv、json、parquet格式输出

## 环境依赖
```bash
# 一键安装依赖
pip install pandas numpy jieba transformers datasets
