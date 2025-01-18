""" 
--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
"""
file_path = "02/input.txt"

def wrapping_paper_needed(l, w, h):
    # Calculate the surface area of the box
    surface_area = 2 * l * w + 2 * w * h + 2 * h * l
    
    # Find the area of the smallest side
    smallest_side = min(l * w, w * h, h * l)
    
    # Add the slack to the surface area
    total_paper = surface_area + smallest_side
    
    return total_paper

def total_paper_needed(file_path):
    with open(file_path, 'r') as f:
        presents = [tuple(map(int, line.strip().split('x'))) for line in f]
    total_paper = sum(wrapping_paper_needed(l, w, h) for l, w, h in presents)
    return total_paper

# total_paper = total_paper_needed(file_path)
# print(total_paper)

# --- Part Two ---

def ribbon_needed(l, w, h):
    sorted_tuple = sorted((l,w,h))
    smallest_sides = sorted_tuple[:2]
    perimeter = sum(smallest_sides) * 2

    volume = l * w * h
    
    total_ribbon = perimeter + volume
    
    return total_ribbon

def total_ribbon_needed(file_path):
    with open(file_path, 'r') as f:
        presents = [tuple(map(int, line.strip().split('x'))) for line in f]
    total_ribbon = sum(ribbon_needed(l, w, h) for l, w, h in presents)
    return total_ribbon


total_ribbon = total_ribbon_needed(file_path)
print(total_ribbon)
