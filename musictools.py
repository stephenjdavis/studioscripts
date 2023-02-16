from simple_term_menu import TerminalMenu

class musictools:
    def __init__(self):
        # Define 10 pre-formatted common chord progression for each key
        self.chord_progressions = {
            "I-IV-V": {
                "C": ["C", "F", "G"], 
                "D": ["D", "G", "A"], 
                "E": ["E", "A", "B"], 
                "F": ["F", "Bb", "C"], 
                "G": ["G", "C", "D"],
                "A": ["A", "D", "E"], 
                "B": ["B", "E", "F#"]
            },
            "vi-IV-V": {
                "C": ["Am", "F", "G"], 
                "D": ["Bm", "G", "A"], 
                "E": ["C#m", "A", "B"], 
                "F": ["Dm", "Bb", "C"], 
                "G": ["Em", "C", "D"],
                "A": ["F#m", "D", "E"], 
                "B": ["G#m", "E", "F#"]
            },
            "iii-vi-ii-V": {
                "C": ["Em", "Am", "Dm", "G"], 
                "D": ["F#m", "Bm", "Em", "A"], 
                "E": ["G#m", "C#m", "F#m", "B"], 
                "F": ["Am", "Dm", "Gm", "C"], 
                "G": ["Bm", "Em", "Am", "D"],
                "A": ["C#m", "F#m", "Bm", "E"],
                "B": ["D#m", "G#m", "C#m", "F#"]
            },
            "ii-V-I": {
                "C": ["Dm", "G", "C"], 
                "D": ["Em", "A", "D"], 
                "E": ["F#m", "B", "E"], 
                "F": ["Gm", "C", "F"], 
                "G": ["Am", "D", "G"], 
                "A": ["Bm", "E", "A"], 
                "B": ["C#m", "F#", "B"]
            },
            "I-vi-IV-V": {
                "C": ["C", "Am", "F", "G"], 
                "D": ["D", "Bm", "G", "A"], 
                "E": ["E", "C#m", "A", "B"], 
                "F": ["F", "Dm", "Bb", "C"],
                "G": ["G", "Em", "C", "D"], 
                "A": ["A", "F#m", "D", "E"], 
                "B": ["B", "G#m", "E", "F#"]
            },
            "vi-IV-I-V": {
                "C": ["Am", "F", "C", "G"], 
                "D": ["Bm", "G", "D", "A"], 
                "E": ["C#m", "A", "E", "B"], 
                "F": ["Dm", "Bb", "F", "C"],
                "G": ["Em", "C", "G", "D"], 
                "A": ["F#m", "D", "A", "E"], 
                "B": ["G#m", "E", "B", "F#"]
            },
            "I-vi-iii-vi": {
                "C": ["C", "Am", "Em", "Am"], 
                "D": ["D", "Bm", "F#m", "Bm"], 
                "E": ["E", "C#m", "G#m", "C#m"], 
                "F": ["F", "Dm", "Am", "Dm"],
                "G": ["G", "Em", "Bm", "Em"], 
                "A": ["A", "F#m", "C#m", "F#m"], 
                "B": ["B", "G#m", "D#m", "G#m"]
            },
            "I-vi-vi-V": {
                "C": ["C", "Am", "Am", "G"], 
                "D": ["D", "Bm", "Bm", "A"], 
                "E": ["E", "C#m", "C#m", "B"], 
                "F": ["F", "Dm", "Dm", "C"], 
                "G": ["G", "Em", "Em", "D"], 
                "A": ["A", "F#m", "F#m", "E"], 
                "B": ["B", "G#m", "G#m", "F#"]
            },
            "I-V-vi-IV": {
                "C": ["C", "G", "Am", "F"], 
                "D": ["D", "A", "Bm", "G"], 
                "E": ["E", "B", "C#m", "A"], 
                "F": ["F", "C", "Dm", "Bb"], 
                "G": ["G", "D", "Em", "C"], 
                "A": ["A", "E", "F#m", "D"], 
                "B": ["B", "F#", "G#m", "E"]
            },
            "I-vi-iii-V": {
                "C": ["C", "Am", "Em", "G"], 
                "D": ["D", "Bm", "F#m", "A"], 
                "E": ["E", "C#m", "G#m", "B"], 
                "F": ["F", "Dm", "Am", "C"], 
                "G": ["G", "Em", "Bm", "D"], 
                "A": ["A", "F#m", "C#m", "E"], 
                "B": ["B", "G#m", "D#m", "F#"]
            }
        }

        # Define steps between intervals
        self.half_steps = {
            "I": 0,
            "II": 2, 
            "III": 4, 
            "IV": 5,
            "V": 7,
            "VI": 9, 
            "VII": 11,
            "i": 0,
            "ii": 2, 
            "iii": 4, 
            "iv": 5,
            "v": 7,
            "vi": 9, 
            "vii": 11
        }

        # Define the chromatic scale of notes
        self.chromatic_scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        
        # Define the chord types and their intervals
        self.chord_types = {
            "maj": [0, 4, 7],
            "min": [0, 3, 7],
            "aug": [0, 4, 8],
            "dim": [0, 3, 6],
            "sus2": [0, 2, 7],
            "sus4": [0, 5, 7],
            "6": [0, 4, 7, 9],
            "7": [0, 4, 7, 10],
            "9": [0, 2, 4, 7, 10],
            "11": [0, 4, 5, 7, 10],
            "13": [0, 4, 7, 9, 10, 14],
        }

                # define the major and minor scales for each key
        self.major_scales = {"C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
                        "C#": ["C#", "D#m", "E#m", "F#", "G#", "A#m", "B#dim"],
                        "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
                        "D#": ["D#", "E#m", "F##m", "G#", "A#", "B#m", "C#dim"],
                        "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
                        "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"],
                        "F#": ["F#", "G#m", "A#m", "B", "C#", "D#m", "E#dim"],
                        "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
                        "G#": ["G#", "A#m", "B#m", "C#", "D#", "E#m", "F#dim"],
                        "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
                        "A#": ["A#", "B#m", "C##m", "D#", "E#", "F#m", "G#dim"],
                        "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"]}
        self.minor_scales = {"A": ["Am", "Bdim", "C", "Dm", "Em", "F", "G"],
                        "A#": ["A#m", "B#dim", "C#", "D#m", "E#m", "F#", "G#"],
                        "B": ["Bm", "C#dim", "D", "Em", "F#m", "G", "A"],
                        "C": ["Cm", "Ddim", "Eb", "Fm", "Gm", "Ab", "Bb"],
                        "C#": ["C#m", "D#dim", "E", "F#m", "G#m", "A", "B"],
                        "D": ["Dm", "Edim", "F", "Gm", "Am", "Bb", "C"],
                        "D#": ["D#m", "E#dim", "F#", "G#m", "A#m", "B", "C#"],
                        "E": ["Em", "F#dim", "G", "Am", "Bm", "C", "D"],
                        "F": ["Fm", "Gdim", "Ab", "Bbm", "Cm", "Db", "Eb"],
                        "F#": ["F#m", "G#dim", "A", "Bm", "C#m", "D", "E"],
                        "G": ["Gm", "Adim", "Bb", "Cm", "Dm", "Eb", "F"],
                        "G#": ["G#m", "A#dim", "B", "C#m", "D#m", "E", "F#"]}

    def get_chords_for_progression(self):
        """The user will first choose a progression and then a key.
        We output the associated chords in that progression for that key.
        """
        # Prompt user to choose a chord progression.
        progression_options = [] # Create our list of progressions for the menu.
        print("Choose a chord progression:")
        for progression in self.chord_progressions:
            progression_options.append(progression)

        progression_menu = TerminalMenu(progression_options) # Create the menu.
        choice_index = progression_menu.show()
        print("Progression: " + str(progression_options[choice_index]))
        print()

        chosen_progression = progression_options[choice_index] # Assign the value.

        # Prompt user to choose a key (We use the same process as above to create menu.)
        key_options = []
        print("Choose a key:")
        for key in self.chord_progressions[chosen_progression]:
            key_options.append(key)

        key_menu = TerminalMenu(key_options)
        key_index = key_menu.show()
        print("Key: " + str(key_options[key_index]))
        print()

        chosen_key = key_options[key_index]

        # Output the chords for the chosen progression and output our desired chords.
        chords = []
        for chord in self.chord_progressions[chosen_progression][chosen_key.upper()]:
            chords.append(chord)

        print("The " + chosen_progression + " chords in the key of " + chosen_key + " are: ")
        print(chords)

    
    def create_custom_progression(self):
        """
        The user chooses a key then chooses intervals 
        for a custom progression.
        """
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
        while notes[0] != chosen_key: # Re-order the notes starting at chosen key.
            notes.append(notes.pop(0))
    
        more = True
        while more == True: # Continue adding to the progression until the user no longer wishes to continue.
            hs_options = []
            
            print("Choose an interval to add to your progression:")
            for hs in self.half_steps:
                hs_options.append(hs)
            hs_menu = TerminalMenu(hs_options)
            hs_index = hs_menu.show()
            prog = hs_options[hs_index]
            intervals.append(prog)
            
            print("Interval added is: " + str(prog))
            print()
        
            moves = self.half_steps.get(prog) # Determine how many half-steps to move up the scale.
            m = notes[moves]
            if prog == "i" or prog == "ii" or prog == "iii" or prog == "iv" or prog == "v" or prog == "vi" or prog == "vii": # Add minor notation to minor intervals.
                m = m + "m"
            progression.append(m)
    
            print("Progression: ")
            print(intervals)
            print(progression)
            
            cont = input("Would you like to add another interval?")
            if cont != "y" and cont != "Y":
                more = False


    def get_notes_in_a_chord(self):
        """
        The user selects a chord & the chords type and we output the notes contained for it
        """
        cs_options = []
        for cs in self.chromatic_scale:
            cs_options.append(cs)
        cs_menu = TerminalMenu(cs_options)
        cs_index = cs_menu.show()
        note = cs_options[cs_index]
                
        ct_options = []
        for ct in self.chord_types:
            ct_options.append(ct)
        ct_menu = TerminalMenu(ct_options)
        ct_index = ct_menu.show()
        chord_t = ct_options[ct_index]
        chord = note + chord_t
        # Parse the chord string to extract the root note and chord type
        root_note = chord[0]
        chord_type = chord[1:]
                
        # Determine the intervals for the chord type
        if chord_type not in self.chord_types:
            print(f"Invalid chord type: {chord_type}")
            return
        intervals = self.chord_types[chord_type]
                
        # Calculate the notes in the chord
        chord_notes = [self.chromatic_scale[(chromatic_scale.index(root_note) + interval) % 12] for interval in intervals]
                
        # Print the notes in the chord
        print(f"The notes in {chord} chord are: {', '.join(chord_notes)}")     

    
    def get_note_from_scale(self):
        cs_options = []
        for cs in self.chromatic_scale:
            cs_options.append(cs)
        cs_menu = TerminalMenu(cs_options)
        cs_index = cs_menu.show()
        note = cs_options[cs_index]

        return note
    
    def get_chord_type(self):
        ct_options = []
        for ct in self.chord_types:
            ct_options.append(ct)
        ct_menu = TerminalMenu(ct_options)
        ct_index = ct_menu.show()
        chord_t = ct_options[ct_index]

        return chord_t

    def main(self):
        tool_options = []
        tool_options.append("1. Get chords for common progressions with a given key")
        tool_options.append("2. Create a custom progression with a given key")
        tool_options.append("3. Get the notes in a chord")
        tool_menu = TerminalMenu(tool_options)
        tool_index = tool_menu.show()
        tool = tool_options[tool_index]
            
        if tool[0] == '1':
            self.get_chords_for_progression()
        elif tool[0] == '2':
            self.create_custom_progression()
        else: 
            self.get_notes_in_a_chord()
        

if __name__ == '__main__':
    mt = musictools()
    mt.main()
