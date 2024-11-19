# LLM Inference Fast Benchmark

This repository benchmarks the performance of large language models (LLMs) on a 7B role play model(`Sao10K/L3-8B-Lunaris-v1`) with an average input of 4k tokens and an output of 250 tokens.

## Getting Started

### Step 0: Clone the Repository
```bash
git clone https://github.com/kobe0938/llm-inference-fast-benchmark
cd llm-inference-fast-benchmark
```

### Step 1: Terminal Setup and Commands

#### Terminal 1: Start the API Server
```bash
source env/bin/activate

pip install vllm

python3 -m vllm.entrypoints.openai.api_server \
    --model Sao10K/L3-8B-Lunaris-v1 \
    --max-model-len 8192 \
    --swap-space 4 \
    --dtype auto \
    --enable-chunked-prefill \
    --disable-log-requests \
    --enable-prefix-caching \
    --port 8081 \
    --root-path /api \
    --served-model-name sao10k/l3-8b-lunaris \
    --max-num-seqs 36
```

#### Terminal 2: Benchmark Script
**1st time run:**

```bash
source env/bin/activate

pip install -r requirements.txt

python run.py \
    --rounds 1 \
    -q 1 \
    --api-base http://localhost:8081/api/v1 \
    --model sao10k/l3-8b-lunaris \
    --max-tokens 250 \
    --prompt-file prompt-1k.txt \
    --random-tokens 3000 \
    --use-chat
```

**2nd and onwards run:**

```bash
source env/bin/activate

python run.py \
    --rounds 1 \
    -q 1 \
    --api-base http://localhost:8081/api/v1 \
    --model sao10k/l3-8b-lunaris \
    --max-tokens 250 \
    --prompt-file prompt-1k.txt \
    --random-tokens 3000 \
    --use-chat
```

#### Terminal 3: Monitor GPU Usage
```bash
watch -n 1 nvidia-smi
```


---

Happy benchmarking!
