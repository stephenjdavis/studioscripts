from simple_term_menu import TerminalMenu

chord_progressions = {
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

def main():
    """The user will first choose a progression and then a key.
    We output the associated chords in that progression for that key.
    """
    # Prompt user to choose a chord progression.
    progression_options = [] # Create our list of progressions for the menu.
    print("Choose a chord progression:")
    for progression in chord_progressions:
        progression_options.append(progression)

    progression_menu = TerminalMenu(progression_options) # Create the menu.
    choice_index = progression_menu.show()
    print("Progression: " + str(progression_options[choice_index]))
    print()

    chosen_progression = progression_options[choice_index] # Assign the value.

    # Prompt user to choose a key (We use the same process as above to create menu.)
    key_options = []
    print("Choose a key:")
    for key in chord_progressions[chosen_progression]:
        key_options.append(key)

    key_menu = TerminalMenu(key_options)
    key_index = key_menu.show()
    print("Key: " + str(key_options[key_index]))
    print()

    chosen_key = key_options[key_index]

    # Output the chords for the chosen progression and output our desired chords.
    chords = []
    for chord in chord_progressions[chosen_progression][chosen_key.upper()]:
        chords.append(chord)

    print("The " + chosen_progression + " chords in the key of " + chosen_key + " are: ")
    print(chords)

if __name__ == "__main__":
    main()
