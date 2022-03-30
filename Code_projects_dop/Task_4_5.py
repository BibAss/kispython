class HTML:
    res = ""

    def __init__(self):
        pass

    def body(self):
        with Tag("b"):
            return Tag

    def div(self):
        with Tag("d"):
            return Tag

    def p(self, a):
        self.res += "<p>" + a + "</p>"


class Tag:
    tag = ""
    res = ""

    def __init__(self, tag):
        self.tag = tag

    def __enter__(self):
        if self.tag == "b":
            print("<body>\n")
        elif self.tag == "d":
            print("<div>\n")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.tag == "b":
            print("</body>\n")
        elif self.tag == "d":
            print("</div>\n")


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('p')
         #   html.p('g')
      #  with html.div():
         #   html.p('t')
# print(html.get_code())
