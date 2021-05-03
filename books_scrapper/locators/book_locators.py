class BookLocators:
    """
    Locators for an item in the HTML page

    This allows easily see what our code will be looking at
    as well as change it quickly if we notice it is now difference
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'
