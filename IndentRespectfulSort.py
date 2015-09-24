import sublime, sublime_plugin, sys

class IndentRespectfulSortCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		
		#self.view.insert(edit, 0, "Hello, World!")
		region = sublime.Region(0, self.view.size())
		#lines = self.view.lines(region)
		content = self.view.substr(sublime.Region(0, self.view.size()))
		lines = content.split("\n")
		rootNode = RootNode(lines, args.get("indent","\t"), 0, int(args.get("maxDepth", sys.maxint)) - 1 , int(args.get("onlyDepth", None)) - 1)
       
		self.view.erase(edit, region)
		self.view.insert(edit, 0, str(rootNode))

class RootNode:
    def __init__(self, content, indent, level, maxDepth, onlyDepth):
        self.content = content
        self.indent = indent
        self.level = level
        self.maxDepth = maxDepth
        self.onlyDepth = onlyDepth
        self.children = self.getChildren()
        
    def getChildren(self):
        children = []
        indices = []
        for idx, val in enumerate(self.content):
            import re
            if re.search("^\S.*", val):
                indices.append(idx)
        iterate = True
        startIdx = 0
        while iterate:
            if len(indices) > startIdx + 1:
                endIdx = indices[startIdx + 1]
                children.append(Node(str(self.content[indices[startIdx]]), self.level + 1, self.indent , list(self.content[indices[startIdx] + 1: endIdx]), self.maxDepth, self.onlyDepth))
                startIdx += 1
            elif len(indices) == startIdx + 1:
                children.append(Node(str(self.content[indices[startIdx]]), self.level + 1, self.indent , list(self.content[indices[startIdx]+ 1:]), self.maxDepth, self.onlyDepth))
                startIdx += 1
                iterate = False
            else:
                iterate = False

        return children

    def __str__ (self):
        childrenString = ""
        if (self.onlyDepth is None) or (self.onlyDepth is not None and self.level == self.onlyDepth):
            self.children.sort(key=lambda node: node.value)
        for child in self.children:
            childrenString += str(child)
        return childrenString


class Node:
    def __init__(self, value, level, indent, content, maxDepth, onlyDepth):
        self.value = value
        self.indent = indent
        self.content = content
        self.level = level
        self.maxDepth = maxDepth
        self.onlyDepth = onlyDepth
        self.children = self.getChildren()

    def getChildren(self):
        children = []
        indices = []
        for idx, val in enumerate(self.content):
            import re
            if re.search("^" + self.indent*self.level +"\S.*", val):
                indices.append(idx)
        iterate = True
        startIdx = 0
        while iterate:
            if len(indices) > startIdx + 1:
                endIdx = indices[startIdx + 1]
                children.append(Node(str(self.content[indices[startIdx]]), self.level + 1, self.indent, self.content[indices[startIdx] + 1: endIdx],self.maxDepth, self.onlyDepth))
                startIdx += 1
            elif len(indices) == startIdx + 1:
                children.append(Node(str(self.content[indices[startIdx]]), self.level + 1, self.indent, self.content[indices[startIdx] + 1:], self.maxDepth, self.onlyDepth))
                startIdx += 1
                iterate = False
            else:
                iterate = False
        return children

    def __str__(self):
        childrenString = ""
        if self.level < self.maxDepth:
            if (self.onlyDepth is None) or (self.onlyDepth is not None and self.level == self.onlyDepth):
                self.children.sort(key=lambda node: node.value)
        for child in self.children:
            childrenString += str(child)
        return self.value + "\n" + childrenString