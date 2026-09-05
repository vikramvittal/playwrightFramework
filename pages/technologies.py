class Technologies:
    def __init__(self, page):
        self.page = page
        #Header Menu
        self.technologies = page.locator('(//a[text()="Technologies"])[1]')
        
        # Technologies Main Categories
        self.ecommerce_development = page.locator('(//strong[text()="eCommerce Development"])[1]')
        self.mobile_app_development = page.locator('(//strong[text()="Mobile App Development"])[1]')
        self.artificial_intelligence = page.locator('(//strong[text()="Artificial Intelligence"])[1]')
        
        # Ecommerce Development Submenus
        self.magento_development = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.opencart_development = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.codeigniter_development = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.wordpress_development = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.big_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.shopify_development = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.cs_cart_development = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.node_js_development = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.nop_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.woo_commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.laravel_development = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.prestashop_development = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.drupal_development = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.wix_development = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.joomla_development = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.react_js_development = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.express_js_development = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.list_ecommerce=[self.magento_development,self.opencart_development,self.codeigniter_development,self.wordpress_development,self.big_commerce,self.shopify_development,self.cs_cart_development,self.node_js_development,self.nop_commerce,self.woo_commerce,self.laravel_development,self.prestashop_development,self.drupal_development,self.wix_development,self.joomla_development,self.react_js_development,self.express_js_development]
    # Mobile App Development Submenus
        self.react_native_mobile_app = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.enterprise_mobile_app = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xamarin_mobile_app = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.kotlin_mobile_app = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.flutter_mobile_app = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.ionic_app = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.swift_app = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.appointment_booking = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.list_mobile_app=[self.react_native_mobile_app,self.enterprise_mobile_app,self.xamarin_mobile_app,self.kotlin_mobile_app,self.flutter_mobile_app,self.ionic_app,self.swift_app,self.appointment_booking]

        # Artificial Intelligence
        self.list_artificial_intelligence=[self.artificial_intelligence]
        
    def ecommerce_navigation(self):
        for i in self.list_ecommerce:
            self.technologies.hover()
            self.ecommerce_development.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
            
    def mobile_app_navigation(self):
        for i in self.list_mobile_app:
            self.technologies.hover()
            self.mobile_app_development.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def artificial_intelligence_navigation(self):
        for i in self.list_artificial_intelligence:
            self.technologies.hover()
            self.artificial_intelligence.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
