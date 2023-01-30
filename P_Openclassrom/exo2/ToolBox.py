class ToolBox:
    def __init__(self, tool):
        self.tool = [tool]

    def add(self, tool):
        tools = self.tool.append(tool)
        return tools
    def remove(self, tool):
        tools = self.tool.index([tool])
        del tools
        return tools