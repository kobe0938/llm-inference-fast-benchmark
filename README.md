# LLM Inference Fast Benchmark

This repository benchmarks the performance of large language models (LLMs) on an 8B role-play model (`Sao10K/L3-8B-Lunaris-v1`) with an average input of 4k tokens and an output of 250 tokens.

---

## Getting Started

### Step 0: Clone the Repository

```bash
git clone https://github.com/kobe0938/llm-inference-fast-benchmark
cd llm-inference-fast-benchmark
```

---

## Terminal 1: Start Server

```bash
source env/bin/activate
```

### Option A: VLLM Server

```bash
# Install VLLM
pip install vllm

# Start the VLLM Server
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

### Option B: SGLang Server

```bash
# Install SGLang and FlashInfer
pip install --upgrade pip
pip install "sglang[all]"

# Install FlashInfer accelerated kernels (CUDA only for now)
pip install flashinfer -i https://flashinfer.ai/whl/cu121/torch2.4/

# Start the SGLang Server
python3 -m sglang.launch_server \
    --model-path Sao10K/L3-8B-Lunaris-v1 \
    --port 8081 \
    --host 0.0.0.0 \
    --context-length 8192 \
    --dtype bfloat16 \
    --enable-metrics \
    --decode-log-interval 50
```

---

## Terminal 2: Run Benchmark Script

### 1st Time Run Only

```bash
source env/bin/activate
pip install -r requirements.txt
```

### 2nd Time and onwards

#### Option A: VLLM

```bash
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

#### Option B: SGLang Server

```bash
python run.py \
    --rounds 1 \
    -q 1 \
    --api-base http://localhost:8081/v1 \
    --model sao10k/l3-8b-lunaris \
    --max-tokens 250 \
    --prompt-file prompt-1k.txt \
    --random-tokens 3000 \
    --use-chat
```

---

## Terminal 3: Monitor GPU Usage

```bash
watch -n 1 nvidia-smi
```

---

## Terminal 4 (Optional): Get Metrics

```bash
curl http://localhost:8081/metrics
```

---

Happy benchmarking! 😊

