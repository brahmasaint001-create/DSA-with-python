class MetroTicketMachine:
    def __init__(self):
        # Sample North-South Kolkata Metro Stations in order
        self.stations = [
            "Kavi Subhash", "Masterda Surya Sen", "Gitanjali", 
            "Netaji", "Mahanayak Uttam Kumar", "Rabindra Sarobar", 
            "Kalighat", "Jatin Das Park", "Netaji Bhavan", 
            "Rabindra Sadan", "Maidan", "Park Street", 
            "Esplanade", "Chandni Chowk", "Central"
        ]
        # Simplified fare chart based on station gaps
        # 0-2 stations = ₹5, 3-5 stations = ₹10, 6-9 stations = ₹15, 10+ stations = ₹20
        self.base_balance = 10000  # Mock machine vault balance

    def display_stations(self):
        print("\n--- AVAILABLE METRO STATIONS ---")
        for index, station in enumerate(self.stations, start=1):
            print(f"{index}. {station}")
        print("--------------------------------")

    def calculate_fare(self, start_idx, end_idx):
        station_gap = abs(start_idx - end_idx)
        if station_gap <= 2:
            return 5
        elif station_gap <= 5:
            return 10
        elif station_gap <= 9:
            return 15
        else:
            return 20

    def start_machine(self):
        print("=======================================")
        print("    WELCOME TO KOLKATA METRO VENDING   ")
        print("=======================================")
        
        while True:
            self.display_stations()
            
            try:
                # 1. Source Selection
                src_choice = int(input("\nSelect Source Station Number (or 0 to exit): "))
                if src_choice == 0:
                    print("Thank you for using Kolkata Metro Services!")
                    break
                if not (1 <= src_choice <= len(self.stations)):
                    print("Invalid station choice. Please try again.")
                    continue
                
                # 2. Destination Selection
                dest_choice = int(input("Select Destination Station Number: "))
                if not (1 <= dest_choice <= len(self.stations)):
                    print("Invalid station choice. Please try again.")
                    continue
                
                if src_choice == dest_choice:
                    print("Source and Destination cannot be the same!")
                    continue

                # 3. Passenger Count
                passengers = int(input("Enter number of passengers (Max 5): "))
                if not (1 <= passengers <= 5):
                    print("Invalid passenger count! You can book between 1 and 5 tickets.")
                    continue

                # 4. Calculation
                single_fare = self.calculate_fare(src_choice - 1, dest_choice - 1)
                total_fare = single_fare * passengers
                
                source_name = self.stations[src_choice - 1]
                dest_name = self.stations[dest_choice - 1]
                
                print("\n=======================================")
                print("            TICKET SUMMARY             ")
                print("=======================================")
                print(f"From:        {source_name}")
                print(f"To:          {dest_name}")
                print(f"Passengers:  {passengers}")
                print(f"Fare/Ticket: ₹{single_fare}")
                print(f"Total Amount:₹{total_fare}")
                print("=======================================")
                
                # 5. Payment Simulation
                confirm = input("Proceed to payment? (yes/no): ").strip().lower()
                if confirm != 'yes':
                    print("Transaction cancelled.")
                    continue
                    
                print(f"\nPlease insert cash or scan QR for ₹{total_fare}...")
                inserted_amount = int(input("Enter amount paid (Simulated Cash Input): ₹"))
                
                if inserted_amount < total_fare:
                    print("Insufficient amount! Transaction failed. Refunding money...")
                else:
                    change = inserted_amount - total_fare
                    print("\nProcessing tickets...")
                    print("=======================================")
                    print("         SUCCESSFULLY BOOKED!          ")
                    print("=======================================")
                    if change > 0:
                        print(f"Please collect your change: ₹{change}")
                    print("Please collect your paper tokens/QR tickets!")
                    print("Have a safe journey!")
                    print("=======================================\n")
                    
            except ValueError:
                print("Invalid input format! Please enter numeric numbers only.")

# Run the program
if __name__ == "__main__":
    machine = MetroTicketMachine()
    machine.start_machine()
