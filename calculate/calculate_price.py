a100_hourly_price = 0.9  # Price per hour for one A100 (80GB) from digital ocean
number_of_a100s = 50    # Number of A100 GPUs rented
hours_per_year = 365 * 24  # Total number of hours in a year

def total_price_per_year():
    return a100_hourly_price * number_of_a100s * hours_per_year

print(f"Total price for renting {number_of_a100s} A100 GPUs per year: ${total_price_per_year():,.2f}")

'''
(base) ➜  inference python3 calculate_throughput.py
Avg Prompt Throughput: 6043.166084855006
Avg Generation Throughput: 269.9859559613317
Avg Running Reqs: 8.17454350161117
Avg Swapped Reqs: 0.0
Avg Pending Reqs: 0.1400375939849624
Avg GPU KV Cache Usage: 6.812150912996792
Avg CPU KV Cache Usage: 0.0
Log Entries Counted: 7448
(base) ➜  inference python3 calculate_throughput.py
Avg Prompt Throughput: 5024.472420313343
Avg Generation Throughput: 222.75999459751526
Avg Running Reqs: 5.103457590491626
Avg Swapped Reqs: 0.0
Avg Pending Reqs: 0.10480821177741761
Avg GPU KV Cache Usage: 4.295488924905446
Avg CPU KV Cache Usage: 0.0
Log Entries Counted: 3702
(base) ➜  inference python3 calculate_throughput.py
Avg Prompt Throughput: 5588.162097392647
Avg Generation Throughput: 249.22871932515284
Avg Running Reqs: 7.5329754601226995
Avg Swapped Reqs: 0.0
Avg Pending Reqs: 0.2200920245398773
Avg GPU KV Cache Usage: 6.272718558282218
Avg CPU KV Cache Usage: 0.0
Log Entries Counted: 5216
'''

hourly_cost = a100_hourly_price
avg_prompt_throughput = 5588.162097392647
avg_generation_throughput = 249.22871932515284

# hourly_cost = a100_hourly_price
# avg_prompt_throughput = 9640
# avg_generation_throughput = 555

# hourly_cost = h100_hourly_price
# avg_prompt_throughput = 20563
# avg_generation_throughput = 1183

def calculate_dollar_per_million_tokens():
    """
    Calculate the cost per 1 million tokens processed.

    Parameters:
        hourly_cost (float): Total cost per hour in dollars.
        avg_prompt_throughput (float): Average prompt throughput in tokens per second.
        avg_generation_throughput (float): Average generation throughput in tokens per second.

    Returns:
        float: Cost per 1 million tokens in dollars.
    """
    total_throughput = avg_prompt_throughput + avg_generation_throughput
    
    seconds_in_one_hour = 3600
    total_tokens_per_hour = total_throughput * seconds_in_one_hour
    
    cost_per_million_tokens = hourly_cost / (total_tokens_per_hour / 1_000_000)
    
    return cost_per_million_tokens

dollar_per_million_tokens = calculate_dollar_per_million_tokens()

print(f"Dollar per 1 million tokens: ${dollar_per_million_tokens:.6f}")
