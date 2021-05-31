# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# img = mpimg.imread("images/UNC-logo.png")
# plt.imshow(img)
# plt.show()

import tkinter as tk

root = tk.Tk()
photo = tk.PhotoImage(file = "images/UNC-logo.png")
w = tk.Label(root, image=photo)
w.pack()

root.mainloop()
