import pandas as pd
import matplotlib.pyplot as plt
import openpyxl 
import numpy as np
import openai

openai.api_key = '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'
def get_response_from_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # или другой доступный вам модель
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

print('введите ваши промпты в gpt по примеру из Readme')
years_input = input("Введите ваш запрос(года): ")
rates_input = input("Введите ваш запрос(показатели): ")

years_response = get_response_from_gpt(years_input)
rates_response = get_response_from_gpt(rates_input)

if not isinstance(years_response, list):
    years_response = [years_response]

if not isinstance(rates_response, list):
    rates_response = [rates_response]
data = {
    # 'Год': [2013, 2014, 2015, 2016, 2017, 2018, 2019,2020,2021,2022,2023],
    # 'Показатель': [6.5, 11.4, 12.9, 5.4, 3.7, 2.9, 3.0, 3.4, 8.4, 12.0, 6.5  ]
    'Years': (years_response),
    'Rates': (rates_response)
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.bar(df['Years'], df['Rates'], color='blue')
plt.title('Динамика показателя по годам')
plt.xlabel('Год')
plt.ylabel('Показатель')
plt.grid(axis='y')

plt.savefig('chart.png')

plt.figure(figsize=(10, 6))
plt.bar(df['Years'], df['Rates'], alpha=1, color='white', edgecolor='black', label='Набор данных 1')
plt.title('Гистограмма данных')
plt.xlabel('Значение')
plt.ylabel('Частота')

plt.savefig('histogram.png')

