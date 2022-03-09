# python3
# file_system.py - Data structures and algorithms for a basic in memory file system.


import unittest


class Folder:
    def __init__(self, parent, name):
        self.parent_dir = parent
        self.name = name
        self.subfolders = {}
        self.files = []


class FileSystem:
    def __init__(self):
        self.root = None
        self.curr_dir = None
        self.path = []

    def is_empty(self):
        return self.root == None

    def add_new_folder(self, name="New Folder"):
        if self.is_empty() == True:
            self.root = new_folder = Folder(self.curr_dir, name)
            self.curr_dir = self.root
            self.path.append(self.curr_dir.name)
        else:
            new_folder = Folder(self.curr_dir, name)
            if new_folder.name not in self.curr_dir.subfolders:
                self.curr_dir.subfolders[new_folder.name] = new_folder
            else:
                raise Exception("Can not have two folder with the same name in the same directory.")
        return new_folder

    def open_folder(self, name):
        if self.is_empty() == False:
            if name == self.curr_dir.name:
                self.curr_dir = self.curr_dir
            elif name in self.curr_dir.subfolders:
                folder = self.curr_dir.subfolders[name]
                self.curr_dir = folder
                self.path.append(self.curr_dir.name)
            else:
                return print(f"No folder named {name} in {self.curr_dir.name}.")
        else:
            return print("File System empty.")

    def list_subfolders(self):
        if self.is_empty() == False:
            # if len(self.curr_dir.subfolders) != 0:
            for folder_name in self.curr_dir.subfolders.keys():
                print(folder_name)
        else:
            return print("File System empty.")

        
    def display_path(self):
        if self.is_empty() == False:
            path = '\\'.join(self.path)
            return print(path)
        else:
            return print("File System empty.")

    def back_to_parent(self):
        """
        Moves up one level and pops off the sub directory from the path.
        """
        if self.is_empty() == False:
            if self.curr_dir.parent_dir == None:
                return print(f'No parent directory. {self.curr_dir.name} is the root directory.')
            self.curr_dir = self.curr_dir.parent_dir
            self.path.pop()
            return self.curr_dir
        else:
            return print("File System empty.")



# TODO: Perform some unittests to see if the values returned are the ones expected.


def gen_file_system():
    
    file_system = FileSystem()
    '''
    print(file_system.is_empty())
    file_system.display_path()
    file_system.list_subfolders()
    file_system.back_to_parent()
    '''

    for x in range(0, 11):
        if x == 0:
            folder = 'C:'
        else:
            folder = f"Folder_{x}"
        file_system.add_new_folder(folder)

    '''
    file_system.open_folder('C:')
    file_system.list_subfolders()
    file_system.back_to_parent()
    file_system.open_folder('Folder_1')
    file_system.list_subfolders()
    file_system.back_to_parent()
    '''

    file_system.open_folder('Folder_1')

    for x in range(1, 11):
        folder = f"Folder_1_Subfolder_{x}"
        file_system.add_new_folder(folder)

    file_system.list_subfolders()
    file_system.open_folder('Folder_1_Subfolder_5')

    for x in range(1, 11):
        folder = f"Folder_1_Subfolder_5_Subsubfolder_{x}"
        file_system.add_new_folder(folder)

    file_system.list_subfolders()
    file_system.open_folder('Folder_1_Subfolder_5_Subsubfolder_7')
    file_system.display_path()

    return file_system


if __name__ == "__main__":
    gen_file_system()

    
