    ###################################################
    #  Some Common Errors                             #         
    #                                                 #  
    # File Not Found                                  #
    # with open("invalid.txt",'r') as file:           #
    #     file.read()                                 #
    #                                                 #
    #                                                 #
    # Type Error                                      #
    # var = "apple"                                   #
    # number = var + 123                              #
    #                                                 #
    # Key Error                                       #
    # a_dict = {"key":"value"}                        #
    # value = a_dict["apple"]                         #
    #                                                 #
    # Index Error                                     #
    # fruit_list = ["Apple","Banana", "Pear"]         #
    # fruit = fruit_list[4]                           #
    #                                                 #
    ###################################################    


# File Not Found
try:
    file = open("day 28/invalid.txt")
    a_dict={"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("day 28/invalid.txt",'w')
    file.write("A line is written")
except KeyError as error_message:
    print(f"the key {error_message} not found")
else:
    data = file.read()
    print(data)
finally:
    file.close()
    print("File was closed")