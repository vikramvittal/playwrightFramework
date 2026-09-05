# pyright: reportMissingImports=false
import pytest
from pages.technologies import Technologies

@pytest.mark.smoke
def test_technologies(page):
    technologies = Technologies(page)
    technologies.ecommerce_navigation()
    technologies.mobile_app_navigation()
    technologies.artificial_intelligence_navigation()
