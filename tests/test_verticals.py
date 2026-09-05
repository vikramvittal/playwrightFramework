# pyright: reportMissingImports=false
import pytest
from pages.verticals import Verticals

@pytest.mark.smoke
def test_trading(page):
    verticals = Verticals(page)
    verticals.trading_navigation()
    verticals.retail_ecommerce_navigation()
    verticals.healthcare_navigation()
    verticals.fintech_navigation()
    verticals.custom_app_navigation()
 