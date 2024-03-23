from itertools import product

# Function to generate the truth table based on the number of input variables
def generate_truth_table(num_vars):
    inputs = [0, 1]  # Possible input values (0 and 1)
    return [p for p in product(inputs, repeat=num_vars)]  # Generate all possible combinations of inputs

# Function to convert the truth table into POS and SOP expressions
def truth_table_to_expr(truth_table, output_var, input_vars):
    pos_terms = []  # List to store terms for POS expression
    sop_terms = []  # List to store terms for SOP expression

    # Iterate through each row of the truth table
    for inputs in truth_table:
        if inputs[output_var] == 1:  # If the output is 1 for this combination
            # Create a term for SOP expression where input variable is included or excluded based on its value
            sop_terms.append("({})".format(" & ".join(["{}".format(input_vars[i] if bit else "!{}".format(input_vars[i])) for i, bit in enumerate(inputs)])))
        else:  # If the output is 0 for this combination
            # Create a term for POS expression where input variable is included or excluded based on its value
            pos_terms.append("({})".format(" | ".join(["{}".format(input_vars[i] if bit else "!{}".format(input_vars[i])) for i, bit in enumerate(inputs)])))

    # Combine all terms using AND operation for POS expression
    pos_expr = " & ".join(pos_terms)
    # Combine all terms using OR operation for SOP expression
    sop_expr = " | ".join(sop_terms)

    return pos_expr, sop_expr

# Main function to prompt user input and execute the logic
def main():
    # Ask user for the number of input variables
    num_vars = int(input("Enter the number of input variables: "))
    # Ask user for the names of input variables
    input_vars = [input("Enter the name of variable {}: ".format(i + 1)) for i in range(num_vars)]
    # Ask user for the index of the output variable (0-indexed)
    output_var = int(input("Enter the index of the output variable (0-indexed): "))

    # Generate the truth table based on user input
    truth_table = generate_truth_table(num_vars)
    # Convert the truth table into POS and SOP expressions
    pos_expr, sop_expr = truth_table_to_expr(truth_table, output_var, input_vars)

    # Print the truth table
    print("\nTruth Table:")
    print("Input Variables: ", input_vars)
    print("Output Variable: ", input_vars[output_var])
    print("Output:")
    for inputs in truth_table:
        print(inputs)

    # Print the POS and SOP expressions
    print("\nProduct of Sums (POS) Expression:", pos_expr)
    print("Sum of Products (SOP) Expression:", sop_expr)

# Execute the main function
if __name__ == "__main__":
    main()
