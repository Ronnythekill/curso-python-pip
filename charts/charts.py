import matplotlib.pyplot as plt

def generate_pie_chart(a, b, c):
    labels = ['A', 'B', 'C']
    values = [a, b, c]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.savefig('pie.png')
    plt.close