from trusted_center import SelectingSystemParameters
from alice_and_hacker import SelectingUserSecrets, Hacker
from round import ProtocolMessages

def identify_user():
    """Идентификация"""
    return input("\nПожалуйста, представьтесь: ").lower()

def perform_identification(n, k, t, s, b, v):
    """Аутентификация для t раундов"""
    result = []
    for i in range(1, t + 1):
        print(f"\nВыполнение раунда №{i}")
        x, r = ProtocolMessages.x_calculation(n, b)
        e = ProtocolMessages.random_vector_generation(k)
        y = ProtocolMessages.y_calculation(r, e, s, n)
        z = ProtocolMessages.z_calculation(y, v, e, n)
        result.append(ProtocolMessages.identification(x, z, n))
        if x == z:
            print(f"x = {x}")
            print(f"z = {z}")
        elif x != z:
            x = -x % n
            print(f"x = {x}")
            print(f"z = {z}")
    return result

if __name__ == '__main__':
    who_are_you = identify_user()

    # Выбор системных параметров доверенным центром
    n = SelectingSystemParameters.generate_n()
    k, t = SelectingSystemParameters.generate_security_params()

    # Алиса/хакер генерирует открытый и закрытый ключ
    alice = SelectingUserSecrets(n, k)
    s, b = alice.select_user_secrets()
    v = alice.v_calculation()

    if who_are_you in ["alice", "a", "а", "алиса"]:
        open_key_v, close_key_s = alice.keys()
        print("\nОткрытый ключ:", open_key_v)
        print("Закрытый ключ:", close_key_s)
    else:
        print("\nХакер узнал открытый ключ")
        hacker = Hacker(n, k, v) 
        s = hacker.hacker_generates_s()
        open_key_v, close_key_s = hacker.keys()
        print("\nОткрытый ключ:", open_key_v)
        print("Закрытый ключ:", close_key_s)

    print(f"\nОтправка открытого ключа {open_key_v} от А к В...")

    identification_result = perform_identification(n, k, t, s, b, v)

    if False not in identification_result:
        print("\nИдентификация прошла успешно\n")
    else:
        print("\nИдентификация провалена\n")