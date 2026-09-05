from conftest import page


class Verticals:
    def __init__(self, page):
        self.page = page
        #Headers
        self.verticals = page.locator('(//a[text()="Verticals"])[1]')

        #Verticals Main Categories
        self.trading = page.locator('(//strong[text()="Trading"])[1]')
        self.retail_ecommerce = page.locator('(//strong[text()="Retail and Ecommerce"])[1]')
        self.healthcare = page.locator('(//strong[text()="Healthcare"])[1]')
        self.fintech = page.locator('(//strong[text()="Fintech"])[1]')
        self.custom_app = page.locator('(//strong[text()="Custom App"])[1]')

        # Trading Submenus
        self.stock_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.algo_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.paper_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.custom_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.cfd_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.web_portal_trading = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
        self.trading_app_massachusetts = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        
        self.list_trading=[self.stock_trading,self.algo_trading,self.paper_trading,self.custom_trading,self.cfd_trading,self.web_portal_trading,self.trading_app_massachusetts]

        # Retail and Ecommerce Submenus
        self.ecommerce_website_development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.ecommerce_app_development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        
        self.list_retail_ecommerce=[self.ecommerce_website_development,self.ecommerce_app_development]
        
        # Healthcare Submenus
        self.diet_nutritions = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.health_tracking_app = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        
        self.list_healthcare=[self.diet_nutritions,self.health_tracking_app]
        
        # Fintech Submenus
        self.pos_software_development = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        
        self.list_fintech=[self.pos_software_development,self.crypto]
        
        # Custom App Submenus
        self.desktop_app_development = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.crm_development = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.hrm_development = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.erp_app_development = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.travel = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.e_learning = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.dating_app_development = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.real_estate = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.crm_development_usa = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')

        self.list_custom_app=[self.desktop_app_development,self.crm_development,self.hrm_development,self.erp_app_development,self.travel,self.e_learning,self.dating_app_development,self.real_estate,self.crm_development_usa]
    
    def trading_navigation(self):
        for i in self.list_trading:
            self.verticals.hover()
            self.trading.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            
    def retail_ecommerce_navigation(self):
        for i in self.list_retail_ecommerce:
            self.verticals.hover()
            self.retail_ecommerce.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            
    def healthcare_navigation(self):
        for i in self.list_healthcare:
            self.verticals.hover()
            self.healthcare.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            
    def fintech_navigation(self):
        for i in self.list_fintech:
            self.verticals.hover()
            self.fintech.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            
    def custom_app_navigation(self):
        for i in self.list_custom_app:
            self.verticals.hover()
            self.custom_app.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
