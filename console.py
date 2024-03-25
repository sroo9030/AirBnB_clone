#!/usr/bin/python3
# models/console.py
"""Define the the console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt="(hbnb)"
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}
    @staticmethod()
    def do_quit():
        """quit"""
        return True
    @staticmethod()
    def do_EOF():
        """End Of File"""
        return True
    @staticmethod()
    def do_help():
        """help"""
        return True
    def do_create(self,line):
        """
        Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print ("** class doesn't exist **")
        else:
            new_obj = Filestorge()
            new_obj.save()
            print(new_obj.id)
    def do_show(self,line):
        """
        Prints the string representation of an instance based on
        the class name and id
        """
        argu=line.split("",1)
        ob_dic = storge.all()
        if not line:
            print("** class name missing **")
        elif argu[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(argu) == 1:
                print('** instance id missing **')
        elif f"{argu[0]}.{argu[1]}" not in obj_dic:
            print("** no instance found **")
        else:  
            print(ob_dic[argu[0]+"."+argu[1]])
    def do_destroy(self,line):
        """
        Deletes an instance based on the class name and id
        """
        argu=line.split("",1)
        ob_dic = storge.all()
        if not line:
            print("** class name missing **")
        elif argu[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(argu) ==1:
            print("** instance id missing **")
        elif f"{argu[0]}.{argu[1]}" not in ob_dic.keys():
            print("** no instance found **")
        else:
            del ob_dic[f"{argu[0]}.{argu[1]}"]
            storge.save()
    def do_all(self,line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        argu=line.split("",1)
        if argu[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj=[]
            for obj_ct in storge.all.values():
                if len(argu) > 0 and argu[0]==obj_ct.__class__.__name__:
                    obj.append(obj_ct.__str__())
                elif len(argu) == 0:
                    obj.append(obj_ct.__str__())
            print(obj)
    def do_update(self,line):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute 
        """
        argu=line.split()
        if not line:
            print("class name missing")
        elif argu[0] not in self.classes:
            print("class doesn't exist")
        elif not len(argu) < 2:
            print("instance id missing")
        elif len(argu) ==2:
            print("attribute name missing ")
        elif len(argu)==3:
            try:
                type(eval(argu[2])) != dict()
            except NameError:
                    print("** value missing **")
        if len(argu) == 4:
            obj=obj_dict[f"{argu[0]}.{argu[1]}"]
            if argu[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[argu[2]])
                obj.__dict__[argu[2]] = val_type(argu[3])
            else:
                obj.__dict__[argu[2]] = argu[3]
        elif type(eval(argu[2])) == dict:
            obj = objdict[f"{argu[0]}.{argu[1]}"]
            for key, val in eval(argu[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    val_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val_type(val)
                else:
                    obj.__dict__[key] = val
        storage.save()
    
if __name__ == "__main__":
    HBNBCommand().cmdlooelifp()
