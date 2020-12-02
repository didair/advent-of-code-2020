# Advent of Code 2020
# Author: Andreas Ekström <didair>

import csv

# Define Password class
class Password:

    def __init__(self, character, max, min, password):
        self.character = character;
        self.max = int(max);
        self.min = int(min);
        self.password = password;

    def validate(self):
        count = self.password.count(self.character);

        if (count >= self.min and count <= self.max):
            return True;
        else:
            return False;

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
