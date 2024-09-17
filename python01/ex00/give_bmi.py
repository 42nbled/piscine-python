import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> np.ndarray:
    """ 
    Calculate BMI values from height and weight lists.

    :param height: A list of height values (floats).
    :param weight: A list of weight values (floats).
    :return: A numpy array of BMI values (floats).
    """
    height = np.array(height, dtype=float)
    weight = np.array(weight, dtype=float)

    if height.shape != weight.shape:
        raise ValueError("Height and weight lists must be of the same length.")
    if np.any(height <= 0):
        raise ValueError("Height must be greater than zero.")

    return weight / (height ** 2)

def apply_limit(bmi: np.ndarray, limit: int) -> np.ndarray:
    """
    Apply a limit to BMI values.

    :param bmi: A numpy array of BMI values (floats).
    :param limit: An integer limit value.
    :return: A numpy array of boolean values.
    """
    return bmi > limit

def main():
    """
    Main function.
    
    Test the give_bmi and apply_limit functions.
    """
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))

        limit = 26
        result = apply_limit(bmi, limit)
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()