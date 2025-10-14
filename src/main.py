from textnode import TextNode, TextType

def main():
    dummy = TextNode("- Yo", TextType.LINK, "https://boot.dev")
    print(dummy)

main()