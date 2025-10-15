class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag      = tag
        self.value    = value
        self.children = children
        self.props    = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    
    def props_to_html(self):
        if self.props is not None:
            html = ""
            for key, value in self.props.items():
                html += " " + key + "=\"" + value + "\""

            return html
        else:
            return ""
    
    def __repr__(self):
        return f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)
        self.tag      = tag
        self.value    = value
        self.children = None
        self.props    = props

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children, props)
        self.tag      = tag
        self.children = children
        self.props    = props

    def to_html(self):
        if self.tag == None:
            raise ValueError("Node must have a tag")
        if self.children == None:
            raise ValueError("Node must have children")
        output = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            output += child.to_html()
        output += f"</{self.tag}>"

        return output
