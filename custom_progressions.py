from simple_term_menu import TerminalMenu

half_steps = {
    "I": 0,
    "II": 2, 
    "III": 4, 
    "IV": 5,
    "V": 7,
    "VI": 9, 
    "VII": 11,
    "ii": 2, 
    "iii": 4, 
    "vi": 9, 
    "vii": 11
}

def main():
    # Prompt user to choose a key.
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    progression = []
    intervals = []
    
    print("Choose a key:")
    notes_menu = TerminalMenu(notes) # Create the menu.
    notes_index = notes_menu.show()
    
    print("Key: " + str(notes[notes_index]))
    print()
    
    chosen_key = notes[notes_index] # Assign the value.
    index = 0;
    while notes[index] != chosen_key: # Re-order the notes starting at chosen key.
        notes.append(notes.pop(0))

    more = True
    while more == True: # Continue adding to the progression until the user no longer wishes to continue.
        hs_options = []
        
        print("Choose an interval to add to your progression:")
        for hs in half_steps:
            hs_options.append(hs)
        hs_menu = TerminalMenu(hs_options)
        hs_index = hs_menu.show()
        prog = hs_options[hs_index]
        intervals.append(prog)
        
        print("Interval added is: " + str(prog))
        print()
    
        moves = half_steps.get(prog) # Determine how many half-steps to move up the scale.
        m = notes[moves]
        if prog == "ii" or prog == "iii" or prog == "vi" or prog == "vii": # Add minor notation to minor intervals.
            m = m + "m"
        progression.append(m)

        print("Progression: ")
        print(intervals)
        print(progression)
        
        cont = input("Would you like to add another interval?")
        if cont != "y" and cont != "Y":
            more = False

if __name__ == "__main__":
    main()
