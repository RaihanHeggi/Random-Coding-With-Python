import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def swap(listSorting, i, j):
    if i != j:
        listSorting[i], listSorting[j] = listSorting[j], listSorting[i]


def selectionSortAscending(listSorting):
    if len(listSorting) == 1:
        return

    for i in range(len(listSorting)):
        # Find minimum unsorted value.
        minValue = listSorting[i]
        minIndex = i
        for j in range(i, len(listSorting)):
            if listSorting[j] < minValue:
                minValue = listSorting[j]
                minIndex = j
            yield listSorting
        swap(listSorting, i, minIndex)
        yield listSorting


def selectionSortDescending(listSorting):
    if len(listSorting) == 1:
        return

    for i in range(len(listSorting)):
        # Find minimum unsorted value.
        minValue = listSorting[i]
        minIndex = i
        for j in range(i, len(listSorting)):
            if listSorting[j] > minValue:
                minValue = listSorting[j]
                minIndex = j
            yield listSorting
        swap(listSorting, i, minIndex)
        yield listSorting


def update_fig(listSorting, rects, iteration, start, text):
    for rect, val in zip(rects, listSorting):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("Number Of Iteration {}".format(iteration[0]))
    text.set_text("Time Elapse {}".format(time.time() - start))


def main():
    # Build and randomly shuffle list of integers.
    listSorting = [x + 1 for x in range(50)]
    random.seed(time.time())
    random.shuffle(listSorting)

    # Choice to Ascending or Descending Sort
    choice = input("Ascending (1) or Descending (2) : ")
    if choice == "1":
        generator = selectionSortAscending(listSorting)
    elif choice == "2":
        generator = selectionSortDescending(listSorting)
    else:
        raise Exception

    try:
        start = time.time()

        # Initialize figure and axis.
        fig, ax = plt.subplots()
        ax.set_title("Selection Sort")

        # Initialize a bar plot. Note that matplotlib.pyplot.bar() returns a
        # list of rectangles (with each bar in the bar plot corresponding
        # to one rectangle), which we store in bar_rects.
        bar_rects = ax.bar(range(len(listSorting)), listSorting, align="edge")

        # Set axis limits. Set y axis upper limit high enough that the tops of
        # the bars won't overlap with the text label.
        ax.set_xlim(0, len(listSorting))
        ax.set_ylim(0, int(2 * len(listSorting)))

        # Place a text label in the upper-left corner of the plot to display
        # number of operations performed by the sorting algorithm (each "yield"
        # is treated as 1 operation).
        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
        text_2 = ax.text(0.02, 0.90, "", transform=ax.transAxes)

        # Define function update_fig() for use with matplotlib.pyplot.FuncAnimation().
        # To track the number of operations, i.e., iterations through which the
        iteration = [0]

        def update_fig(listSorting, rects, iteration):
            for rect, val in zip(rects, listSorting):
                rect.set_height(val)
            iteration[0] += 1
            text.set_text("Number Of Iteration {}".format(iteration[0]))
            text_2.set_text("Time Elapse {}".format(time.time() - start))

        anim = animation.FuncAnimation(
            fig,
            func=update_fig,
            fargs=(bar_rects, iteration),
            frames=generator,
            interval=1,
            repeat=False,
        )
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

