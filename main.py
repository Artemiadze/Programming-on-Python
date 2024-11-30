class Point2D:
    """
    A point in 2D space
    :param x: x coordinate
    :param y: y coordinate
    """

    def __init__(self, x: int, y: int) -> None:
        # Создаём атрибуты и присваиваем им переданные значения координат
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point2D({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"A 2D point with coordinates ({self.x}, {self.y})"

    def __add__(self, other: Point2D) -> Point2D:
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point2D) -> Point2D:
        return Point2D(self.x - other.x, self.y - other.y)


print(Point2D(3, 5) + Point2D(4, 7))
print(Point2D(3, 5) - Point2D(4, 7))