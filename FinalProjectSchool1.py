import os
import random
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

# List of Russian cities and their corresponding image file names
cities = {
    'Москва': ['moscow1.jpg', 'moscow2.jpg', 'moscow3.jpg'],
    'Санкт Петербург': ['stpetersburg1.jpg', 'stpetersburg2.jpg', 'stpetersburg3.jpg'],
    'Новосибирск': ['novosibirsk1.jpg', 'novosibirsk2.jpg', 'novosibirsk3.jpg'],
    'Екатеринбург': ['yekaterinburg1.jpg', 'yekaterinburg2.jpg', 'yekaterinburg3.jpg'],
    'Казань': ['kazan1.jpg', 'kazan2.jpg', 'kazan3.jpg'],
    'Нижний Новгород': ['nizhny_novgorod1.jpg', 'nizhny_novgorod2.jpg', 'nizhny_novgorod3.jpg'],
    'Ростов на Дону': ['rostov_on_don1.jpg', 'rostov_on_don2.jpg', 'rostov_on_don3.jpg'],
    'Красноярск': ['krasnoyarsk1.jpg', 'krasnoyarsk2.jpg', 'krasnoyarsk3.jpg'],
    'Пермь': ['perm1.jpg', 'perm2.jpg', 'perm3.jpg'],
    'Воронеж': ['voronezh1.jpg', 'voronezh2.jpg', 'voronezh3.jpg']
}

def get_random_city():
    """Получить случайный город из списка"""
    return random.choice(list(cities.keys()))

def get_random_image(city):
    """Получить случайное изображение для указанного города"""
    return random.choice(cities[city])

def play_game():
    """Играйте в GeoGuesser game"""
    root = tk.Tk()
    root.title('GeoGuesser Russia by Sergey K')

    city = get_random_city()
    image_file = get_random_image(city)

    # Display image
    image_path = os.path.join('images', image_file)
    image = Image.open(image_path)
    new_image = image.resize((500, 500))
    new_image.save('myimage_500.jpg')
    photo = ImageTk.PhotoImage(new_image)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()

    # Ask player to guess the city
    entry = tk.Entry(root)
    entry.pack()

    def check_guess():
        guess = entry.get()
        if guess.lower() == city.lower():
            score = score + 1 
            messagebox.showinfo('Правильно! ', 'Вы угадали!' , f'Ваш результат {score}')
            
            
        else:
            messagebox.showerror('Неправильный', f'Извините, правильный ответ был {city}' , f'Ваш результат {score}' )
        root.destroy()

    button = tk.Button(root, text='Угадывай', command=check_guess)
    button.pack()

    root.mainloop()
    play_game()
    

play_game()
