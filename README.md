# Backpack with Bitcoin transactions

## How to Run

### Prerequisites

- Python installed on your system

### Steps

1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Place your transaction data in a CSV file named `transactions.csv`.
4. Open a terminal or command prompt.
5. Run the following command:

   python main.py

## Algorithm Used

The algorithm used for sorting transactions is radix sort.
Radix sort is a non-comparative sorting algorithm that sorts numbers by processing individual digits.
It is particularly efficient for sorting transactions based on their fee-to-size ratio, as it can handle large datasets effectively.

For more information on radix sort, look in [here](https://www.geeksforgeeks.org/radix-sort/) and [here](https://www.programiz.com/dsa/radix-sort) .

## Why Radix Sort

Radix sort is chosen for its efficiency in sorting numbers with multiple digits and its linear time complexity, making it suitable for large datasets.
It is particularly well-suited for sorting transactions based on their fee-to-size ratio, which often involves handling large numbers with varying numbers of digits.

## Alternatives Considered

Other sorting algorithms like quicksort, mergesort, or heapsort were considered as alternatives.
However, radix sort was preferred due to its efficiency and suitability for sorting transactions based on their fee-to-size ratio.

## Efficiency

- Time Complexity: O(n\*k), where n is the number of transactions and k is the maximum number of digits in the fee-to-size ratio. Since k is typically a small constant, the time complexity can be considered linear, making radix sort efficient for large datasets.
- Space Complexity: O(n), where n is the number of transactions. Radix sort's space complexity is efficient in terms of memory usage.

## Time

~4.5 hours spent on this task
