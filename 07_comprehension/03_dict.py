prices = {
    "Masala chai": 20,
    "Elaichi tea": 45,
    "Spicy Chai": 30,
}

inDollar = {tea:price / 100 for tea, price in prices.items()}
print(inDollar)