from numpy import random   
import numpy as np



def replace_maxmium(array, replace_value, axis):
   
    output = np.where(array == np.max(
        array, axis=1).reshape(-1, 1), 0 * array, array)
    print(output)


def main():

    # Using NumPy create random vector of size 20 having only float
    # in the range 1-20.

   
    random20 = np.random.random_sample(20) * 20 + 1
    print(random20)
    
    # Reshaping array to 4 by 5
    random20_4_5 = random20.reshape((4, 5))
    print(random20_4_5)

    # Replacing the max in each row by 0(axis=1)
    replace_maxmium(random20_4_5, 0, 1)


if __name__ == "__main__":
    main()