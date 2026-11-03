import pytest

from prompts.prompt_manager import build_summary_prompt


def test_valid_input():
    result = build_summary_prompt("Python is a programming language.")
    assert result == "Summarize the following text:\nPython is a programming language."

def test_invalid_input():
    with pytest.raises(TypeError, match="document_text must be a string"):
        build_summary_prompt(12345)

def test_empty_input():
    with pytest.raises(ValueError, match="document_text cannot be empty"):
        build_summary_prompt("")
    
def test_whitespace_only_input():
    with pytest.raises(ValueError, match="document_text cannot be empty"):
        build_summary_prompt("          ")
