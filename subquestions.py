def calculate_ticket_price(seats, timing, is_weekend):
    prices = {
        "VIP": 500,
        "REGULAR": 300,
        "ECONOMY": 150
    }

    timing_multiplier = {
        "morning": 0.8,
        "afternoon": 1,
        "evening": 1.2,
        "night": 1.5
    }

    valid_seats = [s for s in seats if s in prices]

    if not valid_seats:
        return "No valid booking"

    # Base total
    base_total = sum(prices[s] for s in valid_seats)

    # Timing adjustment
    timing_total = base_total * timing_multiplier[timing]

    # Weekend
    if is_weekend:
        timing_total *= 1.10

    # Discount
    discount = 0
    if len(valid_seats) >= 5:
        discount = timing_total * 0.15
        timing_total -= discount

    # Booking fee
    booking_fee = 50 * len(valid_seats)
    total_with_fee = timing_total + booking_fee

    # GST
    tax = total_with_fee * 0.12

    final_amount = round(total_with_fee + tax)

    return {
        "base_total": base_total,
        "timing_adjustment": round(timing_total),
        "discount": round(discount),
        "tax": round(tax),
        "final_amount": final_amount
    }