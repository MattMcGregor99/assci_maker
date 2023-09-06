import requests
import bs4 

def generate_matrix(rows, columns, order, flip_row=False, flip_column=False):
    #order
    #down
    # 1 6
    # 2 5
    # 3 4

    #zig zag
    # 1 2
    # 3 4
    # 5 6

    #snake
    # 1 2
    # 4 3
    # 5 6

    if columns != 1 and columns != 2:
        print("Invalid number of columns. Please choose 1 or 2.")
        return

    if order == "down":
        matrix = [[0] * columns for _ in range(rows)]
        num = 1
        for j in range(columns):
            if j % 2 == 0:
                for i in range(rows):
                    matrix[i][j] = num
                    num += 1
            else:
                for i in range(rows - 1, -1, -1):
                    matrix[i][j] = num
                    num += 1

    elif order == "zig zag":
        matrix = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    elif order == "snake":
        matrix = [[0] * columns for _ in range(rows)]
        num = 1
        for i in range(rows):
            if i % 2 == 0:
                for j in range(columns):
                    matrix[i][j] = num
                    num += 1
            else:
                for j in range(columns - 1, -1, -1):
                    matrix[i][j] = num
                    num += 1
    else:
        print("Invalid order. Please choose from 'down left up right', 'zig zag left to right', or 'snake left to right'.")
        return

    if flip_row:
        matrix.reverse()
    if flip_column:
        for row in matrix:
            row.reverse()

    return matrix

def print_matrix(matrix, csv_data=None, arduino_data=None, str_before="", str_after="", global_padding=0, title="", title_position="top"):
#add csv_data to each bit of text add correspiodning padding to make it look nice so its like A | 1  2 | B\nC | 3  4 | D\n for eample
    longest = 0
    if csv_data:
        #get tet between start and frist comma etc etc
        #split csv_data into a list of strings
        csv_data = csv_data.split(",")
        #add str_before and str_after to each string in the list if string not empty
        csv_data = [str_before + x + str_after if x else "" for x in csv_data]
        #get the length of the longest string in the list
        longest = len(max(csv_data, key=len))
        #add 2 to the length of the longest string for the padding
        longest += 2

        if longest < global_padding:
            longest = global_padding
        #add the padding to each string in the list
        csv_data = [x.rjust(longest) for x in csv_data]

    #print first column of matrix
    max_left = 0
    max_right = 0
    columns = 1
    for row in matrix:
        if len(row) == 1:
            max_left = max(max_left, row[0])
        else:
            max_left = max(max_left, row[0])
            max_right = max(max_right, row[-1])
            columns = 2
    
    print(max_left)
    print(max_right)

   
    string = ""
    for row in matrix:
        #if size of column is 1 then do this otherwise do this
        if len(row) == 1:
            string += "│ "
        

        for col in row:
            # if column cooun tis 1 do this, else do this
            #text_to_add  = csv_data[col-1]
            try:
                text_to_add  = csv_data[col-1]
            except:
                text_to_add = ""
            #text_to_add  = csv_data[col-1]
            if len(row) > 1 and col == row[0]:
                string += f"{text_to_add} │ "


            if col == row[-1]:
                #string += " " + str(col)if col < 10 else "" + str(col)
                #if max_left < 10 dont add padding to the left 
                if columns == 1:
                    if max_left >= 10 and col < 10:
                        string += " " + str(col)if col < 10 else "" + str(col)
                    else:
                        string += str(col)
                else:
                    if max_right >= 10 and col < 10:
                        string += " " + str(col)if col < 10 else "" + str(col)
                    else:
                        string += str(col)
                #string += " " + str(col) if col < 10 else "" + str(col)
            else:
                #if the column is the first column 
                if col == row[0]: 
                    string += str(col) + "  " if col < 10 else str(col) + " "
                else:
                    string += " " + str(col)if col < 10 else "" + str(col)
        #remove the padding from the text_to_add and add it to the end of the text_to_add
        
                    
        string += f" │ {text_to_add.strip().ljust(longest)}"
        #if not last row add a new line
        if row != matrix[-1]:
            string += "\n"

    #offset the header and footer by size of the longest row up to │
    #if columns == 1: then do something else do something else
    if len(matrix[0]) == 1:
        offset = 0
    else:
        offset = longest + 1
    #find the length of the longest row and add 2 for the borders 
    length = len(matrix[0]) * 3 + 1  
    if max_left < 10 and max_right < 10:
        length -= 1
    header = (" " * offset + "┌" + "─" * length + "┐")
    text = (string)
    footer = (" " * offset + "└" + "─" * length + "┘")


    
    if title:
        original_title = title
        #center the title based on the length of the longest row
        title = title.center(len(header) + offset)
        #underline the title
        num = title.find(original_title)#get how much white space is on the left of the title
        #print(num)
        title += "\n"+ " "*num + "¯" * len(original_title)

        if title_position == "top":
            print(title)
            print(header)
            print(text)
            print(footer)
        elif title_position == "bottom":
            print(header)
            print(text)
            print(footer)
            print(title)
    else:
        print(header)
        print(text)
        print(footer)

def make_csv_data(data, length):
    csv_data = ""
    for i in range(1, length + 1):
        if i in data:
            csv_data += data[i] + ","
        else:
            csv_data += ","
    return csv_data

def get_user_input():
#while rows <1 or not valid
    while True:
        try:
            rows = int(input("Enter the number of rows: "))
            if rows > 0:
                break
            else:
                print("Please enter a valid number")
        except:
            print("Please enter a valid number")
    #while columns <1 and > 2 or not valid
    while True:
        try:
            columns = int(input("Enter the number of columns (1 or 2): "))
            if columns == 1 or columns == 2:
                break
            else:
                print("Please enter a number between 1 and 2")
        except:
            print("Please enter a valid number")
    #valid order = down, zig zag, snake
    if columns == 1:
        order = "down"
    else:
        while True:
            order = input("Enter the order ('down', 'zig zag', 'snake'): ").lower()
            if order == "down" or order == "zig zag" or order == "snake":
                break
            elif order == "d" or order == "z" or order == "s":
                if order == "d":
                    order = "down"
                elif order == "z":
                    order = "zig zag"
                elif order == "s":
                    order = "snake"
                break
            elif order == "":
                order = "down"
                break
            else:
                print("Please enter a valid order")
    #valid flip row = True, False
    while True:
        flip_row = input("Flip rows? (True, False, y, n): ").lower()
        if flip_row == "true" or flip_row == "false":
            flip_row = True if flip_row == "True" else False
            break
        elif flip_row == "y" or flip_row == "n":
            flip_row = True if flip_row == "y" else False
            break
        elif flip_row == "t" or flip_row == "f":
            flip_row = True if flip_row == "t" else False
            break
        elif flip_row == "":
            flip_row = False
            break
        else:
            print("Please enter a valid option")
    #valid flip column = True, False
    if columns == 1:
        flip_column = False
    else:
        while True:
            flip_column = input("Flip columns? (True, False, y, n): ").lower()
            if flip_column == "true" or flip_column == "false":
                flip_column = True if flip_column == "True" else False
                break
            elif flip_column == "y" or flip_column == "n":
                flip_column = True if flip_column == "y" else False
                break
            elif flip_column == "t" or flip_column == "f":
                flip_column = True if flip_column == "t" else False
                break
            elif flip_column == "":
                flip_column = False
                break
            else:
                print("Please enter a valid option")

    #ask if user wants to add csv data
    while True:
        csv = input("Do you want to add csv data? (y, n): ").lower()
        if csv == "true" or csv == "false":
            csv = True if csv == "True" else False
            break
        elif csv == "y" or csv == "n":
            csv = True if csv == "y" else False
            break
        elif csv == "t" or csv == "f":
            csv = True if csv == "t" else False
            break
        elif csv == "":
            csv = False
            break
        else:
            print("Please enter a valid option")
    csv_data = ""
    #get csv data one by one
    for i in range(1, rows * columns + 1):
        if csv:
            csv_data += input(f"String for pin {i}: ") + ","
        else:
            csv_data += ","

    #get title
    title = input("Enter the title: ")
    
    #get title position
    if title:
        while True:
            title_position = input("Enter the title position ('top', 'bottom'): ").lower()
            if title_position == "top" or title_position == "bottom":
                break
            elif title_position == "t" or title_position == "b":
                title_position = "top" if title_position == "t" else "bottom"
                break
            elif title_position == "":
                title_position = "top"
                break
            else:
                print("Please enter a valid option")
    else:
        title_position = "top"

    #get global padding
    while True:
        try:
            global_padding = (input("Enter the global padding: "))
            if global_padding == "":
                global_padding = 0
                break
            global_padding = int(global_padding)
            if global_padding >= 0:
                break
            else:
                print("Please enter a valid number")
        except:
            print("Please enter a valid number")

    return rows, columns, order, flip_row, flip_column, csv_data, title, title_position, global_padding

def main():
    rows, columns, order, flip_row, flip_column, csv_data, title, title_position, global_padding = get_user_input()
    

    matrix = generate_matrix(rows, columns, order, flip_row, flip_column)
    print_matrix(matrix, csv_data, global_padding=global_padding, title=title, title_position=title_position)


##__if run run main
if __name__ == "__main__":
    main()
