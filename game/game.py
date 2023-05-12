import random


def choose_options():
  options = ('piedra', 'papel', 'tijera')
  pc_option = random.choice(options)
  user_input = input("escoge, pieda, papel o tijera =>")
  user_option = user_input.lower()

  if not user_option in options:
    print("escoge una opcion valida")
    print(user_option)
    print('pc option=>', pc_option)
    return None, None
    #continue

  print('User option =>', user_option)
  print('Computer option =>', pc_option)
  return user_option, pc_option


def check_rules(user_option, pc_option, pc_points, user_points):
  if user_option == pc_option:
    print("empate")

  elif user_option == "tijera":
    if pc_option == "piedra":
      print("piedra gana, tu perdiste")
      pc_points += 1
    else:
      print("Ganaste")
      user_points += 1

  elif user_option == "papel":
    if pc_option == "tijera":
      print("tijera gana, tu perdiste")
      pc_points += 1
    else:
      print("Ganaste")
      user_points += 1

  elif user_option == "piedra":
    if pc_option == "papel":
      print("papel gana, tu perdiste")
      pc_points += 1
    else:
      print("Ganaste")
      user_option
      user_points += 1

  return user_points, pc_points


def run_game():
  round = 0
  pc_points = 0
  user_points = 0
  while True:
    round += 1
    print('*' * 12)
    print('Round', round)
    print('*' * 12)
    print('USER =>', user_points)
    print('PC =>', pc_points)

    user_option, pc_option = choose_options()
    user_points, pc_points = check_rules(user_option, pc_option, user_points,
                                         pc_points)

    if pc_points == 3 or user_points == 3:
      print(
        f'SE ACABO OBTUVISTE {user_points} PUNTOS Y LA PC OBTUVO {pc_points} PUNTOS'
      )
      break


run_game()
