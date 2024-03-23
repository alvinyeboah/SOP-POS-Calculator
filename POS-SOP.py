from itertools import product

def generate_truth_table(num_vars):
    inputs = [0, 1]
    return [p for p in product(inputs, repeat=num_vars)]

def parse_output_expr(output_expr, input_vars):
    output_expr = output_expr.strip()
    if output_expr in input_vars:
        return input_vars.index(output_expr), 1  # If output is one of the input variables
    elif output_expr.startswith("!"):
        if output_expr[1:] in input_vars:
            return input_vars.index(output_expr[1:]), 0  # If output is a complement of an input variable
    else:
        terms = output_expr.split("*")
        if len(terms) == 2:  # If output is a product of two input variables
            if terms[0] in input_vars and terms[1] in input_vars:
                return input_vars.index(terms[0]), input_vars.index(terms[1])
        elif len(terms) > 2:  # If output is a complement of one or more products
            complement_terms = []
            product_terms = []
            for term in terms:
                if term.startswith("!"):
                    if term[1:] in input_vars:
                        complement_terms.append(input_vars.index(term[1:]))
                else:
                    if term in input_vars:
                        product_terms.append(input_vars.index(term))
            return complement_terms, product_terms
    return None

def evaluate_output(inputs, output_spec):
    if isinstance(output_spec, int):  # Output is one of the input variables
        return inputs[output_spec]
    elif isinstance(output_spec, tuple):  # Output is a product of two input variables
        return inputs[output_spec[0]] and inputs[output_spec[1]]
    elif isinstance(output_spec, list):  # Output is a complement of one or more products
        product_result = all(inputs[term] for term in output_spec[1])
        return not product_result

def main():
    num_vars = int(input("Enter the number of input variables: "))
    input_vars = [input("Enter the name of variable {}: ".format(i + 1)) for i in range(num_vars)]
    output_expr = input("Enter the output expression (e.g., 'x*y', '!x*y', 'x*y*z', '!x*y*z'): ")

    output_spec = parse_output_expr(output_expr, input_vars)
    if output_spec is None:
        print("Invalid output expression.")
        return

    truth_table = generate_truth_table(num_vars)

    print("\nTruth Table:")
    print("Input Variables: ", input_vars)
    print("Output Expression: ", output_expr)
    print("Output:")
    for inputs in truth_table:
        output_value = evaluate_output(inputs, output_spec)
        print(inputs, "->", output_value)

if __name__ == "__main__":
    main()
