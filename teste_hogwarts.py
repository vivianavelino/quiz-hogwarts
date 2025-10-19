# 🧙‍♀️ Teste das Casas de Hogwarts

grifinoria = 0
corvinal = 0
lufalufa = 0
sonserina = 0

# Pergunta 1
print("Q1) Você gosta do Amanhecer ou Anoitecer?\n")
print("1) Amanhecer")
print("2) Anoitecer\n")

resposta = int(input("Digite sua resposta (1-2): "))

if resposta == 1:
    grifinoria += 1
    corvinal += 1
elif resposta == 2:
    lufalufa += 1
    sonserina += 1
else:
    print("⚠️ Entrada inválida.\n")

# Pergunta 2
print("\nQ2) Quando eu morrer, quero que as pessoas se lembrem de mim como:\n")
print("1) O bom")
print("2) O grande")
print("3) O sábio")
print("4) O ousado\n")

resposta = int(input("Digite sua resposta (1-4): "))

if resposta == 1:
    lufalufa += 2
elif resposta == 2:
    sonserina += 2
elif resposta == 3:
    corvinal += 2
elif resposta == 4:
    grifinoria += 2
else:
    print("⚠️ Entrada inválida.\n")

# Pergunta 3
print("\nQ3) Qual tipo de instrumento mais agrada ao seu ouvido?\n")
print("1) O violino")
print("2) O trompete")
print("3) O piano")
print("4) O tambor\n")

resposta = int(input("Digite sua resposta (1-4): "))

if resposta == 1:
    sonserina += 4
elif resposta == 2:
    lufalufa += 4
elif resposta == 3:
    corvinal += 4
elif resposta == 4:
    grifinoria += 4
else:
    print("⚠️ Entrada inválida.\n")

# Resultado final
print("\n🔹 RESULTADO FINAL 🔹")
print(f"Grifinória: {grifinoria}")
print(f"Lufa-Lufa: {lufalufa}")
print(f"Corvinal: {corvinal}")
print(f"Sonserina: {sonserina}\n")

print("✨ O Chapéu Seletor escolheu... ✨\n")

if grifinoria >= corvinal and grifinoria >= lufalufa and grifinoria >= sonserina:
    print("🦁 GRIFINÓRIA!\n")
elif corvinal >= lufalufa and corvinal >= sonserina:
    print("🦅 CORVINAL!\n")
elif lufalufa >= sonserina:
    print("🦡 LUFA-LUFA!\n")
else:
    print("🐍 SONSERINA!\n")
