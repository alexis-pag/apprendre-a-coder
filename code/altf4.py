import keyboard

# Bloquer plusieurs touches et combinaisons
combinaisons = ["alt+f4", "alt+tab", "win", "ctrl+esc"]

for combo in combinaisons:
    keyboard.block_key(combo)

print("Touches bloquées : Alt+F4, Alt+Tab, Win, Ctrl+Esc")
print("Appuie sur ECHAP (ESC) pour quitter et réactiver les touches.")

# Attente de la touche ESC pour arrêter le script
keyboard.wait("esc")

