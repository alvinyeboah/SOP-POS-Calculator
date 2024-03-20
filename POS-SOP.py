import tkinter as tk

def parse_expression(expression):
    # Parse the input expression into individual terms
    # For example, if the input is "A + B + C", return ['A', 'B', 'C']
    return expression.split('+')

def pos_to_sop(expression):
    # Convert product of sum (POS) expression to sum of product (SOP) expression
    # For example, if the input is ['A', 'B', 'C'], return [['A', 'B', 'C']]
    return [parse_expression(expression)]

def sop_to_pos(expression):
    # Convert sum of product (SOP) expression to product of sum (POS) expression
    # For example, if the input is [['A', 'B', 'C']], return ['A', 'B', 'C']
    return expression[0]

def evaluate_expression(expression, values):
    # Evaluate the expression using the given values for variables
    # For example, if the expression is ['A', 'B', 'C'] and values is {'A': True, 'B': False, 'C': True},
    # return the result of the expression evaluation
    result = []
    for term in expression:
        term_value = all(values[var] if var.isupper() else not values[var.upper()] for var in term)
        result.append(term_value)
    return any(result)

def calculate_pos():
    input_expression = input_entry.get()
    parsed_expression = parse_expression(input_expression)
    pos_expression = pos_to_sop(parsed_expression)
    output_text.delete("1.0", tk.END)  # Clear previous result
    output_text.insert(tk.END, "POS Expression: {}\n".format(' + '.join(['('.join(term) + ')' for term in pos_expression])))

def calculate_sop():
    input_expression = input_entry.get()
    parsed_expression = parse_expression(input_expression)
    sop_expression = sop_to_pos(parsed_expression)
    output_text.delete("1.0", tk.END)  # Clear previous result
    output_text.insert(tk.END, "SOP Expression: {}\n".format(' * '.join(sop_expression)))

# Create main window
root = tk.Tk()
root.title("Discrete Structures Calculator")

# Create input field
input_label = tk.Label(root, text="Enter expression:")
input_label.pack()
input_entry = tk.Entry(root, width=40)
input_entry.pack()

# Create buttons for POS and SOP
pos_button = tk.Button(root, text="Product of Sum", command=calculate_pos)
pos_button.pack()
sop_button = tk.Button(root, text="Sum of Product", command=calculate_sop)
sop_button.pack()

# Create output field
output_label = tk.Label(root, text="Result:")
output_label.pack()
output_text = tk.Text(root, width=40, height=5)
output_text.pack()

root.mainloop()
