def convert_currency(dollars):
    """Convert dollars into Philippine Peso and Japanese Yen (dictionary style)."""
    rates = {
        "peso": 57.17,   
        "yen": 146.67    
    }
    
    return {
        "peso": dollars * rates["peso"],
        "yen": dollars * rates["yen"]
    }



user_input = input("Enter currency in ($): ").replace(",", "")
dollars = float(user_input)

converted = convert_currency(dollars)

print("\nDollar ($)\tPhil Peso (₱)\tJapanese Yen (¥)")
print(f"{dollars:,.2f}\t{converted['peso']:,.2f}\t{converted['yen']:,.2f}")
