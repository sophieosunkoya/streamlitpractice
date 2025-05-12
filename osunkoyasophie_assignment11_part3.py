class Rectangle:
    def __init__(self,width,length,position):
        self.width=width
        self.length=length
        self.position=position
    def get_area(self):
        area=self.width*self.length
        return area
    def get_perimeter(self):
        peri=(2*self.length)+(2*self.width)
        return peri
Rect1=Rectangle(10,15,(5,3))
Rect2=Rectangle(3,5,(15,7))
def main():
    print("Rectangle #1")
    r1area=Rect1.get_area()
    print("* Coordinates:",Rect1.position)
    print("* Area:",r1area)
    r1peri=Rect1.get_perimeter()
    print("* Perimeter:",r1peri)
    print("\nRectangle #2")
    r2area=Rect2.get_area()
    print("* Coordinates:",Rect2.position)
    print("* Area:",r2area)
    r2peri=Rect2.get_perimeter()
    print("* Perimeter:",r2peri)
if __name__ == "__main__":
    main()
