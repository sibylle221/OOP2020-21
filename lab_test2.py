# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# B. Schoen-Phelan
# 11-12-2020

class Document:
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.
    """


    def __init__(self, file_name):
        self.characters = []
        self.cursor = 0
        self.filename = file_name

    def insert(self, character):
        """
        Method inserts a character at the current
        cursor position.
        Argument:
        ---------
        character : str
        the character to insert

        returns: no return
        -------
        """
        self.characters.insert(self.cursor, character)
        self.cursor += 1

    def delete(self):
        """
        Method deletes a character from the current
        cursor position.
        Arguments: none
        Returns: none
        """
        del self.characters[self.cursor]

    def save(self):
        """
        Method saves all characters in the characters list
        to a file.
        Arguments: none
        Returns: none
        """
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

        print(f"Your file {self.filename} has "
              f"been created.\nPlease check.\n")

    def forward(self, steps):
        """
        Method fowards to a particular position in
        characters [].
        Arguments:
        ----------
        steps: int
            The amount of steps the cursor should be
            pushed forward by

        Returns: none.
        """
        self.cursor += steps

    def backward(self, steps):

        """
        Method backward moves the cursor position to
        that specific location in the characters list.
        Arguments:
        ----------
        steps : int
            The amount of steps to go back

        Returns: none
        """

        try:
            if 12 > steps:
                self.cursor -= steps
            else:
                print("Value is too big")

        except ValueError:
            print("ValueError")
        except TypeError:
            print("TypeError")
        except Exception as e:
            print("Caught some other error")


@property
def get_characters(self):
    return self.__characters

@property
def get_cursor(self):
    return self.__cursor


# initialising an object and using the class
doc = Document("lab_t2.txt")
characters = 'fake mews'

for letter in characters:
    doc.insert(letter)

doc.forward(2)
doc.backward(2)
doc.delete()
doc.insert('n')
doc.save()
