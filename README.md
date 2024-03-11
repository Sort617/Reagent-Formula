# Reagent Validator README

## Description
This tool validates reagent formulas based on specific material selection rules. It ensures that the selected materials for a reagent conform to the defined constraints.

## Function
`isValid(formula)`: Checks if the formula array is valid.

- **Parameters**: `formula` - A list of integers representing materials.
- **Returns**: `True` if the formula is valid, `False` otherwise.

## Rules
1. Materials 5 and 6 must be selected together.
2. Materials 1 and 2 cannot be selected together.
3. Materials 3 and 4 cannot be selected together.
4. At least one of materials 7 or 8 must be selected.

## Usage Example
```python
isValid([1,3,7])  # Returns True
isValid([7,1,2,3])  # Returns False
```

## Testing
Run the provided test cases to ensure the function works as expected. Use the `basic_tests` function to execute a series of assertions checking various formula configurations.
