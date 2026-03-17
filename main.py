from fpdf import FPDF


class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, given):
        if given is None or given != str(given):
            raise ValueError
        self._name = given
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if category is None or category != str(category):
            raise ValueError
        valid_category= ["food", "entertainment", "utilities", "other"]
        if category not in valid_category:
            category = "others"
        self._category = category
    @property
    def amount(self):
        return self._amount
    @amount.setter
    def amount(self, amount ):
        if amount is None or not isinstance(amount, (int, float)) or amount<0:
            raise ValueError
        self._amount = amount


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", style="B", size=50)
        self.cell(0, 20, "Expense Report", new_x="LMARGIN", new_y="NEXT", align='C')
    def footer(self):
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", style="I", size=8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def main():
    expenses = []  # Our bucket for objects
    print("Enter expenses as: Name, Category, Amount (or press Enter to finish)")
    while True:
        expense= input("Expense: ")
        if not expense:
            break
        try:
            name, category, amount = expense.split(",")
            whole = Expense(name, category, float(amount))
            expenses.append(whole)
        except ValueError:
            print("Invalid Expense")
            continue
    # if the user puts valid input then we will start printing the pdf
    if expenses:
        pdf = PDF(orientation="P", format="A4", unit= "mm")
        pdf.add_page()
        # table header
        pdf.set_font("helvetica", style="B", size= 15)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(90, 10, "Expense Item", border=1, fill=True)
        pdf.cell(50, 10, "Category", border=1, fill=True)
        pdf.cell(50, 10, "Amount", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")
         # for the dtat inside table
        pdf.set_font("helvetica", size= 12)
        pdf.set_text_color(0, 0, 0)
        for expense in expenses:
          pdf.cell(90, 10, expense.name, border=1)
          pdf.cell(50, 10, expense.category, border=1)
          pdf.cell(50, 10, f"{expense.amount:.2f}", border=1,align='R', new_x="LMARGIN", new_y="NEXT")
    pdf.output("expenses.pdf")
    print("done")




if __name__ == "__main__":
    main()











