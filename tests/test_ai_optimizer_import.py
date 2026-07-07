def test_ai_optimizer_imports_without_openai_installed():
    import tools.ai_optimizer as optimizer
    assert optimizer.ROOT.name
