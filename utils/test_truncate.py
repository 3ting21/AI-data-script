import pytest

from utils.text_truncate import truncate_text


def test_truncate_long_text_with_ellipsis():
    text = "这是一个用于测试的超长文本内容，用于验证截断功能是否可以正确处理。"
    result = truncate_text(text, 20)
    assert result.endswith("...")
    assert len(result) <= 23


def test_negative_max_len_raises_value_error():
    with pytest.raises(ValueError):
        truncate_text("文本", -1)


def test_preserve_word_boundary():
    text = "这是 测试 文本 用于 保留 词语 边界。"
    result = truncate_text(text, 10, preserve_word=True)
    assert result.endswith("...")
    assert result == "这是 测试..."


def test_no_ellipsis_on_truncate():
    text = "测试不带省略号的截断功能"
    result = truncate_text(text, 6, add_ellipsis=False)
    assert result == "测试不带省"


def test_short_max_len_with_ellipsis():
    text = "短文本"
    result = truncate_text(text, 2)
    assert result == ".."
