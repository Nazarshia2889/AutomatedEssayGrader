def grammarCheck(essay):
    # import language_tool_python
    # tool = language_tool_python.LanguageTool('en-US')
    # x = tool.check(essay)
    # return len(x)
    import grammar_check
    tool = grammar_check.LanguageTool('en-GB')
    matches = tool.check(essay)
    return len(matches)