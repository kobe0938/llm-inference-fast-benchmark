import re

'''cat lunaris-79ddc8b959-hgkc2_vllm-container.log | grep Avg'''

def parse_log_file(file_path):
    total_prompt_throughput = 0
    total_generation_throughput = 0
    total_running_reqs = 0
    total_swapped_reqs = 0
    total_pending_reqs = 0
    total_gpu_kv_cache_usage = 0
    total_cpu_kv_cache_usage = 0
    count = 0

    pattern = re.compile(
        r"Avg prompt throughput: ([\d.]+) tokens/s, "
        r"Avg generation throughput: ([\d.]+) tokens/s, "
        r"Running: (\d+) reqs, "
        r"Swapped: (\d+) reqs, "
        r"Pending: (\d+) reqs, "
        r"GPU KV cache usage: ([\d.]+)%, "
        r"CPU KV cache usage: ([\d.]+)%."
    )

    with open(file_path, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                total_prompt_throughput += float(match.group(1))
                total_generation_throughput += float(match.group(2))
                total_running_reqs += int(match.group(3))
                total_swapped_reqs += int(match.group(4))
                total_pending_reqs += int(match.group(5))
                total_gpu_kv_cache_usage += float(match.group(6))
                total_cpu_kv_cache_usage += float(match.group(7))
                count += 1

    avg_prompt_throughput = total_prompt_throughput / count if count else 0
    avg_generation_throughput = total_generation_throughput / count if count else 0
    avg_running_reqs = total_running_reqs / count if count else 0
    avg_swapped_reqs = total_swapped_reqs / count if count else 0
    avg_pending_reqs = total_pending_reqs / count if count else 0
    avg_gpu_kv_cache_usage = total_gpu_kv_cache_usage / count if count else 0
    avg_cpu_kv_cache_usage = total_cpu_kv_cache_usage / count if count else 0

   
    return {
        "Avg Prompt Throughput": avg_prompt_throughput,
        "Avg Generation Throughput": avg_generation_throughput,
        "Avg Running Reqs": avg_running_reqs,
        "Avg Swapped Reqs": avg_swapped_reqs,
        "Avg Pending Reqs": avg_pending_reqs,
        "Avg GPU KV Cache Usage": avg_gpu_kv_cache_usage,
        "Avg CPU KV Cache Usage": avg_cpu_kv_cache_usage,
        "Log Entries Counted": count,
    }


log_file_path = "lunaris-79ddc8b959-hgkc2_vllm-container.log"
results = parse_log_file(log_file_path)

for key, value in results.items():
    print(f"{key}: {value}")
