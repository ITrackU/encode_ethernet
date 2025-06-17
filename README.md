# Ethernet Encoders in Python with Matplotlib Visualization

This repository contains Python implementations of various Ethernet encoding schemes, ranging from Manchester encoding to the 64b/66b encoding. Each encoder is designed to illustrate how data is encoded for transmission in Ethernet networks, accompanied by visualizations created using Matplotlib to help you understand the signal transformations.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Supported Encodings](#supported-encodings)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Examples](#examples)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview

Ethernet communication relies on various encoding schemes to ensure reliable data transmission. This project implements a range of these encoding techniques in Python, from the simpler Manchester encoding to complex schemes like 64b/66b. The focus is not only on encoding the bitstreams but also on visualizing the resulting waveforms to facilitate learning and analysis.

---

## Supported Encodings

- **Manchester Encoding**  
- **Differential Manchester Encoding**  
- **4B/5B Encoding**  
- **8B/10B Encoding**  
- **64b/66b Encoding**  

---

## Features

- Pure Python implementations for educational purposes  
- Waveform visualization using Matplotlib for each encoding  
- Modular design for easy extension and testing  
- Sample input data and corresponding encoded waveforms  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ethernet-encoders-python.git
   cd ethernet-encoders-python
    ```
(Optional) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

    pip install -r requirements.txt

Usage

Each encoding module contains functions to encode a binary input string and generate a plot of the encoded signal.

Example usage for Manchester encoding:

from encoders.manchester import manchester_encode
import matplotlib.pyplot as plt

data = "11010011"
encoded_signal = manchester_encode(data)

plt.plot(encoded_signal)
plt.title("Manchester Encoding")
plt.xlabel("Time")
plt.ylabel("Signal Level")
plt.show()

Examples

See the /examples directory for sample scripts demonstrating each encoder with visual output.
Contributing

Contributions are welcome! Please open issues or submit pull requests for new encodings, bug fixes, or enhancements.
License

This project is licensed under the MIT License. See the LICENSE file for details.
