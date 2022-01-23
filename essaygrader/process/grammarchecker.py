def grammarCheck(essay):
    import language_tool_python
    tool = language_tool_python.LanguageTool('en-US')
    x = tool.check(essay)
    return len(x)