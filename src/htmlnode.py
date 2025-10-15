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
