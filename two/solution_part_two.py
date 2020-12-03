# Advent of Code 2020
# Author: Andreas Ekström <didair>

import csv

# Define Password class
class Password:

    def __init__(self, character, pos1, pos2, password):
        self.character = character;
        self.pos1 = int(pos1) - 1;
        self.pos2 = int(pos2) - 1;
        self.password = password;

    def validate(self):
        if (self.password[self.pos1] == self.character and self.password[self.pos2] == self.character):
            return False

        if (self.password[self.pos1] == self.character or self.password[self.pos2] == self.character):
            return True

        return False

# Generate Password class instance from line data
def generatePasswordFromData(raw_password):
    line = raw_password.split(': ');
    rules = line[0].split(' ');
    character = rules[-1];
    maxNumber = rules[0].split('-')[-1];
    minNumber = rules[0].split('-')[0];
    data = line[-1];

    return Password(character, maxNumber, minNumber, data);

def day_two():
    with open("input.csv") as f:
        data = f.read().splitlines();
        correct = 0;
        incorrect = 0;

        for raw_password in data:
            password = generatePasswordFromData(raw_password);

            if (password.validate()):
                correct = correct +1;
            else:
                incorrect = incorrect +1;

        print("🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄");
        print("Correct passwords: " + str(correct));
        print("Incorrect passwords: " + str(incorrect));
        print("🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄🎄");


## 23 days until christmas 🎄🎄🎄🎄🎄
day_two();
