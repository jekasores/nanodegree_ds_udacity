class Shirt:
    """The Shirt class represents an article of a clothing store"""
    
    #Attributes definition
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        """Method for initializing a Shirt object

        Args: 
            color (str)
            size (str)
            style (str)
            price (float)

        Attributes:
            color (str): color of a shirt object
            size (str): waist size of a shirt object
            style (str): style of a shirt object
            price (float): price of a shirt object
        """
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    
    #Methods definition
    def change_price(self, new_price):
        """The change_price method changes the price attribute of a shirt object

        Args: 
            new_price (float): the new price of the shirt object

        Returns: None

        """
        self.price = new_price
        
    def discount(self, discount):
        """The discount method gives the price with discount of a shirt object

        Args: 
            discount (float): discount percentage of the shirt object

        Returns: New price with the discount

        """
        return self.price * (1-discount)