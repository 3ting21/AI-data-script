def truncate_text(text: str, max_len: int, add_ellipsis: bool = True) -> str:
    """
    文本长度截断工具
    :param text: 原始文本
    :param max_len: 允许最大字符数
    :param add_ellipsis: 超长是否添加末尾省略号
    :return: 截断后文本
    """
    if len(text) <= max_len:
        return text
    # 截断文本
    cut = text[:max_len]
    if add_ellipsis:
        cut = cut + "..."
    return cut


# 内置自测
if __name__ == "__main__":
    test_str = "人工智能文本预处理工具，包含清洗、去停用词、数字过滤、文本长度截断全套功能"
    print("=== 文本截断独立模块自测 ===")
    print("原文：", test_str)
    print("限制20字符，带省略号：", truncate_text(test_str, 20))
    print("限制20字符，不带省略号：", truncate_text(test_str, 20, add_ellipsis=False))
    print("限制100字符（无需截断）：", truncate_text(test_str, 100))