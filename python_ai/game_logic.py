class Liquid:
    def __init__(self, type, state='liquid'):
        self.type = type
        self.state = state  # 'liquid', 'solid', 'gas'

    def transform(self, new_state):
        self.state = new_state

def play_puzzle():
    water = Liquid('water')
    print(f"Start: {water.type} in state {water.state}")
    water.transform('steam')
    print(f"Transformed to: {water.state}")

if __name__ == "__main__":
    play_puzzle()
