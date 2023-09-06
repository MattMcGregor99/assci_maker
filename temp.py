
cool = r'''

  _  _     _ _                      _    _ 
 | || |___| | |___  __ __ _____ _ _| |__| |
 | __ / -_) | / _ \ \ V  V / _ \ '_| / _` |
 |_||_\___|_|_\___/  \_/\_/\___/_| |_\__,_|
                                           

'''
print(cool)
#https://patorjk.com/software/taag/#p=display&c=c&f=Small&t=Hello%20World



#pinout 2
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
print_matrix(matrix, out, str_before="(", str_after=")", global_padding=global_padding)


#old ersion
def make_csv_data(data, length):
    csv_data = ""
    for i in range(1, length + 1):
        if i in data:
            csv_data += data[i] + ","
        else:
            csv_data += ","
    #print(csv_data)        
    #make safe gaurd if number of commas is fgreater thebn length then remove extra ones
    # if csv_data.count(",") > length:
    #     csv_data = csv_data[:length]   
    #     #if lenght less than length then add commas to the end
    # if csv_data.count(",") < length:
    #     csv_data += "," * (length - csv_data.count(","))
    #     #      
    #return csv_data[:-1]
    return csv_data


# else:
#     rows = 8
#     columns = 2
#     order = "zig zag"
#     csv_data = "GND,VCC_IN,NC,D0/CLK,D1/DIN,D2,D3,D4,D5,D6,D7,E/RD#,R/W#,D/C#,RES#,CS#"
#     flip_column = True
#     flip_row = False

#pinout 1
#global_padding = 10