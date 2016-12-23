import matplotlib.pyplot as plt

def draw_pie_chart(percentages, colors, labels, explode):
    plt.pie(percentages, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()
