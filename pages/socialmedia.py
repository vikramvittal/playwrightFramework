class SocialMedia:
    def __init__(self, page):
        self.page = page

        # Header menu
        self.about = page.locator('(//a[@href="https://www.tranktechnologies.com/about"])[1]')

        # Social media links
        self.facebook = page.locator('(//a[@href="https://www.facebook.com/TrankTechnologies"])[1]')
        self.linkedin = page.locator('(//a[@href="https://in.linkedin.com/company/trank-technologies-official"])[1]')
        self.insta = page.locator('(//a[@href="https://www.instagram.com/tranktechnologies/"])[1]')
        self.pin = page.locator('(//a[@href="https://in.pinterest.com/tranktechnologies12/"])[1]')
        self.twitter = page.locator('(//a[@href="https://twitter.com/tranktechno"])[1]')
        self.youtube = page.locator('(//a[@href="https://www.youtube.com/channel/UCWu1Y-tfrXf-Utpaft830Cg"])[1]')
        self.quora = page.locator('(//a[@href="https://www.quora.com/profile/Trank-Technologies-1"])[1]')
        self.socialmedia_list = [
            self.facebook,
            self.linkedin,
            self.insta,
            self.pin,
            self.twitter,
            self.youtube,
            self.quora,
        ]

    def social_media_page_click(self):
        self.about.click()
        self.page.wait_for_load_state(state="load")
        for social_media_link in self.socialmedia_list:
            with self.page.context.expect_page() as new_page_info:
                social_media_link.click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close()
        self.page.go_back()
