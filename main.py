from pyscript import document, display

def btnp(e):
    document.getElementById('result').innerHTML = ' '
    element_symbol = document.getElementById('input').value.upper().strip()
    symbol = element_symbol

    element_list = {
        'C': 'Symbol: C // Element: Carbon // Atomic Number: 6 // Atomic Mass: 12.011',
        'F': 'Symbol: F // Element: Flourine // Atomic Number: 9 // Atomic Mass: 18.998',
        'HE': 'Symbol: HE // Element: Helium // Atomic Number: 2 // Atomic Mass: 4.003',
        'NE': 'Symbol: NE // Element: Neon// Atomic Number: 10 // Atomic Mass: 20.180',
        'AR': 'Symbol: AR // Element: Argon // Atomic Number: 18 // Atomic Mass: 39.948',
        'CL': 'Symbol: CL // Element: Chlorine // Atomic Number: 17 // Atomic Mass: 35.453'
        }
    # elementDetails = document.getElementById('element_list')
    element_checker = symbol in element_list

    display_message = (f'Sorry {symbol} is not a non-metal.', element_list.get(symbol))

    display(display_message[element_checker], target='result', append=False )
