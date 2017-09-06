#!/usr/bin/env python3

from html.parser import HTMLParser


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    # function to handle the processing of HTML comments
    def handle_comment(self, data):
        print("Encountered comment:", data)
        pos = self.getpos()
        print("At line: ", pos[0], " position ", pos[1])


def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()

    # open the sample HTML file and read it
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()  # read the entire file
        parser.feed(contents)


if __name__ == "__main__":
    main();
