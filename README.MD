# Makes pinouts of headers/ breakoutboards etc

Example of pin names alongside their number

           ┌───────┐
       CS# │ 16 15 │ RES#
      D/C# │ 14 13 │ R/W#
     E/RD# │ 12 11 │ D7
        D6 │ 10  9 │ D5
        D4 │ 8   7 │ D3
        D2 │ 6   5 │ D1/DIN
    D0/CLK │ 4   3 │ NC
    VCC_IN │ 2   1 │ GND
           └───────┘

Example of where they'd go to a microcontroller for instance

           ┌───────┐
      (13) │ 16 15 │ (14)
      (27) │ 14 13 │
           │ 12 11 │
           │ 10  9 │
           │ 8   7 │
           │ 6   5 │ (23)
      (18) │ 4   3 │
     (3V3) │ 2   1 │ (GND)
           └───────┘

# Usage
Just run it in cli or via vscode and input corresponding values when prompted. YOu can skip some fields if a value isn't desired/required

# Future

- Add custom padding to inside of box
- Add custom padding to outside of box
- Clean code up majorly
