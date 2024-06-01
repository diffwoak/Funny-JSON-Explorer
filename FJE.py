import argparse
import json
from Icon import PokerFaceIconFactory,MyIconFactory
from Container import TreeContainer,RectangleContainer


    
# Funny JSON Explorer 类
class FunnyJsonExplorer:
    def __init__(self,style,icon):
        self.style = style
        self.icon = icon
        self.json_object = None

    def load(self,file_path):
        with open(file_path, 'r') as file:
            self.json_object = json.load(file)
    
    def show(self):
        # icon_family
        if self.icon == "poker-face":
            icon_factory = PokerFaceIconFactory()
        elif  self.icon == "myicon":
            icon_factory = MyIconFactory()
        else:
            raise ValueError("Unsupported icon family")

        icon_product = icon_factory.createIconProduct ()
        # style
        if self.style == "tree":
            container = TreeContainer(icon_product)
        elif self.style == "rectangle":
            container = RectangleContainer(icon_product)
        else:
            raise ValueError("Unsupported style")

        container.generate_leafs(self.json_object)
        container.draw()    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Funny JSON Explorer")
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', type=str, required=True, choices=['tree', 'rectangle'], help='Style of the output (tree or rectangle)')
    parser.add_argument('-i', '--icon', type=str, required=True, choices=['poker-face','myicon'], help='Icon family to use (e.g., poker-face)')

    args = parser.parse_args()


    Explorer = FunnyJsonExplorer(args.style,args.icon)
    # tree rectangle  poker-face
    # Explorer = FunnyJsonExplorer("rectangle","myicon")
    Explorer.load("test.json")
    Explorer.show()
