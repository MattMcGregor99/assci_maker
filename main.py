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
                string += " " + str(col) if col < 10 else "" + str(col)
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
    header = (" " * offset + "┌" + "─" * length + "┐")
    text = (string)
    footer = (" " * offset + "└" + "─" * length + "┘")


    
    if title:
        original_title = title
        #center the title based on the length of the longest row
        title = title.center(len(header) + offset)
        #underline the title
        num = title.find(original_title)#get how much white space is on the left of the title
        print(num)
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
    print(csv_data)        
    #make safe gaurd if number of commas is fgreater thebn length then remove extra ones
    # if csv_data.count(",") > length:
    #     csv_data = csv_data[:length]   
    #     #if lenght less than length then add commas to the end
    # if csv_data.count(",") < length:
    #     csv_data += "," * (length - csv_data.count(","))
    #     #      
    #return csv_data[:-1]
    return csv_data


user_input = False
if user_input:    
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns (1 or 2): "))
    order = input("Enter the order ('down', 'zig zag', 'snake'): ")
else:
    rows = 9
    columns = 2
    order = "zig zag"
    csv_data = "GND,VCC_IN,NC,D0/CLK,D1/DIN,D2,D3,D4,D5,D6,D7,E/RD#,R/W#,D/C#,RES#,CS#"

arduino_data = {
    1: "GND",
    2: "3V3",
    4: "18",
    5: "23",
    14: "27",
    15: "14",
    16: "13"
}
out = make_csv_data(arduino_data, rows * columns)

matrix = generate_matrix(rows, columns, order, True, True)
global_padding = 10
print_matrix(matrix, csv_data, global_padding=global_padding, title="Pinfghfhout", title_position="top")
print_matrix(matrix, out, str_before="(", str_after=")", global_padding=global_padding)

cool = r'''

  _  _     _ _                      _    _ 
 | || |___| | |___  __ __ _____ _ _| |__| |
 | __ / -_) | / _ \ \ V  V / _ \ '_| / _` |
 |_||_\___|_|_\___/  \_/\_/\___/_| |_\__,_|
                                           

'''
print(cool)
#https://patorjk.com/software/taag/#p=display&c=c&f=Small&t=Hello%20World
