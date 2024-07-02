# Awesome Store Receipt Generator

This Python program generates a receipt for purchases made at the "Awesome Store". It's a simple command-line application that allows users to input items they wish to purchase along with their prices. After all items are entered, the program calculates the total cost including tax.

## Example receipt:
![image](https://github.com/Araviera/receipt-generator/assets/108753652/6de24904-be26-45ef-b07b-5b12ae298687)

## Features

- **User Input for Items**: Users can input the name and price of each item they wish to purchase.
- **Dynamic Item Addition**: Items can be added continuously until the user types 'done'.
- **Tax Calculation**: Automatically calculates the total cost including a predefined tax rate.

## Requirements

To run this program, you need to have Python installed on your machine. Additionally, the `reportlab` library is required for PDF generation capabilities.

## Installation

1. Ensure Python is installed on your system.
2. Install the `reportlab` library using pip:

```bash
pip install reportlab
