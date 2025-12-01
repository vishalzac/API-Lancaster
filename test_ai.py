from ai_service import ask_ai

def test_ai_response_structure():
    """
    This test checks if the AI response contains expected keys
    without testing the external API directly.
    """
    question = "What is data science?"
    result = ask_ai(question)

    assert isinstance(result, dict)
    assert "question" in result
    assert "answer" in result
