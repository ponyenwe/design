import math 

#replicates and depicts the movement of a car

class Car: 

    def __init__(self, x = 0.0, y = 0.0, heading = 0.0):
    #x coordinate of the car, as a float.[1] Default: 0
    #y coordinate of the car, as a float. Default: 0
    #heading, as a float. Default: 0
        self.x = x 
        self.y = y
        self.heading = heading
        
    def turn(self, degrees):
    #assign a new value to theheading attribute 
        self.heading = (degrees + self.heading) %360
    
    def drive(self, d):
    #two parameters, self and a distance expressed as a float
        h = math.radians(self.heading) #convert the heading from degrees to radians)
        self.x += d * math.sin(h) #updating x attribute
        self.y -= d * math.cos(h) #updating y attribute
         
def sanity_check():
    car_object = Car()
    car_object.turn(90) #Turn 90 degrees
    car_object.drive(10) #Drive 10 units
    car_object.turn(30) #Turn 30 degrees
    car_object.drive(20) #Drive 20 units
    
    #Print the location and heading of your instance
    print(f"location: {car_object.x}, {car_object.y}")
    print(f"heading: {car_object.heading}")
    
if __name__ == "__main__":
   sanity_check() 
   
   
###PT.2

from argparse import ArgumentParser 
import sys

def get_winner(electors, outcomes):
    
    r_votes = 0 
    d_votes = 0
    

    for state in electors:
        if outcomes[state] == 'R':
            r_votes += electors[state]
        elif outcomes[state] == 'D':
            d_votes += electors[state]
            
    if r_votes > d_votes:
        return ('R', electors_d)
    else:
        return ('D', electors_r)

    """
    The keys in both dictionaries are state names. 
    Each state's elector count is represented as an integer value in the elector dictionary. 
    Its values are either "R" or "D" in the dictionary of possible outcomes. 
    A tuple containing the winning candidate and the total number of electoral votes 
    the candidate obtained is returned by the function after calculating the number of electoral votes each candidate received ("R" or "D").
    """

def to_dict(filename, value_type=str):
    """ Read a two-column, tab-delimited file and return the lines as
    a dictionary with data from the first column as keys and data from
    the second column as values.
    Args:
    filename (str): the file to be read.
    value_type (data type): the type of the values in the second
    column (default: str).
    Raises:
    ValueError: encountered a line with the wrong number of columns.
    Returns:
    dict: the data from the file.
    """

    lines = dict()
    with open(filename, "r", encoding="utf-8") as f:
        for n, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            values = line.split("\t")
            if len(values) != 2:
                raise ValueError("unexpected number of columns on line"
                                f" {n} of {filename}")
            lines[values[0]] = value_type(values[1])
    return lines

def read_data(elector_file, outcome_file):
    """ Read elector data and outcome data and return as dictionaries.
    Args:
        elector_file (str): path to the file of electors by state.
        outcome_file (str): path to the file of hypothetical outcomes by
            state.
Returns:
    tuple of dict, dict: the elector data and outcome data. Keys in
    each dictionary will be state names.
"""

    elector_dict = to_dict(elector_file, value_type=int)
    outcome_dict = to_dict(outcome_file)
    return elector_dict, outcome_dict


def parse_args(arglist):
    """ Parse command-line arguments.
    Args:
    arglist (list of str): list of arguments from the command line.
    Returns:
    namespace: the parsed arguments, as returned by
    argparse.ArgumentParser.parse_args().
    """
    parser = ArgumentParser()
    parser.add_argument("elector_file", help="file of electors by state")
    parser.add_argument("outcome_file", help="file of outcomes by state")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    elector_dict, outcome_dict = read_data(args.elector_file, args.outcome_file)
    candidate, votes = get_winner(elector_dict, outcome_dict)
    print(f"{candidate} would win with {votes} electoral votes.")
