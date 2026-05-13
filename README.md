# Webcam Random Number Generator

A Python tool that generates true random numbers using webcam frames as an entropy source. Each frame captured by the camera is hashed with SHA-256, making every number genuinely unpredictable.

## How it works

Instead of using pseudo-random algorithms, the program captures a live webcam frame and runs it through SHA-256 hashing. Since every frame is slightly different due to light, noise and motion, the output is truly random.

## Features

- Generate a random integer from a SHA-256 hash
- Generate random numbers in a custom range
- Run n generations of numbers from 1 to 5 with percentage stats and elapsed time
- Base64 encoded hash output

## Requirements

pip install opencv-python

## How to use

Run the script and use the following keys in the camera window:

- `0` — quit
- `1` — generate a random integer
- `2` — run n generations (1-5) with stats
- `3` — generate a number in a custom range
- `4` — base64 hash output
