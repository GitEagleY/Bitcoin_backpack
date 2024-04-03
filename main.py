import csv
import time
import sys

class Transaction:
    def __init__(self, tx_id, tx_size, tx_fee):
        self.tx_id = tx_id
        self.tx_size = tx_size
        self.tx_fee = tx_fee
        self.fee_to_size_ratio = tx_fee / tx_size

def counting_sort(transactions, exp):
 
    n = len(transactions)

    # initialize output array as 0
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = transactions[i].fee_to_size_ratio // exp

        # Extract the units place digit
        units_digit = index % 10
    
        # Increment the count of occurrences of the units place digit
        count[int(units_digit)] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1  # Start from the last transaction in the original array
    while i >= 0:  # Iterate through each transaction in reverse order
        #Calculate the index where the current transaction should be placed in the output array
        index = transactions[i].fee_to_size_ratio // exp
        
        #Determine the position in the output array using the count array
        #-1 because indexing is 0-based
        output_index = count[int(index) % 10] - 1
        
        #Place the current transaction in the output array at the determined position
        output[output_index] = transactions[i]
        
        #Update the count array to reflect the placement of the current transaction
        count[int(index) % 10] -= 1
        
        #Move to the previous transaction in the original array
        i -= 1


    for i in range(n):
        transactions[i] = output[i]

def radix_sort(transactions):
    
    # Initialize max_ratio to negative infinity
    # to ensure that any transaction's fee-to-size ratio will be greater than the initial value.
    max_ratio = float('-inf')  

    # Iterate through transactions to find the maximum fee-to-size ratio
    for tx in transactions:
        if tx.fee_to_size_ratio > max_ratio:
            max_ratio = tx.fee_to_size_ratio

    # Iterate through each significant place

    #exp = 1 is because we want to start by examining the rightmost (least significant) 
    #digit of each fee-to-size ratio.
    exp = 1
    
    #This condition ensures that we continue iterating 
    #until we've processed all significant digits of the largest fee-to-size ratio
    while max_ratio // exp > 0:
        counting_sort(transactions, exp)

        #This shifts our focus to the next significant place 
        #(e.g., from units to tens, from tens to hundreds, and so on).
        exp *= 10

    return transactions


def construct_block(transactions, block_size_limit):

    start_time = time.time()

    # sort transactions
    transactions = radix_sort(transactions)

    block_size = 0
    total_extracted_value = 0
    block_transactions = []

    for tx in transactions:
        # check for exceeding block size limit
        if block_size + tx.tx_size <= block_size_limit:
            # add transactions
            block_size += tx.tx_size
            total_extracted_value += tx.tx_fee
            block_transactions.append(tx)
        else:
            break

    
    construction_time = time.time() - start_time

    max_memory_usage = len(transactions) * (sys.getsizeof(Transaction) + sys.getsizeof(float))

    return block_transactions, len(transactions), block_size, total_extracted_value, \
           construction_time, max_memory_usage


def main():
    transactions = []

    # Open CSV file containing transactions
    with open('transactions.csv', 'r') as file:
        # Create a CSV reader
        reader = csv.reader(file)

        # Parse transaction data and create Transaction objects using a for loop, skipping the header row
        for row in reader:
            if row[0] != 'tx_id':
                tx_id, tx_size, tx_fee = map(int, row)
                transactions.append(Transaction(tx_id, tx_size, tx_fee))

    #block size limit (1 MB)
    block_size_limit = 1_000_000

    block_transactions, num_transactions, block_size, total_extracted_value, \
    construction_time, max_memory_usage = construct_block(transactions, block_size_limit)

    print("Constructed Block:")
    print(f"Amount of transactions in the block: {num_transactions}")
    print(f"Block size: {block_size}")
    print(f"Total extracted value: {total_extracted_value}")
    print(f"Construction time: {construction_time} seconds")
    print(f"Maximum memory usage: {max_memory_usage} bytes")


main()
