def celsius_to_fahrenheit(celsius):
    """Mengkonversi suhu dari Celsius ke Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """Mengkonversi suhu dari Celsius ke Kelvin."""
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    """Mengkonversi suhu dari Fahrenheit ke Celsius."""
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    """Mengkonversi suhu dari Fahrenheit ke Kelvin."""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_celsius(kelvin):
    """Mengkonversi suhu dari Kelvin ke Celsius."""
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """Mengkonversi suhu dari Kelvin ke Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def main():
    print("Pilih jenis konversi suhu:")
    print("1. Celsius ke Fahrenheit")
    print("2. Celsius ke Kelvin")
    print("3. Fahrenheit ke Celsius")
    print("4. Fahrenheit ke Kelvin")
    print("5. Kelvin ke Celsius")
    print("6. Kelvin ke Fahrenheit")
    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == "1":
        c = float(input("Masukkan suhu dalam Celsius: "))
        print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
    elif pilihan == "2":
        c = float(input("Masukkan suhu dalam Celsius: "))
        print(f"{c}°C = {celsius_to_kelvin(c)}K")
    elif pilihan == "3":
        f = float(input("Masukkan suhu dalam Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_celsius(f)}°C")
    elif pilihan == "4":
        f = float(input("Masukkan suhu dalam Fahrenheit: "))
        print(f"{f}°F = {fahrenheit_to_kelvin(f)}K")
    elif pilihan == "5":
        k = float(input("Masukkan suhu dalam Kelvin: "))
        print(f"{k}K = {kelvin_to_celsius(k)}°C")
    elif pilihan == "6":
        k = float(input("Masukkan suhu dalam Kelvin: "))
        print(f"{k}K = {kelvin_to_fahrenheit(k)}°F")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
