def truncate_text(text: str, max_len: int, add_ellipsis: bool = True, preserve_word: bool = False) -> str:
    """
    文本长度截断工具。

    该函数用于将输入文本截断为指定最大字符数，并可选择是否添加省略号。
    它支持两种主要行为：
      1. add_ellipsis=True：超出长度时在末尾追加 "..."。
      2. preserve_word=True：在截断时尽量保留完整词语边界。

    参数说明：
      text: 待截断的原始文本。
      max_len: 允许的最大字符数，如果小于 0 则抛出 ValueError。
      add_ellipsis: 是否在超长文本后追加省略号，默认为 True。
      preserve_word: 是否尝试在空格边界处截断，以保留完整词语，默认为 False。

    返回值：
      截断后的文本。若原始文本长度不超过 max_len，则直接返回原文本。
      若超过 max_len 且 add_ellipsis=True，则返回带省略号的截断结果。
      若 max_len 非常短且无法完整添加 "..."，则返回截断后的部分省略号。
    """
    if max_len < 0:
        raise ValueError("max_len must be non-negative")
    if len(text) <= max_len:
        return text
    if add_ellipsis and max_len <= 3:
        return "..."[:max_len]

    cut = text[:max_len]
    if preserve_word:
        cut = cut.rstrip()
        if " " in cut and len(cut) < len(text):
            cut = cut.rsplit(" ", 1)[0]
    if add_ellipsis:
        cut = cut.rstrip() + "..."
    return cut


# 内置自测
if __name__ == "__main__":
    test_str = "人工智能文本预处理工具，包含清洗、去停用词、数字过滤、文本长度截断全套功能"
    print("=== 文本截断独立模块自测 ===")
    print("原文：", test_str)
    print("限制20字符，带省略号：", truncate_text(test_str, 20))
    print("限制20字符，不带省略号：", truncate_text(test_str, 20, add_ellipsis=False))
    print("限制20字符，保留词语边界：", truncate_text(test_str, 20, preserve_word=True))
    print("限制100字符（无需截断）：", truncate_text(test_str, 100))