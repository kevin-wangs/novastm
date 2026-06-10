# Novastm

<div align="center">

**Streaming data pipeline framework for GPU-accelerated workloads**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ROCm](https://img.shields.io/badge/AMD%20ROCm-powered-orange.svg)]()

</div>

## Overview

Novastm handles high-throughput ETL, buffer management, and real-time data flow between host and device memory. Built on ROCm pinned memory for zero-copy transfers.

## Features
- Async pipeline stages with backpressure control
- Pinned memory buffers (ROCm hipHostMalloc)
- Smart micro-batching for GPU throughput
- Stream-aware I/O with HIP streams
- Multiple source/sink connectors

## Quick Start
```python
from novastm import Pipeline, Stage

pipe = Pipeline([
    Stage("load", fn=load_data, n_workers=4),
    Stage("transform", fn=process, n_workers=2),
    Stage("upload", fn=to_gpu, n_workers=1),
])
pipe.run(source="/data/*.parquet")
```

## Requirements
- Python 3.9+
- Optrix 0.1+
- AMD ROCm 6.0+ (optional)


---

**Developed by Apex Ridge Technologies, Inc.**

2805 E Cottonwood Pkwy, Suite 100, Salt Lake City, UT 84121
