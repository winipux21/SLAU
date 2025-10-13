import matplotlib.pyplot as plt
import json

class FinancialDashboard:
    """
    Панель финансовых метрик, визуализация структуры расходов,
    доходов, динамики активов по месяцам (bar, pie chart).
    """
    def __init__(self, finance_file):
        with open(finance_file, "r", encoding="utf-8") as f:
            self.data = json.load(f)
        self.metrics = {}

    def aggregate(self):
        income = sum(i["amount"] for i in self.data["items"] if i["type"] == "income")
        expense = sum(i["amount"] for i in self.data["items"] if i["type"] == "expense")
        by_category = {}
        for i in self.data["items"]:
            by_category.setdefault(i["category"], 0)
            by_category[i["category"]] += i["amount"]
        self.metrics = {"income": income, "expense": expense, "by_category": by_category}

    def plot_pie_expenses(self):
        expenses = {cat: val for cat, val in self.metrics["by_category"].items() if val < 0 or cat not in ["Зарплата","Фриланс"]}
        plt.pie(list(expenses.values()), labels=list(expenses.keys()), autopct='%1.1f%%')
        plt.title("Структура расходов")
        plt.show()

    def plot_income_vs_expense(self):
        plt.bar(["Доходы", "Расходы"], [self.metrics["income"], self.metrics["expense"]], color=["green", "red"])
        plt.title("Доходы vs Расходы")
        plt.show()

if __name__ == "__main__":
    dashboard = FinancialDashboard("budget_data.json")
    dashboard.aggregate()
    dashboard.plot_income_vs_expense()
    dashboard.plot_pie_expenses()
