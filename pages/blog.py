class Blog:
    def __init__(self, page):
        self.page = page
        self.blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')
        self.list_blog = [self.blog]

    def blog_navigation(self):
        for i in self.list_blog:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
