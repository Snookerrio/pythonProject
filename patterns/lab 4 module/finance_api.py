import mysql.connector
import requests

# Параметри підключення до бази даних
db_config = {
    'user': 'root',
    'password': 'romadb52',
    'host': 'localhost',
    'database': 'finance_data'
}

API_HOST = "real-time-finance-data.p.rapidapi.com"

# Функція для отримання ціни акцій
def get_stock_quote(symbol):
    url = "https://real-time-finance-data.p.rapidapi.com/stock-quote"
    headers = {
        "X-RapidAPI-Host": API_HOST,
        "X-RapidAPI-Key": "23e06aa874mshf3aee18d0f86424p105ed1jsn9b1a25705076"
    }

    params = {
        'symbol': symbol
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f'Error: {response.status_code}')
        return None


# Функція для збереження даних у базі даних
def save_to_db(stock_data):
    try:
        # Перевіряємо, чи всі необхідні поля присутні
        required_fields = ['symbol', 'price', 'open', 'high', 'low', 'volume', 'previous_close', 'change', 'change_percent', 'last_update_utc']
        for field in required_fields:
            if field not in stock_data:
                print(f"Missing field: {field}")
                return

        with mysql.connector.connect(**db_config) as conn:
            cursor = conn.cursor()
            insert_query = '''
            INSERT INTO stock_prices (symbol, price, open, high, low, volume, previous_close, `change`, change_percent, last_update_utc)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

            cursor.execute(insert_query, (
                stock_data['symbol'],
                stock_data['price'],
                stock_data['open'],
                stock_data['high'],
                stock_data['low'],
                stock_data['volume'],
                stock_data['previous_close'],
                stock_data['change'],
                stock_data['change_percent'],
                stock_data['last_update_utc']
            ))

            conn.commit()
            print(f'Data for {stock_data["symbol"]} saved to database.')

    except mysql.connector.Error as err:
        print(f"Database error: {err}")

# Основна частина програми
if __name__ == '__main__':
    symbol = input('Enter the stock symbol (e.g., AAPL for Apple): ')
    stock_data = get_stock_quote(symbol)
    if stock_data:
        save_to_db(stock_data)