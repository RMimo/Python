from pay.order import LineItem

def test_line_item_default() -> None:
    line_item = LineItem("Test", 100)
    assert line_item.total == 100
