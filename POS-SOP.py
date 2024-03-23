from itertools import product

def generate_truth_table(num_vars):
    inputs = [0, 1]
    return [p for p in product(inputs, repeat=num_vars)]

def truth_table_to_expr(truth_table, output_var, input_vars):
    pos_terms = []
    sop_terms = []

    for inputs in truth_table:
        if inputs[output_var] == 1:
            sop_terms.append("({})".format(" & ".join(["{}".format(input_vars[i] if bit else "!{}".format(input_vars[i])) for i, bit in enumerate(inputs)])))
        else:
            pos_terms.append("({})".format(" | ".join(["{}".format(input_vars[i] if bit else "!{}".format(input_vars[i])) for i, bit in enumerate(inputs)])))

    pos_expr = " & ".join(pos_terms)
    sop_expr = " | ".join(sop_terms)

    return pos_expr, sop_expr

def main():
    num_vars = int(input("Enter the number of input variables: "))
    input_vars = [input("Enter the name of variable {}: ".format(i + 1)) for i in range(num_vars)]
    output_value = input("Enter the value of F({}): ".format(', '.join(input_vars)))

    truth_table = generate_truth_table(num_vars)
    # Determine the output variable index based on user input
    output_var = None
    for i, var in enumerate(input_vars):
        if var == output_value:
            output_var = i
            break
    if output_var is None:
        print("Output variable not found!")
        return

    pos_expr, sop_expr = truth_table_to_expr(truth_table, output_var, input_vars)

    print("\nTruth Table:")
    print("Input Variables: ", input_vars)
    print("Output Variable: ", input_vars[output_var])
    print("Output:")
    for inputs in truth_table:
        print(inputs)

    print("\nProduct of Sums (POS) Expression:", pos_expr)
    print("Sum of Products (SOP) Expression:", sop_expr)

if __name__ == "__main__":
    main()
