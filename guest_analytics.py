# Disney IT: Guest Analytics & Privacy Dashboard
# Developed by: Nyla Dickerson - IT Major @ Towson University

def run_guest_dashboard():
    # Simulated Guest Data (Name, MagicBand ID, Age)
    raw_guests = [
        {"name": "Tiana", "mb_id": "9876543210", "age": 24},
        {"name": "Naveen", "mb_id": "1234567890", "age": 26},
        {"name": "Louis", "mb_id": "1122334455", "age": 35}
    ]

    print("--- 🏰 Disney IT Dashboard: Secure Analytics ---")
    
    total_age = 0
    
    for guest in raw_guests:
        # SECURITY: Mask the MagicBand ID 
        masked_id = "*" * 6 + guest["mb_id"][-4:]
        
        # DATA: Accumulate age for analytics 
        total_age += guest["age"]
        
        print(f"Guest: {guest['name']} | Secure ID: {masked_id} | Status: Active")

    # Analytics Calculation
    avg_age = total_age / len(raw_guests)
    print(f"\n--- 📊 Park Insights ---")
    print(f"Average Guest Age: {avg_age:.1f}")
    print("Compliance Check: All Guest IDs have been masked per Privacy Standards.")

if __name__ == "__main__":
    run_guest_dashboard()
