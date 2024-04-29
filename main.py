import tkinter as tk
import csv

class FlowerCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flower Counter")
        self.root.geometry("400x300")  # Adjusted size for 1080p screen

        self.total_sum = 0
        self.history = []

        self.total_label = tk.Label(root, text="Total: 0", font=("Helvetica", 20))
        self.total_label.pack()

        self.history_label = tk.Label(root, text="History:", font=("Helvetica", 14))
        self.history_label.pack()

        self.add_button_7 = tk.Button(root, text="Add 7", font=("Helvetica", 14), command=lambda: self.add_number(7))
        self.add_button_7.pack()

        self.add_button_9 = tk.Button(root, text="Add 9", font=("Helvetica", 14), command=lambda: self.add_number(9))
        self.add_button_9.pack()

        self.add_button_11 = tk.Button(root, text="Add 11", font=("Helvetica", 14), command=lambda: self.add_number(11))
        self.add_button_11.pack()

        self.delete_button = tk.Button(root, text="Delete Last", font=("Helvetica", 14), command=self.delete_last)
        self.delete_button.pack()

        self.generate_button = tk.Button(root, text="Generate Combinations", font=("Helvetica", 14), command=self.generate_combinations)
        self.generate_button.pack()

    def add_number(self, number):
        self.total_sum += number
        self.history.append(number)

        self.update_display()

    def delete_last(self):
        if self.history:
            last_number = self.history.pop()
            self.total_sum -= last_number

            self.update_display()

    def update_display(self):
        self.total_label.config(text="Total: {}".format(self.total_sum))
        self.update_history_label()

    def update_history_label(self):
        history_text = "History: "
        for num in self.history:
            history_text += str(num) + ", "
        self.history_label.config(text=history_text)

    def generate_combinations(self):
        combinations = set()
        self.generate_combinations_helper(self.total_sum, [], combinations)
        self.save_combinations_to_csv(combinations)

    def generate_combinations_helper(self, target, current_history, combinations):
        if sum(current_history) == target:
            combinations.add(tuple(current_history))
            return

        if sum(current_history) > target:
            return

        for number in [7, 9, 11]:
            current_history.append(number)
            self.generate_combinations_helper(target, current_history, combinations)
            current_history.pop()

    def save_combinations_to_csv(self, combinations):
        with open("combinations.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Total", "History"])
            for combination in combinations:
                total = sum(combination)
                history = ", ".join(map(str, combination))
                writer.writerow([total, history])

def main():
    root = tk.Tk()
    app = FlowerCounterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
