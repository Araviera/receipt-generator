from reportlab.pdfgen import canvas


def main():
    # Store information
    store_name = "Awesome Store"
    store_address = "123 Main St"
    store_phone = "0143867302845"

    # Item information


    items = [] #list of items
    print("Enter the items you want to buy and their prices. Press enter after each item. When you are done, type 'done'.")
    while True:
        item = input("Item: ")
        if item == 'done':
            break
        price = float(input("Price: "))
        items.append((item, price))

    # Calculate total
    subtotal = sum(price for _, price in items)
    tax_rate = 0.14  # 14% tax
    tax = subtotal * tax_rate
    total = subtotal + tax

    # Create a new PDF document with a descriptive title
    pdf = canvas.Canvas("receipt.pdf")

    # Set the font and font size for the store information
    pdf.setFont("Helvetica", 12)

    # Add store name, address, and phone number with appropriate spacing
    pdf.drawString(100, 700, store_name)
    pdf.drawString(50, 680, store_address)
    pdf.drawString(50, 660, store_phone)

    # Draw a horizontal line to separate header from items
    pdf.line(50, 640, 550, 640)

    # Set font and size for item description
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, 620, "Items:")

    # Set font and size for item details (name and price)
    pdf.setFont("Helvetica", 10)
    current_y = 600  # Starting position for item details

    # Loop through each item and add name and price with formatting
    for name, price in items:
        pdf.drawString(50, current_y, name)
        pdf.drawString(450, current_y, f"${price:.2f}")  # Right-align price with 2 decimal places
        current_y -= 15  # Adjust y position for next item

    # Draw a line before subtotal, tax, and total
    pdf.line(50, 560, 550, 560)

    # Set font and size for subtotal, tax, and total labels
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, 540, "Subtotal:")
    pdf.drawString(50, 520, "Tax:")
    pdf.drawString(50, 500, "Total:")

    # Set font and size for subtotal, tax, and total values
    pdf.setFont("Helvetica", 10)
    pdf.drawString(450, 540, f"${subtotal:.2f}")
    pdf.drawString(450, 520, f"${tax:.2f}")
    pdf.drawString(450, 500, f"${total:.2f}")

    # Draw a line at the bottom of the receipt
    pdf.line(50, 480, 550, 480)

    # Add a thank you message with centering
    pdf.setFont("Helvetica", 10)
    pdf.drawCentredString(300, 460, "Thank you for shopping at Awesome Store!")

    # Save the PDF document
    pdf.save()


if __name__ == "__main__":
    main()